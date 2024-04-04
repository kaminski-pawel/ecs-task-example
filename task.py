import boto3

STATICWS_WIP_BUCKET_NAME = "dgtmon-dev-staticws-wip"

def upload_to_s3(body, s3_bucket_name, s3_object_key):
    try:
        s3_client = boto3.client("s3")
        s3_client.put_object(
            Body=body.decode("utf-8"),
            Bucket=s3_bucket_name,
            Key=s3_object_key,
            ContentType="text/html",
        )
        # s3_client.upload_file(local_file_path, s3_bucket_name, s3_object_key)
    except Exception as e:
        print(f"Error uploading to S3: {e}")


if __name__ == "__main__":
    local_file_path = "/tmp/anita-thesis.txt"
    s3_bucket_name = STATICWS_WIP_BUCKET_NAME
    s3_object_key = "test.html"
    body = """<!DOCTYPE html><html>
<head>
  <title>The title</title>
</head>
<body>
<div>
  <h1>Test worked!</h1>
  <p>Finally, it worked!!!</p>
</div>
</body>
</html>"""
    upload_to_s3(body.encode("utf-8"), s3_bucket_name, s3_object_key)
