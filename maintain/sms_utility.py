from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()
def send_sms_alert(task):
    account_sid = os.getenv('SMS_ACCOUNT_SSID_API_KEY')
    auth_token = os.getenv('SMS_ACCOUNT_AUTH_API_KEY')
    client = Client(account_sid, auth_token)
    
    message_body = f"Maintenance Alert: {task.machinery} requires attention. Task: {task.description}. Hours of Operation: {task.hours_of_operation}."
    
    message = client.messages.create(
        body=message_body,
        from_='+1234567890', 
        to='+0987654321'
    )
    
    return message.sid