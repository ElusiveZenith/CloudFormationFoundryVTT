from server import cron_job_state, update_service_desired_count
from discord import post_discord_message
from dns import deregister_ip


def start_server():
  print("Starting Server")
  try:
    cron_job_state(True)
  except Exception as e:
    post_discord_message("Unable to start server. Failed to start server manager.", admin_ping=True)
    raise e
  # TODO: Set world to load on start
  update_service_desired_count(1)
  post_discord_message("Launching Server", notification_ping=True)
  return 200, "Server Launch Initiated"


def stop_server():
  print("Stopping Server")
  try:
    update_service_desired_count(0)
  except Exception as e:
    post_discord_message("Unable to stop server. Failed to set desired count.", admin_ping=True)
    raise e
  deregister_ip()
  try:
    cron_job_state(False)
  except Exception as e:
    post_discord_message("Failed to stop server manager.", admin_ping=True)
    print("Failed to stop server manager", e)
  post_discord_message("Server Stopped", notification_ping=False)
  return 200, "Server Stop Initiated"


def routing(path):
  match path:
    case "/start":
      return start_server()
    case "/stop":
      return stop_server()
    case "/health":
      return 200, "API Running"


def lambda_handler(event, context):
  status_code, message = routing(event['path'])
  return {
      "statusCode": status_code,
      "headers": {
          "Content-Type": "*/*"
      },
      "body": message
  }
