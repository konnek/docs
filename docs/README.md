# Konnek
Konnek retrieves events from cloud platforms – like AWS and GCP –, transform them into CloudEvents and send to whenever you want.

Try it out now by [receiving events in your own local machine](getting-started/setting-up-local-consumer.md).

## How does it work?
Konnek is a very simple piece of software and infrastructure, it generally works by:
- Deploying a FaaS to a cloud provider, e.g. Lambda
- Subscribing the FaaS to an event source, e.g. SQS
- Setting up the `KONNEK_CONSUMER` environment variable to the address you would like to receive the events
- Profit!

_[Logo by Openmoji](https://openmoji.org/library/#emoji=23E9)_