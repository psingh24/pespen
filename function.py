import sys
import boto3


def s3_upload(bucketname, filename) :
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket = bucketname)
    s3.upload_file(filename, bucketname, filename)

s3_upload(sys.argv[1],sys.argv[2])