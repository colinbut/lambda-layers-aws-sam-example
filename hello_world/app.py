import json
import boto3
from http import HTTPStatus
from parameter_retriever import get_param


def lambda_handler(event, context):
    """
    Lambda function fetches ssm parameter and returns as Lambda response
    """

    return {
        "statusCode": HTTPStatus.OK,
        "body": json.dumps({
            "message": get_param("/param/text"),
        }),
    }
