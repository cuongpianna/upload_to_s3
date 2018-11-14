from flask import Flask, request, jsonify
import boto3


class Config:
    SECRET_KEY = '421412412412'
    DEBUG = True
    PORT = 5000


app = Flask(__name__)
app.config.from_object(Config)

s3 = boto3.resource(
    "s3",
    aws_access_key_id='your key',
    aws_secret_access_key='your key'
)


def upload_file_to_s3(file, bucket_name, acl="public-read"):
    """
    Docs: http://boto3.readthedocs.io/en/latest/guide/s3.html
    """
    try:
        s3.upload_fileobj(
            Fileobj=file, Bucket=bucket_name, Key='AKIAITVNJVWUSOEHP3JA',
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )

    except Exception as e:
        print("Something Happened: ", e)
        return e

    return "{}{}".format(app.config["S3_LOCATION"], file.filename)


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    b = s3.Bucket('creatjvvdjdkk').put_object(Key=file.filename, Body=file, ACL='public-read')
    return 'ok'


if __name__ == '__main__':
    app.run()
