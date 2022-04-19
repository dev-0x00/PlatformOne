from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

from telegram import ParseMode

from miscellaneous.otherfunctions import Otherfunctions

import pandas as panda

import requests
import tabulate

class Telegram: #require tokens
    """
    Getting id for a group chat send /my_id BOT_NAME to the group or anyone to initiate
    conversation or messaging.
    """


    myTokens = "5008241176:AAEWjhp0R-Xd1wVJ3dzdbRJsZiktzz27KPI" 
    updater = Updater(myTokens, use_context=True)

    def GetChatId(self, botToken):
        """
        create a group or add your bot to a group as a member to get the chat id to send messages
        to the group
        """
        url = "https://api.telegram.org/bot{}/getUpdates".format(botToken)
        response = requests.get(url)
        chatId = (response.json()["result"][0]["my_chat_member"]["chat"]["id"])
        return chatId

    def DefaultText(update: Update, context: CallbackContext):
        update.message.reply_text("Hello?")
    
    def Helper(update: Update, context: CallbackContext):
        update.message.reply_text("This should basically give options on whats availble on bot")

    def Weather(update: Update, context: CallbackContext):

        """"
        This is a demo method, it fetches the weather data from the seven continents and returns
        a nice feedback to the the user when any message containing weather command is sent.
        """
        update.message.reply_text("From which continent do you want weather details exactly?")
    
    def Continent(update: Update, contenxt: CallbackContext):  
        otherFunctions = Otherfunctions(update.message["text"][1:])
        heading, data = otherFunctions.FetchWeatherUpdates()
        table = otherFunctions.TableForData()
        update.message.reply_text(heading)
        print(len(table))
        update.message.reply_text(f'<pre>{table}</pre>', parse_mode=ParseMode.HTML)
       

    #Handlers to hangle messages and commands can be initiated this way
    updater.dispatcher.add_handler(CommandHandler("weather", Weather))
    updater.dispatcher.add_handler(CommandHandler(("Africa", "Asia", "Arctantica"),  Continent))

    updater.start_polling()

if __name__ == "__main__":
    tele = Telegram()
    tele 
