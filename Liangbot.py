import asyncio
from datetime import datetime
from telegram import Bot

# Define your bot token
TOKEN = '6084519947:AAFxaMXHTp8pHSUJMZtX1PJbpSb5zlmhgr4'

# Define the reminder message
reminder_message = "平安，健康，快乐，从交易里不断盈利，生活富足幸福，岁月静好每一天 ^_^"

# Create an instance of the Bot class
bot = Bot(token=TOKEN)

# Define the asynchronous function to send the reminder message
async def send_reminder():
    await bot.send_message(chat_id='5021626843', text=reminder_message)

# Run the bot continuously
async def main():
    # Keep track of whether the reminder has been sent
    reminder_sent = False

    while True:
        # Get the current time
        current_time = datetime.now().strftime('%H:%M')

        # Check if it's a whole hour
        if current_time.endswith(':00'):
            # Send the reminder message only if it hasn't been sent before
            if not reminder_sent:
                await send_reminder()
                reminder_sent = True
        else:
            # Reset the reminder_sent flag for the next hour
            reminder_sent = False

        # Sleep for 1 minute
        await asyncio.sleep(60)

# Run the main function
asyncio.run(main())
