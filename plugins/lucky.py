import random
from telegram import Update
from telegram.ext import Updater, CommandHandler

# List of videos set by the admin
admin_videos = [
    "video1.mp4",
    "video2.mp4",
    "video3.mp4",
    "video4.mp4",
    # Add more videos as needed
]

def get_random_video(update: Update, context):
    random_video = random.choice(admin_videos)
    context.bot.send_video(chat_id=update.effective_chat.id, video=open(random_video, 'rb'))

# Add command handlers
get_random_video_handler = CommandHandler('getvideo', get_random_video)


dispatcher.add_handler(get_random_video_handler)
