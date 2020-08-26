from chatbot import Chatbot
from flask import Flask, request
app = Flask(__name__)

chatbot = Chatbot()

@app.route("/", methods=['POST'])
def handler():
    event = request.json
    print(event)
    user_id = request.remote_addr
    msg = event.get('msg', '')
    print('handling request from user_id: {} - msg: {}'.format(user_id, msg) )
    return chatbot.chat(user_id, msg)

if __name__ == "__main__":
    app.run()