# Setting up a Local Consumer

Let's create a setup to receive events directly in your machine.

Open one terminal and run the following Docker container and keep it running, as the event will be shown in the logs:
```bash
docker run --rm -p 8080:8080 konnek/consumer
```

Open another terminal and use [ngrok](https://ngrok.com) to expose the Docker container to the Internet, so Konnek can reach you:
```bash
ngrok http 8080
```

Note down your ngrok HTTPS address (something like `https://xxxxxxxx.ngrok.io`) for the next step.

## Receive the Events!
Now that you have a local consumer, try receiving events from [AWS](getting-started/installing-konnek-for-aws.md) or [GCP](getting-started/installing-konnek-for-gcp.md).