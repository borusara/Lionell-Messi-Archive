import random
from telethon.sync import TelegramClient, events
import riddles # python libs are chad

# Create a TelegramClient instance
client = TelegramClient('existing_bot', api_id, api_hash)

# Function to get a random brain teaser from the lib 🗿
def get_random_riddle():
    riddle = random.choice(riddles.riddles)
    question = riddle["question"]
    answer = riddle["answer"]
    return {'question': question, 'answer': answer}

# Function to handle incoming messages , 🗿
@client.on(events.NewMessage(pattern='/riddle'))
async def handle_riddle(event):
    message = event.message
    sender = await event.get_sender()
    current_riddle = get_random_riddle()
    await message.reply("Here's a riddle for you:\n" + current_riddle['question'])

    # Function to check the answers🗿
    async def check_answer(answer_message):
        user_answer = answer_message.text.strip().lower()
        if user_answer == current_riddle['answer']:
            await answer_message.reply("Oh, you have won, but you don't win anything 🗿")
        else:
            await answer_message.reply("Sorry to say, but that is not correct 🗿")
            await answer_message.reply("Try again or type /riddle for a new riddle.")

    # Wait for the answer message
    async with client.conversation(sender) as conv:
        answer_message = await conv.get_response()
        await check_answer(answer_message)

# Start the bot, no?
async def start_bot():
    await client.start()
    await client.run_until_disconnected()

#  let's Run the bot 🗿
if name == 'main':
    client.loop.run_until_complete(start_bot())
