from flask import Flask, request, jsonify, render_template
from chatter.core import train, reply


app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send():
    return reply(request.data.decode('utf-8'))

@app.route('/train', methods=['POST'])
def doTrain():
    train()
    return "Training complete"

# @app.route("/webhook", methods=['GET', 'POST'])
# def recieve_message():
#     if request.method == 'GET':
#         """Before allowing people to message your bot, Facebook has implemented a verify token
#         that confirms all requests that your bot receives came from Facebook."""
#         token_sent = request.args.get("hub.verify_token")
#         return verify_fb_token(token_sent)
#         #if not get request, then we post
#     else:
#         # Get message from user
#         output = request.get_json()
#         for event in output['entry']:
#             messaging = event['messaging']
#             for message in messaging:
#                 if message.get('message'):
#                     recipient_id = message['sender']['id']
#                     if message['message'].get('text'):
#                         response_sent_text = get_message(message['message'].get('text'))
#                         send_message(recipient_id, response_sent_text)
#         return "Message Processed"

# def verify_fb_token(token_sent):
#     if token_sent == VERIFY_TOKEN:
#         return request.args.get('hub.challenge')
#     return 'Invalid verification token'


# def get_message(question):
#     return reply(question)

# def send_message(recipient_id, response):
#     #send the message
#     bot.send_text_message(recipient_id, response)
#     return "success"

# @app.route('/policy')
# def render():
#     return render_template('privacy-policy.html')


if __name__ == '__main__':
    app.run()
