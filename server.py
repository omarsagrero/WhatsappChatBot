from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from createMenu import *
from manageDatabase import *
from messagesAPI import *
from utilities import *
from backMenu import *
load_dotenv()

app = Flask(__name__)

WEBHOOK_VERIFY_TOKEN = os.getenv('WEBHOOK_VERIFY_TOKEN')
GRAPH_API_TOKEN = os.getenv('GRAPH_API_TOKEN')
PORT = os.getenv('PORT')
GRAPH_API_VERSION = "v22.0"
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
debug = False

@app.route('/webhook', methods=['POST'])
def webhook_post():
    data = request.get_json()
    if debug:
        print(f"\n\n\n\nIncoming webhook message: {data}")

    if data:
        messages = data.get('entry', [{}])[0]. \
                        get('changes', [{}])[0]. \
                        get('value', {}). \
                        get('messages', [])
          
        business_phone_number_id = data.get('entry', [{}])[0]. \
                                        get('changes', [{}])[0]. \
                                        get('value', {}). \
                                        get('metadata', {}). \
                                        get('phone_number_id')      
        if messages:
            if debug:
                print("Esto es un message: ", messages)
            message = messages[0]
            edited_number = message.get('from')[:2] + message.get('from')[3:]
            allowed_user = read_database(DB_HOST, 
                                         DB_PORT, 
                                         DB_NAME, 
                                         DB_USER, 
                                         DB_PASSWORD, 
                                         "usersadm")
 
            if accessGrant(allowed_user, edited_number):
                message_text = getMessage(message)
                user = getData(allowed_user, edited_number)

                inventario = read_database( DB_HOST, 
                                            DB_PORT, 
                                            DB_NAME, 
                                            DB_USER, 
                                            DB_PASSWORD, 
                                            "weed")
                
                user = selectMenuOption(GRAPH_API_VERSION,
                                 GRAPH_API_TOKEN,
                                 inventario,
                                 user,
                                 message_text,
                                 edited_number,
                                 business_phone_number_id,)

                update_database(DB_HOST,
                                DB_PORT,
                                DB_NAME,
                                DB_USER,
                                DB_PASSWORD,
                                "usersadm",
                                user)
                
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