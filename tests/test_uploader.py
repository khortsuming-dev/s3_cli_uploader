import boto3
import os
from moto import mock_aws
from uploader.s3_uploader import upload_file

@mock_aws
def test_upload_file_success(tmp_path):
    # Arrange
    s3 = boto3.client("s3", region_name="us-east-1")
    bucket_name = "test-bucket"
    s3.create_bucket(Bucket=bucket_name)

    test_file = tmp_path / "test.txt"
    test_file.write_text("hello devops")

    # Act
    result = upload_file(str(test_file), bucket_name)

    # Assert
    assert result is True
    response = s3.list_objects_v2(Bucket=bucket_name)
    assert response["KeyCount"] == 1

