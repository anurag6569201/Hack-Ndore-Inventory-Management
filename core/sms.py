from twilio.rest import Client
from dotenv import load_dotenv
import os
load_dotenv()


ACCOUNT_SID = os.getenv("SMS_ACCOUNT_SSID_API_KEY")
AUTH_TOKEN = os.getenv("SMS_ACCOUNT_AUTH_API_KEY")
FROM_PHONE = os.getenv("SMS_FROM_NUMBER")
TO_PHONE = '9098691543'

client = Client(ACCOUNT_SID, AUTH_TOKEN)
maintenance_data = {
    "Bulldozer": [
        (100, "Checked and adjusted track tension, lubricated all points - Track tension needed"),
        (300, "Replaced engine oil and filter, cleaned air filter - Air filter had significant dust."),
        (600, "Checked hydraulic system, inspected undercarriage - No significant wear observed")
    ],
    "Excavator": [
        (200, "Lubricated all grease points, checked hydraulic oil level - All in good condition."),
        (500, "Changed engine oil and filter, inspected hydraulic system - Hydraulic oil level low"),
        (1000, "Replaced hydraulic oil and filter, inspected tracks - Minor wear on tracks.")
    ],
    "Road Roller": [
        (150, "Checked vibratory system, lubricated all points - Vibratory system working well."),
        (400, "Replaced engine oil and filter, cleaned air filter - Air filter had moderate dust."),
        (800, "Checked hydraulic system, inspected drum - No significant wear observed.")
    ],
    "Waste Collection Car": [
        (300, "Checked and adjusted brakes, lubricated all points - Brakes needed minor adjustment."),
        (700, "Replaced engine oil and filter, inspected hydraulic system - Hydraulic system in good condition."),
        (1200, "Checked waste compactor, inspected tires - Tires needed rotation.")
    ]
}
