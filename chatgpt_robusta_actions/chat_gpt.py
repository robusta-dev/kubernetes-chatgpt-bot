from robusta.api import *
import openai
from openai.openai_object import OpenAIObject


class ChatGPTTokenParams(ActionParams):
    """
    :var token: ChatGPT auth token
    """
    chat_gpt_token: str


class ChatGPTParams(ChatGPTTokenParams):
    """
    :var search_term: ChatGPT search term
    :var token: ChatGPT auth token
    :var model: ChatGPT OpenAi API model
    """
    search_term: str
    model: str = "text-davinci-003"


@action
def show_chat_gpt_search(event: ExecutionBaseEvent, params: ChatGPTParams):
    """
    Add a finding with ChatGPT top results for the specified search term.
    This action can be used together with the stack_overflow_enricher.
    """
    openai.api_key = params.chat_gpt_token
    res: OpenAIObject = openai.Completion.create(
        model=params.model,
        prompt=params.search_term,
        max_tokens=1000,
        temperature=0
    )
    answers = []
    if res:
        for choice in res.choices:
            answers.append(choice.text)

    finding = Finding(
        title="ChatGPT Results",
        source=FindingSource.PROMETHEUS,
        aggregation_key="ChatGPT Wisdom",
    )

    finding.add_enrichment([MarkdownBlock(f"*{params.search_term}*")])
    if answers:
        finding.add_enrichment([ListBlock(answers)])
    else:
        finding.add_enrichment(
            [
                MarkdownBlock(
                    f'Sorry, ChatGPT doesn\'t know anything about "{params.search_term}"'
                )
            ]
        )
    event.add_finding(finding)


@action
def chat_gpt_enricher(alert: PrometheusKubernetesAlert, params: ChatGPTTokenParams):
    """
    Add a button to the alert - clicking it will ask chat gpt to help find a solution.
    """
    alert_name = alert.alert.labels.get("alertname", "")
    if not alert_name:
        return

    alert.add_enrichment(
        [
            CallbackBlock(
                {
                    f'Ask ChatGPT': CallbackChoice(
                        action=show_chat_gpt_search,
                        action_params=ChatGPTParams(
                            search_term=f"How to solve {alert_name} on Kubernetes?",
                            chat_gpt_token=params.chat_gpt_token,
    ),
                    )
                },
            )
        ]
    )
