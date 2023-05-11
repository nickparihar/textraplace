import re
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enter your Telegram bot token here
bot_token = '5828988755:AAHy9aDTN5WmIdj_oTjjgohSpCbNMjsXGqI'

# Enter the ID of the Telegram channel here
channel_id = -1939684824 # replace with your own channel ID

# Initialize the Telegram bot
bot = telegram.Bot(token=bot_token)

# Define a function to handle incoming messages
def handle_message(update, context):
    message = update.message.text
    if re.search('keyword1|keyword2|keyword3', message):
        # Replace the target text with the desired replacement text
        new_message = re.sub('keyword1|keyword2|keyword3', 'replacement_text', message)
        # Edit the original message with the modified text
        bot.edit_message_text(chat_id=channel_id, message_id=update.message.message_id, text=new_message)
        # Send a message to the user letting them know their message has been modified
        bot.send_message(chat_id=update.message.chat_id, text='Your message has been modified.')
        
# Start the bot and listen for incoming messages
updater = Updater(bot_token, use_context=True)
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
updater.start_polling()
updater.idle()
