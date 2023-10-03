# import firebase_admin
# from firebase_admin import credentials, messaging
# firebase_cred = credentials.Certificate("../cred.json")
# firebase_app = firebase_admin.initialize_app(firebase_cred)

# # tokens are list of token
# def send_token_push(title, body, tokens):
#     message = messaging.MulticastMessage(
#     notification=messaging.Notification(
#     title=title,
#     body=body
#     ),
#     tokens=tokens
#     )
#     messaging.send_multicast(message)

def delete_na_fields(map):
    for key in list(map.keys()):
        if map[key] == "":
            del map[key]
        elif map[key] == []:
            del map[key]
        elif map[key] == None:
            del map[key]
    return map
