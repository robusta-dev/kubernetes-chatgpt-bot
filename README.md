# Introduction
A ChatGPT bot for Kubernetes issues and Prometheus alerts.

No more solving alerts alone in the darkness - the internet has your back.

# How it works
Prometheus forwards alerts to the bot using a webhook receiver.

The bot is implemented using [Robusta.dev](https://github.com/robusta-dev/robusta), an open source platform for responding to Prometheus alerts and Kubernetes events.

# Prerequisites
* A Slack workspace (for Teams/Discord support, please open an issue)
* A [ChatGPT API key](https://beta.openai.com/account/api-keys)

# Setup
1. [Install Robusta with Helm](https://docs.robusta.dev/master/installation.html)
2. Configure the ChatGPT playbook. Add the following to Robusta's `generated_values.yaml` file: 
```
playbookRepos:
  chatgpt_robusta_actions:
    url: "https://github.com/robusta-dev/kubernetes-chatgpt-bot.git"

globalConfig:
  chat_gpt_token: YOUR KEY GOES HERE


customPlaybooks:
# Add the 'Ask ChatGPT' button to all Prometheus alerts
- triggers:
  - on_prometheus_alert: {}
  actions:
  - chat_gpt_enricher: {}
```
3. [Send your Prometheus alerts to Robusta](https://docs.robusta.dev/master/user-guide/alert-manager.html). Alternatively, just use Robusta's bundled Prometheus stack.
