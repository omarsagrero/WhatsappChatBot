from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from createMenu import *
from readDatabase import *
from messagesAPI import *
load_dotenv()

app = Flask(__name__)

WEBHOOK_VERIFY_TOKEN = os.getenv('WEBHOOK_VERIFY_TOKEN')
GRAPH_API_TOKEN = os.getenv('GRAPH_API_TOKEN')
PORT = os.getenv('PORT', 5000) # Usa 5000 como valor por defecto si PORT no esta definido.
GRAPH_API_VERSION = "v22.0"
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

allowed_senders = ["524426235079"]
global_users = []
user = {}
debug = True
webhook_counter = 0 



def check_user(phone_number):
    for user in global_users:    
        if phone_number in user:
            return True
        else:
            return False


@app.route('/webhook', methods=['POST'])
def webhook_post():
    
    data = request.get_json()

    if debug:
        print(f"\n\n\n\nIncoming webhook message: {data}")

    if data:
        messages = data.get('entry', [{}])[0].get('changes', [{}])[0].get('value', {}).get('messages', [])
        
        if messages:
            
            
            if debug:
                print("Esto es un message: ", messages)

            message = messages[0]

            if message.get('type') == 'text' or message.get('type') == 'image' or message.get('type') == 'location':

                business_phone_number_id = data.get('entry', [{}])[0].get('changes', [{}])[0].get('value', {}).get('metadata', {}).get('phone_number_id')
                message_text = message.get('text', {}).get('body')
                from_number = message.get('from')
                edited_number = from_number[:2] + from_number[3:]

                if debug:
                    print("edited_number: ", edited_number)
                    print("Message received from:", edited_number)
                    print("Message text:", message_text)
                    print("global_users: ", global_users)
                
                mark_as_read(GRAPH_API_VERSION, GRAPH_API_TOKEN, business_phone_number_id, message.get('id'))

                if not check_user(edited_number) and edited_number in allowed_senders:
                    if debug:
                        print("New user")
                    newuser = {}
                    newuser[edited_number] = {'fase': "1", 'message': [message_text]}
                    global_users.append(newuser)
                    send_message(GRAPH_API_VERSION, GRAPH_API_TOKEN, business_phone_number_id, edited_number, phase1())

                elif (check_user(edited_number)):
                    for user in global_users:
                        if edited_number in user:

                            if debug:
                                print("User already exists\n Phase: ", user[edited_number]['fase'])
                            
                            if user[edited_number]['fase'] == "1":
                                if message_text == "1":
                                    user[edited_number]['fase'] = "2A"
                                    user[edited_number]['message'].append(message_text)
                                    send_message(GRAPH_API_VERSION, GRAPH_API_TOKEN, business_phone_number_id, edited_number, phase2A())
                                else:
                                    send_message(GRAPH_API_VERSION, GRAPH_API_TOKEN, business_phone_number_id, edited_number, "Opción no válida, por favor selecciona una opción válida.")
                            
                            elif user[edited_number]['fase'] == "2A":
                                inventario = read_database(DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD, "weed")
                                if message_text == "1":
                                    user[edited_number]['fase'] = "2A1"
                                    user[edited_number]['message'].append(message_text)
                                    send_message(GRAPH_API_VERSION, GRAPH_API_TOKEN, business_phone_number_id, edited_number, phase2A1(inventario))
                                elif message_text == "2":
                                    user[edited_number]['fase'] = "2A2"
                                    user[edited_number]['message'].append(message_text)
                                    send_message(GRAPH_API_VERSION, GRAPH_API_TOKEN, business_phone_number_id, edited_number, phase2A2(inventario))
                                elif message_text == "3":
                                    user[edited_number]['fase'] = "2A3"
                                    user[edited_number]['message'].append(message_text)
                                    send_message(GRAPH_API_VERSION, GRAPH_API_TOKEN, business_phone_number_id, edited_number, phase2A3(inventario))
                                elif message_text == "4":
                                    user[edited_number]['fase'] = "1"
                                    user[edited_number]['message'].append(message_text)
                                    send_message(GRAPH_API_VERSION, GRAPH_API_TOKEN, business_phone_number_id, edited_number, phase1())
                                else:
                                    send_message(GRAPH_API_VERSION, GRAPH_API_TOKEN, business_phone_number_id, edited_number, "Opción no válida, por favor selecciona una opción válida.")
                            
                            elif user[edited_number]['fase'] == "2A1":
                                if message_text == "1":
                                    user[edited_number]['fase'] = "3"
                                    user[edited_number]['message'].append(message_text)
                                    send_message(GRAPH_API_VERSION, GRAPH_API_TOKEN, business_phone_number_id, edited_number, phase3())
                                if message_text == "2":
                                    user[edited_number]['fase'] = "3"
                                    user[edited_number]['message'].append(message_text)
                                    send_message(GRAPH_API_VERSION, GRAPH_API_TOKEN, business_phone_number_id, edited_number, phase3())
                                if message_text == "3":
                                    user[edited_number]['fase'] = "3"
                                    user[edited_number]['message'].append(message_text)
                                    send_message(GRAPH_API_VERSION, GRAPH_API_TOKEN, business_phone_number_id, edited_number, phase3())
                                if message_text == "4":
                                    user[edited_number]['fase'] = "2A"
                                    user[edited_number]['message'].append(message_text)
                                    send_message(GRAPH_API_VERSION, GRAPH_API_TOKEN, business_phone_number_id, edited_number, phase2A())
                                if message_text not in ["1", "2", "3", "4"]:
                                    send_message(GRAPH_API_VERSION, GRAPH_API_TOKEN, business_phone_number_id, edited_number, "Opción no válida, por favor selecciona una opción válida.")
                            
                            elif user[edited_number]['fase'] == "2A2":
                                if message_text == "1":
                                    user[edited_number]['fase'] = "3"
                                    user[edited_number]['message'].append(message_text)
                                    send_message(GRAPH_API_VERSION, GRAPH_API_TOKEN, business_phone_number_id, edited_number, phase3())
                                if message_text == "2":
                                    user[edited_number]['fase'] = "3"
                                    user[edited_number]['message'].append(message_text)
                                    send_message(GRAPH_API_VERSION, GRAPH_API_TOKEN, business_phone_number_id, edited_number, phase3())
                                if message_text == "3":
                                    user[edited_number]['fase'] = "3"
                                    user[edited_number]['message'].append(message_text)
                                    send_message(GRAPH_API_VERSION, GRAPH_API_TOKEN, business_phone_number_id, edited_number, phase3())
                                if message_text == "4":
                                    user[edited_number]['fase'] = "2A"
                                    user[edited_number]['message'].append(message_text)
                                    send_message(GRAPH_API_VERSION, GRAPH_API_TOKEN, business_phone_number_id, edited_number, phase2A())
                                if message_text not in ["1", "2", "3", "4"]:
                                    send_message(GRAPH_API_VERSION, GRAPH_API_TOKEN, business_phone_number_id, edited_number, "Opción no válida, por favor selecciona una opción válida.")
                            
                            elif user[edited_number]['fase'] == "2A3":
                                
                                if message_text == "1":
                                    user[edited_number]['fase'] = "3"
                                    user[edited_number]['message'].append(message_text)
                                    send_message(GRAPH_API_VERSION, GRAPH_API_TOKEN, business_phone_number_id, edited_number, phase3())
                                elif message_text == "2":
                                    user[edited_number]['fase'] = "3"
                                    user[edited_number]['message'].append(message_text)
                                    send_message(GRAPH_API_VERSION, GRAPH_API_TOKEN, business_phone_number_id, edited_number, phase3())
                                elif message_text == "3":
                                    user[edited_number]['fase'] = "3"
                                    user[edited_number]['message'].append(message_text)
                                    send_message(GRAPH_API_VERSION, GRAPH_API_TOKEN, business_phone_number_id, edited_number, phase3())
                                elif message_text == "4":
                                    user[edited_number]['fase'] = "2A"
                                    user[edited_number]['message'].append(message_text)
                                    send_message(GRAPH_API_VERSION, GRAPH_API_TOKEN, business_phone_number_id, edited_number, phase2A())
                                else:
                                    send_message(GRAPH_API_VERSION, GRAPH_API_TOKEN, business_phone_number_id, edited_number, "Opción no válida, por favor selecciona una opción válida.")
                            
                            elif user[edited_number]['fase'] == "3":
                                user[edited_number]['fase'] = "4"
                                user[edited_number]['message'].append(message_text)
                                askLocation(GRAPH_API_VERSION, GRAPH_API_TOKEN, business_phone_number_id, edited_number, phase4())
                            
                            elif user[edited_number]['fase'] == "4":
                                if message.get('type') == 'location':
                                    user[edited_number]['fase'] = "5"
                                    send_message(GRAPH_API_VERSION, GRAPH_API_TOKEN, business_phone_number_id, edited_number, phase5())
                                user[edited_number]['message'].append(message_text)
                            
                            elif user[edited_number]['fase'] == "5":
                                user[edited_number]['fase'] = "1"
                                user[edited_number]['message'].append(message_text)
                                send_message(GRAPH_API_VERSION, GRAPH_API_TOKEN, business_phone_number_id, edited_number, phase1())
                
                else:
                    send_message(GRAPH_API_VERSION, GRAPH_API_TOKEN, business_phone_number_id, edited_number, "Lo siento, no tienes permiso para usar este servicio.")
                    
    return jsonify({"status": "success"}), 200


@app.route('/webhook', methods=['GET'])
def webhook_get():
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')

    if mode == 'subscribe' and token == WEBHOOK_VERIFY_TOKEN:
        print('Webhook verified successfully!')
        return challenge, 200
    else:
        return '403 Forbidden', 403


@app.route('/', methods=['GET'])
def index():
    return '<pre>Nothing to see here.\nCheckout README.md to start.</pre>', 200


if __name__ == '__main__':
    app.run(port=PORT)