import os
import boto3

client = boto3.client('ecs')
scheduler_client = boto3.client('scheduler')

def update_service_desired_count(desired_count):
  client.update_service(
    cluster=os.environ.get('CLUSTER') or 'FoundryVTT-ServerCluster',
    service=os.environ.get('SERVICE') or 'FoundryVTT',
    desiredCount=desired_count
  )


def cron_job_state(enabled):
  response = scheduler_client.get_schedule(
      Name='FoundryVTT-Server-Monitor-Schedule'
  )
  response['State'] = "ENABLED" if enabled else "DISABLED"
  response.pop('Arn', None)
  response.pop('CreationDate', None)
  response.pop('LastModificationDate', None)
  response.pop('ResponseMetadata', None)
  scheduler_client.update_schedule(**response)