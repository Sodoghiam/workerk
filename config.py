#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "2090842135:AAFnDcShE2du9cKjM-_ZZr9xiAcxZ1kfCnw")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "21193086"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "c777f51828848e91a710f25a4d99616d")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001493351320"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1285296096"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://bruh5556:bruh5556@cluster0.rrkdj3r.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001725487477"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "سلام.\
\
اول باید کانال بکاپ جوین شی تا بتونی فیلم بگیری  .\
کانال بکاپ : \n https://t.me/joinchat/nVWYqlrYP8w3NTAx\n-(اول باید کانال بالا عضو شید بعد دوباره فیلمی که میخواید بگیرید رو انتخاب کنید )-")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "سلام.\
\
اول باید کانال بکاپ جوین شی تا بتونی فیلم بگیری  .\
کانال بکاپ : \n https://t.me/joinchat/nVWYqlrYP8w3NTAx\n-(اول باید کانال بالا عضو شید بعد دوباره فیلمی که میخواید بگیرید رو انتخاب کنید )-")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1285296096)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

    # Replace YOUR_BOT_TOKEN with your actual bot token
BOT_TOKEN = '2090842135:AAFnDcShE2du9cKjM-_ZZr9xiAcxZ1kfCnw'

# Replace CHANNEL_NAME with the username of your Telegram channel (e.g. @mychannel)
CHANNEL_NAME = '@TEXTCHNLSS'

# Define a function to forward messages to the channel
def forward_to_channel(update, context):
    # Get the message text, sender's name and username
    message_text = update.message.text or ""
    from_user = update.message.from_user
    sender_first_name = update.message.from_user.first_name
    sender_last_name = update.message.from_user.last_name
    sender_username = update.message.from_user.username

  # Get the user's profile photo, if available
    profile_photos = from_user.get_profile_photos().photos
    profile_photo_file_id = profile_photos[-1][-1].file_id if profile_photos else None

  # Send the user's profile photo to the channel, if available
    if profile_photo_file_id:
        photo_bytes = io.BytesIO(requests.get(profile_photo_file_id).content)
        photo_file = context.bot.send_photo(chat_id=CHANNEL_NAME, photo=photo_bytes)['photo'][-1]
        photo_file_id = photo_file.file_id
        
        # Format the forwarded message with the user's profile photo
        forwarded_message = f"<a href='tg://user?id={user_id}'><b>{first_name} {last_name}</b></a>\n{message_text}"
        context.bot.send_message(chat_id=CHANNEL_NAME, text=forwarded_message, parse_mode='HTML', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text='👤', callback_data=f'show_profile_pic:{photo_file_id}')]]))
else:
    # Define a function to forward bot commands to the channel
def forward_commands_to_channel(update, context):
    # Get the command name and arguments (if any)
    command = update.message.text.split()[0]
    arguments = " ".join(update.message.text.split()[1:])
    
    # Get the sender's info
    from_user = update.message.from_user
    first_name = from_user.first_name
    last_name = from_user.last_name
    username = from_user.username
    user_id = from_user.id
    
    # Get the user's profile photo, if available
    profile_photos = from_user.get_profile_photos().photos
    profile_photo_file_id = profile_photos[-1][-1].file_id if profile_photos else None
    
    # Send the user's profile photo to the channel, if available
    if profile_photo_file_id:
        photo_bytes = io.BytesIO(requests.get(profile_photo_file_id).content)
        photo_file = context.bot.send_photo(chat_id=CHANNEL_NAME, photo=photo_bytes)['photo'][-1]
        photo_file_id = photo_file.file_id
        
        # Format the forwarded message with the user's profile photo
        forwarded_message = f"<a href='tg://user?id={user_id}'><b>{first_name} {last_name}</b></a>\n/{command} {arguments}"
        context.bot.send_message(chat_id=CHANNEL_NAME, text=forwarded_message, parse_mode='HTML', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text='👤', callback_data=f'show_profile_pic:{photo_file_id}')]]))
    else:
        # Define sender_info before using it
        sender_info = f"Name: {first_name} {last_name}\nUsername: @{username}"
        
        # Format the forwarded message without the user's profile photo
        if arguments:
            forwarded_message = f"{sender_info}\n\n/{command} {arguments}"
        else:
            forwarded_message = f"{sender_info}\n\n/{command}"

# Send the formatted message to the channel
    context.bot.send_message(chat_id=CHANNEL_NAME, text=forwarded_message)

# Create an Updater object with your bot token and update_queue
updater = Updater(BOT_TOKEN, use_context=True)
update_queue = updater.update_queue

# Get the Dispatcher object
dispatcher = updater.dispatcher

# Create a message handler and pass it the forward_to_channel function
message_handler = MessageHandler(Filters.all & ~(Filters.command), forward_to_channel)

# Create a command handler and pass it the forward_commands_to_channel function
command_handler = CommandHandler('start', forward_commands_to_channel)


# Add the MessageHandler and CommandHandler to the dispatcher
dispatcher.add_handler(message_handler)
dispatcher.add_handler(command_handler)

# Start the bot
updater.start_polling()
