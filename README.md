# Introduction
ChatGPT bot for Kubernetes issues using [Robusta](https://github.com/robusta-dev/robusta)

# What does it do?
Allow getting ChatGPT insights on Prometheus alerts fired on your Kubernetes cluster

# Prerequisites
Use Robusta to enrich and publish your Prometheus alerts
Use Robusta's Slack integration (Currently this works only with Slack)


# How to use?
1. Install Robusta [90 seconds installation](https://docs.robusta.dev/master/installation.html)
2. Get your ChatGPT api key [ChatGPT API key](https://beta.openai.com/account/api-keys)
3. Add this actions repo to Robusta
To your `generated_values.yaml` file add: 
```
playbookRepos:
  chatgpt_robusta_actions:
    url: "https://github.com/robusta-dev/kubernetes-chatgpt-bot.git"
```

4. Add the api key and custom playbooks to your `generated_values.yaml`: 
```
globalConfig:
  chat_gpt_token: YOUR KEY GOES HERE


customPlaybooks:
# Add 'Ask ChatGPT' button to all Prometheus alerts notifications
- triggers:
  - on_prometheus_alert: {}
  actions:
  - chat_gpt_enricher: {}
```
