import boto3


def get_param(path: str):
    ssm_client = boto3.client('ssm', region_name='eu-west-1')
    param = ssm_client.get_parameter(Name='/param/text', WithDecryption=False)['Parameter']['Value']
    print(f'Received param: {param} from SSM')
    return param
