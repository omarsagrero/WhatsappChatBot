

def accessGrant(allowed_user, edited_number):
    for user in allowed_user:
        if edited_number == user['numero']:
            return True
        
    return False


def getMessage(message):
    if message.get('type') == 'text':
        return {"text": message.get('text', {}).get('body'),
                "type": message.get('type')}
    
    elif message.get('type') == 'location':
        return {"text": "",
                "type": message.get('type')}
    
    else:
        return {"text": "",
                "type": message.get('type')}


def getData(allowed_user, edited_number):
    for user in allowed_user:
        if edited_number == user['numero']:
            return {"id": user['id'],
                    "Nombre": user['nombre'],
                    "Fase": user['fase']}
        
    return None
