import os
import requests

discord_webhook_url = os.environ.get('DISCORD_WEBHOOK_URL') or None
discord_comment_username = os.environ.get('DISCORD_WEBHOOK_USERNAME') or 'FoundryVTT Server'
discord_error_admin_id = os.environ.get('DISCORD_ERROR_ADMIN_ID') or None
discord_notification_role_id = os.environ.get('DISCORD_NOTIFICATION_ROLE_ID') or None


def post_discord_message(message, notification_ping=False, admin_ping=False):
  if discord_webhook_url is None:
    return
  if notification_ping and discord_notification_role_id:
    message = f'<{discord_notification_role_id}> {message}'
  if admin_ping and discord_error_admin_id:
    message = f'<{discord_error_admin_id}> {message}'
  data = {
      "content": message,
      "username": discord_comment_username
  }
  requests.post(discord_webhook_url, json=data)