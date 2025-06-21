from flask import Flask, request
import requests
import os

app = Flask(__name__)

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
IMG_URL = "https://i.imgur.com/qY4rrHY.jpeg"
API_URL = f"https://graph.facebook.com/v18.0/{{}}/messages".format(PHONE_NUMBER_ID)

def send_message(to, text):
    return requests.post(API_URL, headers={
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }, json={"messaging_product":"whatsapp","to":to,"type":"text","text":{"body":text}})

def send_image(to, link, caption):
    return requests.post(API_URL, headers={
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }, json={"messaging_product":"whatsapp","to":to,"type":"image","image":{"link":link,"caption":caption}})

@app.route("/webhook", methods=["GET"])
def verify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge"), 200
    return "Forbidden", 403

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    entry = data.get('entry', [])
    for change in entry[0].get('changes', []):
        msg = change.get('value', {}).get('messages', [])
        if not msg: continue
        msg = msg[0]
        number = msg['from']
        text = msg.get('text', {}).get('body', '').strip()
        if text == "1":
            send_message(number, f"Você pode fazer seu pedido pelo nosso iFood! 🍫🛵\n\n📲 Acesse agora:\nhttps://www.ifood.com.br/delivery/recife-pe/kopenhagen-tacaruna-recife-santo-amaro/b2346fd5-f700-4f35-be96-4d3e973262ee?utm_medium=share")
        elif text == "2":
            caption = "📍 Nossa loja no Shopping Tacaruna, piso térreo, em frente ao Outback.\n🕒 Segunda a Sábado: 9h às 22h\nDomingos: 12h às 21h"
            send_image(number, IMG_URL, caption)
        elif text == "3":
            send_message(number, "🔔 Estamos te conectando com um atendente da loja... ☎️")
        else:
            send_message(number, "Olá! 🍫 Bem-vindo à Kopenhagen Tacaruna!\nEscolha:\n1️⃣ Fazer um pedido\n2️⃣ Onde estamos\n3️⃣ Falar com a Kopenhagen Tacaruna")
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
