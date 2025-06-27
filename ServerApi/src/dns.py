import os
import boto3

client = boto3.client('ecs')
route_client = boto3.client('route53')

hosted_zone_id = os.environ.get('HOSTED_ZONE_ID')
dns_name = os.environ.get('DNS_NAME')
service = os.environ.get('SERVICE')

def set_ip_to_dns(ip):
  print(f'Setting IP to {ip}')
  all_records = route_client.list_resource_record_sets(HostedZoneId=hosted_zone_id).get('ResourceRecordSets')
  server_record = [record for record in all_records if record['Name'] == f"{dns_name}."][0] or None # None isn't going to work because it modified that return
  server_record['ResourceRecords'] = [{'Value': ip}]
  return route_client.change_resource_record_sets(
    HostedZoneId=hosted_zone_id,
    ChangeBatch={
      'Changes': [{
        'Action': 'UPSERT',
        'ResourceRecordSet': server_record
      }]
    }
  )


def deregister_ip():
  print('Deregister IP - START')
  response = set_ip_to_dns('0.0.0.0')
  if response.get('ResponseMetadata', {}).get('HTTPStatusCode', 500) != 200:
    print('ERROR: Unable to set Route53 record', response.get('message'))
  client.untag_resource(resourceArn=service, tagKeys=['DNS'])
  print('Deregister IP - END')
