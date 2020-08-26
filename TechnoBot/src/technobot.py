"""
Author: Rakesh Yadav
Aim: To make a conversational chatbot by using ML, NLTK & tkinter
        through python.
"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat-bot named as TechnoBot
chatbot = ChatBot('TechnoBot')

trainer = ListTrainer(chatbot)
# using file-handling concept to accessing training-data
training_data = open('training_data/updated_QA_bank.txt').read().splitlines()

trainer.train(training_data)

print("\n ***************##############*******************\n\t........ YOU ARE TALKING TO TECHNOBOT .........\n")

while True:
    query = input()
    if query == "exit":
        break
    bot_response = chatbot.get_response(query)
    print("Bot : ", bot_response)
