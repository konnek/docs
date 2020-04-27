# Konnek AWS - Serverless Framework

Make sure you have the Serverless Framework [installed](https://serverless.com/framework/docs/getting-started/) and the AWS credentials [configured](https://serverless.com/framework/docs/providers/aws/cli-reference/config-credentials/).

First, get the latest Konnek version:
```bash
wget https://github.com/konnek/konnek-aws/releases/download/v0.0.3/konnek-aws-v0.0.3.zip -O konnek.zip
```

Get the official Konnek `serverless.yml` file: 
```bash
wget https://raw.githubusercontent.com/konnek/konnek-aws/master/config/serverless-framework/serverless.yml
```

Set the `KONNEK_CONSUMER` environment variable to the CloudEvents server address that will consume the event. If you setup a [_local consumer_](/getting-started/setting-up-local-consumer.md), this is the ngrok address!
```bash
KONNEK_CONSUMER="https://xxxxxxxx.ngrok.io" serverless deploy
```

Get a SQS mock data file:
```bash
wget https://raw.githubusercontent.com/konnek/konnek-aws/master/testdata/sqs.json
```

Finally, test it:
```bash
serverless invoke -f konnek -p sqs.json
```

Look in your Docker terminal, you should see something like:
```bash
Context Attributes,
  specversion: 1.0
  type: com.amazon.sqs
  source: arn:aws:sqs:eu-central-1:123456789012:MyQueue
  id: cfbb5e8d-f025-4a9c-9b7a-55d10a4b42e2
  time: 2020-04-23T16:56:44.066357394Z
  datacontenttype: application/json
Extensions,
  traceparent: 00-a0b1fe0032d5ad22af09319d51271ded-916075d55bd96bfe-00
Data,
  {
    "Records": [
      {
        "attributes": {
          "ApproximateFirstReceiveTimestamp": "1523232000001",
          "ApproximateReceiveCount": "1",
          "SenderId": "123456789012",
          "SentTimestamp": "1523232000000"
        },
        "awsRegion": "eu-central-1",
        "body": "Hello from SQS!",
        "eventSource": "aws:sqs",
        "eventSourceARN": "arn:aws:sqs:eu-central-1:123456789012:MyQueue",
        "md5OfBody": "7b270e59b47ff90a553787216d55d91d",
        "messageAttributes": {},
        "messageId": "19dd0b57-b21e-4ac1-bd88-01bbb068cb78",
        "receiptHandle": "MessageReceiptHandle"
      }
    ]
  }
```

That's your event!