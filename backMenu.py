from messagesAPI import *
from createMenu import *
from manageDatabase import *

def selectMenuOption(GRAPH_API_VERSION, 
                     GRAPH_API_TOKEN, 
                     inventario, 
                     user, 
                     message, 
                     edited_number, 
                     business_phone_number_id):
    
    if user['Fase'] == "1":
        if message['text'] == "1":
            user['Fase'] = '2A'
            send_message(GRAPH_API_VERSION,
                        GRAPH_API_TOKEN,
                        business_phone_number_id,
                        edited_number,
                        phase2())
            
        elif message['text'] == "2":
            user['Fase'] = '2B'
            send_message(GRAPH_API_VERSION,
                        GRAPH_API_TOKEN,
                        business_phone_number_id,
                        edited_number,
                        phase2())
        elif message['text'] == "3":
            user['Fase'] = '2C'
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

    elif user['Fase'] == "2A":        
        if message['text'] == "1":
            user['Fase'] = '2A1'
            send_message(GRAPH_API_VERSION,
                        GRAPH_API_TOKEN,
                        business_phone_number_id,
                        edited_number,
                        phase2A1(inventario))
            
        elif message['text'] == "2":
            user['Fase'] = '2A2'
            send_message(GRAPH_API_VERSION,
                        GRAPH_API_TOKEN,
                        business_phone_number_id,
                        edited_number,
                        phase2A2(inventario))
            
        elif message['text'] == "3":
            user['Fase'] = '2A3'
            send_message(GRAPH_API_VERSION,
                         GRAPH_API_TOKEN,
                         business_phone_number_id,
                         edited_number,
                         phase2A3(inventario))
            
        elif message['text'] == "4":
            user['Fase'] = '1'
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

    elif user['Fase'] == "2A1":
        if message['text'] == "1":
            user['Fase'] = '3'
            send_message(GRAPH_API_VERSION,
                         GRAPH_API_TOKEN,
                         business_phone_number_id,
                         edited_number,
                         phase3())
            
        elif message['text'] == "2":
            user['Fase'] = '3'
            send_message(GRAPH_API_VERSION, 
                         GRAPH_API_TOKEN, 
                         business_phone_number_id, 
                         edited_number, 
                         phase3())
            
        elif message['text'] == "3":
            user['Fase'] = '3'
            send_message(GRAPH_API_VERSION,
                         GRAPH_API_TOKEN, 
                         business_phone_number_id,
                         edited_number,
                         phase3())
            
        elif message['text'] == "4":
            user['Fase'] = '2A'
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

    elif user['Fase'] == "2A2":
        if message['text'] == "1":
            user['Fase'] = '3'
            send_message(GRAPH_API_VERSION, 
                         GRAPH_API_TOKEN, 
                         business_phone_number_id, 
                         edited_number, 
                         phase3())
            
        elif message['text'] == "2":
            user['Fase'] = '3'
            send_message(GRAPH_API_VERSION,
                         GRAPH_API_TOKEN, 
                         business_phone_number_id, 
                         edited_number, 
                         phase3())
            
        elif message['text'] == "3":
            user['Fase'] = '3'
            send_message(GRAPH_API_VERSION, 
                         GRAPH_API_TOKEN, 
                         business_phone_number_id, 
                         edited_number, 
                         phase3())
            
        elif message['text'] == "4":
            user['Fase'] = '2A'
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

    elif user['Fase'] == "2A3":
        
        if message['text'] == "1":
            user['Fase'] = '3'
            send_message(GRAPH_API_VERSION, 
                         GRAPH_API_TOKEN, 
                         business_phone_number_id, 
                         edited_number, 
                         phase3())
            
        elif message['text'] == "2":
            user['Fase'] = '3'
            send_message(GRAPH_API_VERSION, 
                         GRAPH_API_TOKEN, 
                         business_phone_number_id, 
                         edited_number, 
                         phase3())
            
        elif message['text'] == "3":
            user['Fase'] = '3'
            send_message(GRAPH_API_VERSION, 
                         GRAPH_API_TOKEN, 
                         business_phone_number_id, 
                         edited_number, 
                         phase3())
            
        elif message['text'] == "4":
            user['Fase'] = '2A'
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

    elif user['Fase'] == "3":
        user['Fase'] = '4'
        askLocation(GRAPH_API_VERSION, 
                    GRAPH_API_TOKEN, 
                    business_phone_number_id, 
                    edited_number,
                    phase4())

    elif user['Fase'] == "4":
        if message['type'] == 'location':
            user['Fase'] = '5'
            send_message(GRAPH_API_VERSION, 
                         GRAPH_API_TOKEN, 
                         business_phone_number_id, 
                         edited_number, 
                         phase5())

    elif user['Fase'] == "5":
        user['Fase'] = '1'
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

    return user