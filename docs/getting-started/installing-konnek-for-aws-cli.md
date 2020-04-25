# Konnek AWS - CLI

Make sure you have the AWS CLI [installed](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) and the AWS credentials [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html).

Get Konnek latest version:
```bash
wget https://github.com/konnek/konnek-aws/releases/download/v0.0.2/konnek-aws-0.0.2.zip -O konnek.zip
```

Get a basic AWS Role template for the Lambda:
```bash
wget https://raw.githubusercontent.com/konnek/konnek-aws/master/config/aws-basic-role.json
```

Create a basic AWS Lambda Role. Note down the `Role.Arn` output, we will use in a bit:
```bash
aws iam create-role --role-name konnek-lambda-role --assume-role-policy-document file://aws-basic-role.json
```

Give it the `AWSLambdaBasicExecutionRole` policy:
```bash
aws iam attach-role-policy --role-name konnek-lambda-role --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
```

Deploy the function. Change in the following command:
- Add the `Role.Arn` in the `<id>` field on the `--role` option
- Add the CloudEvents server address to the `KONNEK_CONSUMER` environment variable (if you setup the local consumer, use the ngrok address!)
```bash
aws lambda create-function \ 
    --function-name konnek \ 
    --runtime go1.x \ 
    --zip-file fileb://konnek.zip \ 
    --environment "Variables={KONNEK_CONSUMER=<your-ngrok-address>}" \ 
    --handler main \ 
    --role arn:aws:iam::<id>:role/konnek-lambda-role
```

To test, get a SQS mock data file:
```bash
wget https://raw.githubusercontent.com/konnek/konnek-aws/master/testdata/sqs.json
```

And invoke the function:
```bash
aws lambda invoke --function-name konnek --payload fileb://sqs.json out.txt
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