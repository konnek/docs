# Konnek GCP - CLI

Make sure you have the gcloud CLI [installed](https://cloud.google.com/sdk/install) and [configured](https://cloud.google.com/sdk/docs/initializing).

Setup some environment variables.
`KONNEK_CONSUMER` is the address of CloudEvents server address that will consume the event. If you setup a [_local consumer_](/getting-started/setting-up-local-consumer.md), this is the ngrok address!
```bash
export KONNEK_CONSUMER="https:/xxxxxxx.ngrok.io"
export KONNEK_VERSION="v0.0.4"
```

Deploy the latest version of Konnek:
```
gcloud functions deploy konnek \ 
  --runtime go111 \ 
  --entry-point Handler \ 
  --set-env-vars KONNEK_CONSUMER=$KONNEK_CONSUMER \ 
  --allow-unauthenticated \ 
  --source gs://konnek-gcp/konnek-gcp-$KONNEK_VERSION.zip \

  # and define your trigger
  --trigger-bucket <bucket-name>
```

See other available triggers with `gcloud functions deploy --help` and look for the `--trigger-*` options.

## Testing
To test locally, make sure the [local consumer](/getting-started/setting-up-local-consumer.md) is up and running.

Get a Storage mock data file:
```bash
wget https://raw.githubusercontent.com/konnek/konnek-gcp/master/testdata/storage.json
```

And invoke the function:
```bash
gcloud functions call konnek --data "$(cat storage.json)"
```

Look in your Docker terminal, you should see something like:
```bash
2020/04/27 15:16:43 Validation: valid
Context Attributes,
  specversion: 1.0
  type: google.storage.object.finalize
  source: projects/_/buckets/konnek-test
  id: 1645410183
  time: 2020-04-27T15:16:42.703311041Z
  datacontenttype: application/json
Extensions,
  traceparent: 00-4272eb2694803b400e30b2675343cd0a-661f836129c697b2-00
Data,
  {
    "bucket": "konnek-test",
    "contentType": "application/octet-stream",
    "crc32c": "exmple==",
    "etag": "etag",
    "generation": "1588000397832026",
    "id": "konnek-test/file/1588000397832026",
    "kind": "storage#object",
    "md5Hash": "hash==",
    "mediaLink": "https://www.googleapis.com/download/storage/v1/b/konnek-test/o/file?generation=1588000397832026\u0026alt=media",
    "metageneration": "1",
    "name": "main.go",
    "selfLink": "https://www.googleapis.com/storage/v1/b/konnek-test/o/file",
    "size": "1211",
    "storageClass": "STANDARD",
    "timeCreated": "2020-04-27T15:13:17.831Z",
    "timeStorageClassUpdated": "2020-04-27T15:13:17.831Z",
    "updated": "2020-04-27T15:13:17.831Z"
  }
```

That's your event!