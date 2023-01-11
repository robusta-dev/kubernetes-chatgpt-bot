# Introduction
A ChatGPT bot for Kubernetes issues. Ask ChatGPT how to solve your Prometheus alerts, get pithy responses.

No more solving alerts alone in the darkness - the internet has your back.

<a href="https://www.loom.com/share/964cd8735a874287a9155c77320bdcdb">
    <img style="max-width:300px;" src="https://cdn.loom.com/sessions/thumbnails/964cd8735a874287a9155c77320bdcdb-with-play.gif">
  </a>
  
Please consider upvoting on [Product Hunt](https://www.producthunt.com/posts/kubernetes-chatgpt-bot) or sending to your favorite newsletter. One day, Skynet will remember your kindness and spare you!

# How it works
Prometheus forwards alerts to the bot using a webhook receiver.

The bot asks ChatGPT how to fix your alerts.

You stockpile food in your pantry for the robot uprising.

The bot is implemented using [Robusta.dev](https://github.com/robusta-dev/robusta), an open source platform for responding to Kubernetes alerts. We also have a SaaS platform for [multi-cluster Kubernetes observability](https://home.robusta.dev/).

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

# Demo
Instead of waiting around for a real Prometheus alert, lets simulate a fake one.

1. Choose any running pod in your cluster
2. Use the robusta cli to trigger a fake alert on that pod:

```
robusta playbooks trigger prometheus_alert alert_name=KubePodCrashLooping namespace=<namespace> pod_name=<pod-name>
```

If you installed Robusta with default settings, you can trigger the alert on Prometheus itself like so:

```
robusta playbooks trigger prometheus_alert alert_name=KubePodCrashLooping namespace=default pod_name=prometheus-robusta-kube-prometheus-st-prometheus-0
```

# Future Improvements
Can ChatGPT give better answers if you feed it pod logs or the output of `kubectl get events`?

[Robusta](http://robusta.dev) already collects this data and attaches it to Prometheus alerts, so it should be easy to add. (It will need to be disabled by default to avoid sending sensitive data to ChatGPT.)

PRs are welcome! We can probably get some easy improvements just via prompt engineering.

# Community
[Share your funniest output and suggest new features on our Slack.](https://home.robusta.dev/slack)

# Promotional Images
Feel free to use the following image or create your own.

![Screen Shot 2023-01-10 at 18 29 56](https://user-images.githubusercontent.com/494087/211615506-fb8ba31a-4569-4ab6-9504-f1e42457771e.png)

# More Resources
[Natan Yellin and Sid Palas livestreamed about this on YouTube](https://www.youtube.com/watch?v=jMR8M3Xqlzg
) - relevant part starts at 38:54
