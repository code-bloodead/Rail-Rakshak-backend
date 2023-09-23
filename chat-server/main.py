import os
from dotenv import load_dotenv
from pyngrok import ngrok, conf
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from utils import generate_alphanumeric_id, contains_initiating_strings, is_report_incident_input, is_helpdesk_input, is_conclusive

load_dotenv()

PORT = os.getenv('FLASK_RUN_PORT') or 5002
NGROK_AUTHTOKEN = os.getenv('NGROK_AUTHTOKEN')
NGROK_DOMAIN = os.environ.get('NGROK_DOMAIN')

app = Flask(__name__)
ngrok.set_auth_token(NGROK_AUTHTOKEN)
tunnel_url = ngrok.connect(
    PORT, bind_tls=True, hostname=NGROK_DOMAIN).public_url

print(f"Ingress established at {tunnel_url}")


@app.route("/whatsapp", methods=["GET", "POST"])
def reply_whatsapp():
    print(request.values)
    request.values.get("Body")
    incoming_message_body = request.values.get("Body")
    incoming_message = (incoming_message_body or "").strip().lower()
    # num_media = int(request.values.get("NumMedia"))
    print("Incoming message: ", incoming_message)

    response = MessagingResponse()

    if contains_initiating_strings(incoming_message):
        msg = response.message(
            "Welcome to Rail Rakshak !\nHow can we assist you today?\nPlease choose an option:\n1. Report an incident\n2. Helpdesk")
    elif incoming_message == "1" or is_report_incident_input(incoming_message):
        msg = response.message(
            "Sure, please describe your incident, You can also add relevant media")
    elif incoming_message == "2" or is_helpdesk_input(incoming_message):
        msg = response.message(
            "Here are the helpline phone numbers:\nRailway Police: 1800 1113 22 \nVigilance Helpline: 0111 552 10")
    elif is_conclusive(incoming_message):
        msg = response.message("If you need further assistance, feel free to reach out anytime.\nBye 👋")
    else:
        incident_id = generate_alphanumeric_id()
        msg = response.message(
            f"Thank you for reporting the incident !\nReference ID: {incident_id}")

    print("Formatted xml reply: \n", msg)
    return str(response)


@app.route("/ping", methods=["GET", "POST"])
def ping():
    return f"GG !!"


if __name__ == "__main__":
    app.run()

# def reply_whatsapp_with_media():
#     GOOD_BOY_URL = (
#         "https://images.unsplash.com/photo-1518717758536-85ae29035b6d?ixlib=rb-1.2.1"
#         "&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"
#     )
#     try:
#         num_media = int(request.values.get("NumMedia"))
#     except (ValueError, TypeError):
#         return "Invalid request: invalid or missing NumMedia parameter", 400
#     response = MessagingResponse()
#     if not num_media:
#         msg = response.message("Send us an image!")
#     else:
#         msg = response.message("Thanks for the image. Here's one for you!")
#         msg.media(GOOD_BOY_URL)
#     return str(response)
