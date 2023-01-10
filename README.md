# Introduction
A ChatGPT bot for Kubernetes issues. Ask ChatGPT how to solve your Prometheus alerts, get pithy responses.

No more solving alerts alone in the darkness - the internet has your back.

# How it works
Prometheus forwards alerts to the bot using a webhook receiver.

The bot asks ChatGPT how to fix your alerts.

You stockpile food in your pantry for the robot uprising.

The bot is implemented using [Robusta.dev](https://github.com/robusta-dev/robusta), an open source platform for responding to Prometheus alerts and Kubernetes events.

# Prerequisites
* A Slack workspace (for Teams/Discord support, please open an issue)

# Setup
1. [Install Robusta with Helm](https://docs.robusta.dev/master/installation.html)
2. Load the ChatGPT playbook. Add the following to `generated_values.yaml`: 
```
playbookRepos:
  chatgpt_robusta_actions:
    url: "https://github.com/robusta-dev/kubernetes-chatgpt-bot.git"

customPlaybooks:
# Add the 'Ask ChatGPT' button to all Prometheus alerts
- triggers:
  - on_prometheus_alert: {}
  actions:
  - chat_gpt_enricher: {}
```

3. Add your [ChatGPT API key](https://beta.openai.com/account/api-keys) to `generated_values.yaml`. Make sure you edit the existing `globalConfig` section, don't add a duplicate section.

```
globalConfig:
  chat_gpt_token: YOUR KEY GOES HERE
```

4. Do a Helm upgrade to apply the new values: `helm upgrade robusta robusta/robusta --values=generated_values.yaml --set clusterName=<YOUR_CLUSTER_NAME>`

5. [Send your Prometheus alerts to Robusta](https://docs.robusta.dev/master/user-guide/alert-manager.html). Alternatively, just use Robusta's bundled Prometheus stack.
