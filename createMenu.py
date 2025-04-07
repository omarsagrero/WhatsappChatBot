"""
WhatsApp Chatbot Menu Creation

This module contains the code to create a menu for the WhatsApp Chatbot.
It includes functions to create a menu with options for the user to choose from.
The menu is created using the WhatsApp Business API and is designed to be user-friendly and easy to navigate.
The menu is created in a JSON format that is compatible with the WhatsApp Business API.
The menu reads the options from a postgress database and creates a JSON object with the options.

Created by: O. Sagrero
"""

def phase1():
    FASE1 = "Hola, bienvenido a la tiendita, ¿En qué puedo ayudarte?" \
            "\n1. WEED" \
            "\n2. EDIBLES" \
            "\n3. CARTS" \
            "\n4. OTROS"
    return FASE1

def phase2():
    FASE2 = "¿Qué tipo de weed buscas" \
            "\n1. SATIVA" \
            "\n2. INDICA" \
            "\n3. HÍBRIDA" \
            "\n4. REGRESAR" 
    return FASE2


def phase2A1(inventario):
    FASE2A1 = "¿Qué cepa quieres?"
    for i in inventario:
        if i['tipo'] == 'Sativa':
            FASE2A1 += "\n" + str(i['id']) + ". " + i['producto']
    return FASE2A1

def phase2A2(inventario):
    FASE2A2 = "¿Qué cepa quieres?"
    for i in inventario:
        if i['tipo'] == 'Índica':
            FASE2A2 += "\n" + str(i['id']) + ". " + i['producto']
    return FASE2A2

def phase2A3(inventario):
    FASE2A3 = "¿Qué cepa quieres?"
    for i in inventario:
        if i['tipo'] == 'Híbrida':
            FASE2A3 += "\n" + str(i['id']) + ". " + i['producto']
    return FASE2A3

def phase3():
    FASE3 = "¿Cuántas oz quieres?"
    return FASE3

def phase4():
    FASE4 = "Mandanos tu ubicación"
    return FASE4
def phase5():
    FASE5 = "Tu pedido está en camino, gracias por tu compra"
    return FASE5