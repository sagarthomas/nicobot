from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from .extractor import extract

def init():
    chatbot = ChatBot('Nicobot')
    return chatbot

def train():
    chatbot = init()
    conversation = extract()
    chatbot.set_trainer(ListTrainer)
    chatbot.train(conversation)

def reply(question):
    chatbot = init()
    return str(chatbot.get_response(question))
    

