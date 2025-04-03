import requests

def send_message(api_version, api_token, business_phone_number_id, recipient, message):
    try:
        response = requests.post(
            f"https://graph.facebook.com/{api_version}/{business_phone_number_id}/messages",
            headers={'Authorization': f'Bearer {api_token}', 'Content-Type': 'application/json'},
            json={
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": f'+{recipient}',
                "type": "text",
                "text": {"body": message}
            }
        )
        response.raise_for_status()
        print("Message sent successfully.")
    except requests.exceptions.RequestException as e:
        print("Error sending message:", e)
        if response is not None:
            print("Response Content: ", response.content)


def mark_as_read(api_version, api_token, business_phone_number_id, message_id):
    try:
        response = requests.post(
            f"https://graph.facebook.com/{api_version}/{business_phone_number_id}/messages",
            headers={'Authorization': f'Bearer {api_token}', 'Content-Type': 'application/json'},
            json={
                "messaging_product": "whatsapp",
                "status": "read",
                "message_id": message_id
            }
        )
        response.raise_for_status()
        print("Message marked as read successfully.")
    except requests.exceptions.RequestException as e:
        print("Error sending message:", e)
        if response is not None:
            print("Response Content: ", response.content)   


def askLocation (api_version, api_token, business_phone_number_id, recipient, message):
    try:
        response = requests.post(
            f"https://graph.facebook.com/{api_version}/{business_phone_number_id}/messages",
            headers={'Authorization': f'Bearer {api_token}', 'Content-Type': 'application/json'},
            json={
                    "messaging_product": "whatsapp",
                    "recipient_type": "individual",
                    "to": recipient,
                    "type": "interactive",
                    "interactive": {
                        "type": "location_request_message",
                        "body": {
                            "text": message},
                        "action": {
                            "name": "send_location",}}}
        )
        response.raise_for_status()
        print("Location request sent successfully.")
    except requests.exceptions.RequestException as e:
        print("Error sending message:", e)
        if response is not None:
            print("Response Content: ", response.content)
