import json
import boto3
from http import HTTPStatus


def lambda_handler(event, context):
    """
    Lambda function fetches ssm parameter and returns as Lambda response
    """

    ssm_client = boto3.client('ssm', region_name='eu-west-1')
    param = ssm_client.get_parameter(Name='/param/text', WithDecryption=False)['Parameter']['Value']
    print(f'Received param: {param} from SSM')

    return {
        "statusCode": HTTPStatus.OK,
        "body": json.dumps({
            "message": param,
        }),
    }
