import boto3
import datetime
import traceback
import logging

logger = logging.getLogger(__name__)


def run():
    try:

        filename = f'squad_tagged_data_01_15_20.csv'

        s3 = boto3.resource('s3')
        s3.Bucket('squad-go').download_file(filename, '/tmp/squad_test.csv')

    except Exception as e:
        logger.error(f'{e}\t{traceback.format_exc()}'
