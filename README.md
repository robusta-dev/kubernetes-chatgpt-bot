 ## 🚨This project will be depreciated and replaced by [HolmesGPT](https://github.com/robusta-dev/holmesgpt), our advanced Open Source DevOps assistant. With Holmes you can investigate incidents, triage issues, enrich alerts and much more. Check it out [https://github.com/robusta-dev/holmesgpt](https://github.com/robusta-dev/holmesgpt)**

# Introduction

A ChatGPT[^1] bot for Kubernetes issues. Ask the AI how to solve your Prometheus alerts, get pithy responses.

No more solving alerts alone in the darkness - the internet has your back.

<a href="https://www.loom.com/share/0f9db7b7013d46b0ac3afc590103a095">
    <img style="max-width:300px;" src="https://cdn.loom.com/sessions/thumbnails/0f9db7b7013d46b0ac3afc590103a095-1676152572154-with-play.gif">
  </a>
  
Please consider upvoting on [Product Hunt](https://www.producthunt.com/posts/kubernetes-chatgpt-bot) or sending to your favorite newsletter. One day, Skynet will remember your kindness and spare you!

# How it works
Prometheus forwards alerts to the bot using a webhook receiver.

The bot sends a query to OpenAI, asking it how to fix your alerts.

You stockpile food in your pantry for the robot uprising.

The bot is implemented using [Robusta.dev](https://github.com/robusta-dev/robusta), an open source platform for responding to Kubernetes alerts. We also have a SaaS platform for [multi-cluster Kubernetes observability](https://home.robusta.dev/).

# Prerequisites
* A Slack workspace

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

3. Add your [OpenAI API key](https://beta.openai.com/account/api-keys) to `generated_values.yaml`. Make sure you edit the existing `globalConfig` section, don't add a duplicate section.

```
globalConfig:
  chat_gpt_token: YOUR KEY GOES HERE
```

4. Do a Helm upgrade to apply the new values: `helm upgrade robusta robusta/robusta --values=generated_values.yaml --set clusterName=<YOUR_CLUSTER_NAME>`

5. [Send your Prometheus alerts to Robusta](https://docs.robusta.dev/master/user-guide/alert-manager.html). Alternatively, just use Robusta's bundled Prometheus stack.

# Demo
Instead of waiting around for a Prometheus alert, lets cause one.

1. Deploy a broken pod that will be stuck in pending state:

```
kubectl apply -f https://raw.githubusercontent.com/robusta-dev/kubernetes-demos/main/pending_pods/pending_pod_node_selector.yaml
```

2. Trigger a Prometheus alert immediately, skipping the normal delays:

```
robusta playbooks trigger prometheus_alert alert_name=KubePodCrashLooping namespace=default pod_name=example-pod
```

An alert will arrive in Slack with a button. Click the button to ask ChatGPT about the alert.

# Future Improvements
Can ChatGPT give better answers if you feed it pod logs or the output of `kubectl get events`?

[Robusta](http://robusta.dev) already collects this data and attaches it to Prometheus alerts, so it should be easy to add. 

PRs are welcome!

# Community
[Share your funniest output and suggest new features on our Slack.](https://home.robusta.dev/slack)

# Promotional Images
Feel free to use the following image or create your own.

![Screen Shot 2023-01-10 at 18 29 56](https://user-images.githubusercontent.com/494087/211615506-fb8ba31a-4569-4ab6-9504-f1e42457771e.png)

# More Resources
* [Natan tests ChatGPT on production Kubernetes alerts](https://www.youtube.com/watch?v=RVK6jb4Ssuo)
* [Natan Yellin and Sid Palas go over the code on YouTube](https://www.youtube.com/watch?v=jMR8M3Xqlzg
) - relevant part starts at 38:54

[^1]: Technically this project doesn't use ChatGPT. It uses the `text-davinci-003` model which is a [GPT3.5-based sibling of ChatGPT](https://matt-rickard.ghost.io/gpt-lineage/). Given that most people are familiar with ChatGPT, but not `text-davinci-003` or GPT3.5, we've decided to keep the name "ChatGPT bot" despite the technical inaccuracy.
