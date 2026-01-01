#!/usr/bin/env python3

import os
import logging
import boto3
import click
from botocore.exceptions import ClientError

def upload_file(file_path, bucket_name):
    s3 = boto3.client("s3")
    s3.upload_file(file_path, bucket_name, os.path.basename(file_path))
    return True

# -------------------------
# Logging Configuration
# -------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger(__name__)

# -------------------------
# CLI Command
# -------------------------
@click.command()
@click.argument("file_path")
@click.argument("bucket_name")

def cli(file_path, bucket_name):
    upload_file(file_path, bucket_name)
    click.echo(f"Uploaded {file_path} to {bucket_name}")

if __name__ == "__main__":
    cli()

def upload(file_path, bucket_name):
    """Upload a file to AWS S3"""

    logger.info("CLI invoked")

    # 1️⃣ Check file exists
    if not os.path.exists(file_path):
        logger.error(f"File not found: {file_path}")
        raise SystemExit(1)

    s3 = boto3.client("s3")

    try:
        logger.info(f"Starting upload: {file_path} → s3://{bucket_name}/{file_path}")

        s3.upload_file(
            Filename=file_path,
            Bucket=bucket_name,
            Key=os.path.basename(file_path)
        )

        logger.info("Upload completed successfully")

    except ClientError as e:
        logger.error("Upload failed due to AWS error")
        logger.error(e)
        raise SystemExit(1)

    except Exception as e:
        logger.exception("Unexpected error occurred")
        raise SystemExit(1)


if __name__ == "__main__":
    upload()

