from messagesAPI import *
from createMenu import *
from readDatabase import *

def selectMenuOption(GRAPH_API_VERSION, 
                     GRAPH_API_TOKEN, 
                     inventario, 
                     user, 
                     message, 
                     edited_number, 
                     business_phone_number_id):
    
    if user['fase'] == "1":
        if message['text'] == "1":
            user['fase'] = "2A"
            send_message(GRAPH_API_VERSION,
                        GRAPH_API_TOKEN,
                        business_phone_number_id,
                        edited_number,
                        phase2())
        elif message['text'] == "2":
            user['fase'] = "2B"
            send_message(GRAPH_API_VERSION,
                        GRAPH_API_TOKEN,
                        business_phone_number_id,
                        edited_number,
                        phase2())
        elif message['text'] == "3":
            user['fase'] = "2C"
            send_message(GRAPH_API_VERSION,
                        GRAPH_API_TOKEN,
                        business_phone_number_id,
                        edited_number,
                        phase2())
        else:
            send_message(GRAPH_API_VERSION,
                        GRAPH_API_TOKEN,
                        business_phone_number_id,
                        edited_number,
                        "Opción no válida, por favor selecciona una opción válida.")

    elif user[edited_number]['fase'] == "2A":

        
        if message['text'] == "1":
            user['fase'] = "2A1"
            send_message(GRAPH_API_VERSION,
                        GRAPH_API_TOKEN,
                        business_phone_number_id,
                        edited_number,
                        phase2A1(inventario))
            
        elif message['text'] == "2":
            user['fase'] = "2A2"
            send_message(GRAPH_API_VERSION,
                        GRAPH_API_TOKEN,
                        business_phone_number_id,
                        edited_number,
                        phase2A2(inventario))
            
        elif message['text'] == "3":
            user['fase'] = "2A3"
            send_message(GRAPH_API_VERSION,
                         GRAPH_API_TOKEN,
                         business_phone_number_id,
                         edited_number,
                         phase2A3(inventario))
            
        elif message['text'] == "4":
            user['fase'] = "1"
            send_message(GRAPH_API_VERSION,
                         GRAPH_API_TOKEN,
                         business_phone_number_id,
                         edited_number,
                         phase1())
            
        else:
            send_message(GRAPH_API_VERSION,
                         GRAPH_API_TOKEN,
                         business_phone_number_id,
                         edited_number,
                         "Opción no válida, por favor selecciona una opción válida.")

    elif user[edited_number]['fase'] == "2A1":
        if message['text'] == "1":
            user['fase'] = "3"
            send_message(GRAPH_API_VERSION,
                         GRAPH_API_TOKEN,
                         business_phone_number_id,
                         edited_number,
                         phase3())
            
        elif message['text'] == "2":
            user['fase'] = "3"
            send_message(GRAPH_API_VERSION, 
                         GRAPH_API_TOKEN, 
                         business_phone_number_id, 
                         edited_number, 
                         phase3())
            
        elif message['text'] == "3":
            user['fase'] = "3"
            send_message(GRAPH_API_VERSION,
                         GRAPH_API_TOKEN, 
                         business_phone_number_id,
                         edited_number,
                         phase3())
            
        elif message['text'] == "4":
            user['fase'] = "2A"
            send_message(GRAPH_API_VERSION, 
                         GRAPH_API_TOKEN, 
                         business_phone_number_id, 
                         edited_number, 
                         phase2())
        else:
            send_message(GRAPH_API_VERSION,
                         GRAPH_API_TOKEN, 
                         business_phone_number_id, 
                         edited_number, 
                         "Opción no válida, por favor selecciona una opción válida.")

    elif user[edited_number]['fase'] == "2A2":
        if message['text'] == "1":
            user['fase'] = "3"
            send_message(GRAPH_API_VERSION, 
                         GRAPH_API_TOKEN, 
                         business_phone_number_id, 
                         edited_number, 
                         phase3())
            
        elif message['text'] == "2":
            user['fase'] = "3"
            send_message(GRAPH_API_VERSION,
                         GRAPH_API_TOKEN, 
                         business_phone_number_id, 
                         edited_number, 
                         phase3())
            
        elif message['text'] == "3":
            user['fase'] = "3"
            send_message(GRAPH_API_VERSION, 
                         GRAPH_API_TOKEN, 
                         business_phone_number_id, 
                         edited_number, 
                         phase3())
            
        elif message['text'] == "4":
            user['fase'] = "2A"
            send_message(GRAPH_API_VERSION,
                         GRAPH_API_TOKEN, 
                         business_phone_number_id, 
                         edited_number, 
                         phase2())
            
        else:
            send_message(GRAPH_API_VERSION,
                         GRAPH_API_TOKEN, 
                         business_phone_number_id, 
                         edited_number, 
                         "Opción no válida, por favor selecciona una opción válida.")

    elif user[edited_number]['fase'] == "2A3":
        
        if message['text'] == "1":
            user['fase'] = "3"
            send_message(GRAPH_API_VERSION, 
                         GRAPH_API_TOKEN, 
                         business_phone_number_id, 
                         edited_number, 
                         phase3())
            
        elif message['text'] == "2":
            user['fase'] = "3"
            send_message(GRAPH_API_VERSION, 
                         GRAPH_API_TOKEN, 
                         business_phone_number_id, 
                         edited_number, 
                         phase3())
            
        elif message['text'] == "3":
            user['fase'] = "3"
            send_message(GRAPH_API_VERSION, 
                         GRAPH_API_TOKEN, 
                         business_phone_number_id, 
                         edited_number, 
                         phase3())
            
        elif message['text'] == "4":
            user['fase'] = "2A"
            send_message(GRAPH_API_VERSION, 
                         GRAPH_API_TOKEN,
                         business_phone_number_id, 
                         edited_number, 
                         phase2())
        else:
            send_message(GRAPH_API_VERSION, 
                         GRAPH_API_TOKEN, 
                         business_phone_number_id, 
                         edited_number, 
                         "Opción no válida, por favor selecciona una opción válida.")

    elif user['fase'] == "3":
        user['fase'] = "4"
        askLocation(GRAPH_API_VERSION, 
                    GRAPH_API_TOKEN, 
                    business_phone_number_id, 
                    edited_number,
                    phase4())

    elif user[edited_number]['fase'] == "4":
        if message['type'] == 'location':
            user['fase'] = "5"
            send_message(GRAPH_API_VERSION, 
                         GRAPH_API_TOKEN, 
                         business_phone_number_id, 
                         edited_number, 
                         phase5())

    elif user['fase'] == "5":
        user['fase'] = "1"
        send_message(GRAPH_API_VERSION,
                     GRAPH_API_TOKEN, 
                     business_phone_number_id, 
                     edited_number, 
                     phase1())

    else:
        send_message(GRAPH_API_VERSION, 
                     GRAPH_API_TOKEN, 
                     business_phone_number_id, 
                     edited_number, 
                     "Lo siento, no tienes permiso para usar este servicio.")
