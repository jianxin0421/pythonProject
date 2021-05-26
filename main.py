#import constants as keys
#from telegram.ext import *
#import responses as R



#print("Bot started")


#def start_command(update, context):
#    update.message.reply_text('Type something here.')


#def help_command(update, context):
#    update.message.reply_text('What can i help you?')


#def handler_message(update, context):
#    text = str(update.message.text).lower()
#    response = R.sample_response(text)

#    update.message.reply_text(response)


#def error(update, context):
#    print(f"Update {update} caused error {context.error}")


#def main():
#    updater = Updater(keys.API_KEY, use_context=True)
#    dp = updater.dispatcher

#    dp.add_handler(CommandHandler("start", start_command))
#    dp.add_handler(CommandHandler("help", help_command))

#    dp.add_handler(MessageHandler(Filters.text, handler_message))

#    dp.add_error_handler(error)

#    updater.start_polling()
#    updater.idle()


#main()
import os
from http import server

import webbrowser
import schedule
import time
import urllib.request

def sudo_placement():
    print("Get ready for Sudo Placement at Geeksforgeeks")


def demo():
    #webbrowser.open('https://api.telegram.org/bot1808471997:AAEvGMqX9EvGgIs5Z7bERnJ-I9XIADg7N38/sendMessage?chat_id=-595191824&text=check%20it%20up')
    weburl = urllib.request.urlopen('https://api.telegram.org/bot1808471997:AAEvGMqX9EvGgIs5Z7bERnJ-I9XIADg7N38/sendMessage?chat_id=-595191824&text=check%20it%20up')

schedule.every(1).minutes.do(demo)

while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)

