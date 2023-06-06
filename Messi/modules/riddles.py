import random
from telethon.sync import TelegramClient, events

# Create a TelegramClient instance
client = TelegramClient('brain_teasers_bot', api_id, api_hash)

# List of brain teasers
brain_teasers = [
    {
        'question': "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
        'answer': 'echo'
    },
    {
        'question': "What has keys but can't open locks?",
        'answer': 'piano'
    },
    {
        'question': "What comes once in a minute, twice in a moment, but never in a thousand years?",
        'answer': 'letter m'
    },
    # Add more brain teasers here
]

# Function to handle incoming messages
@client.on(events.NewMessage)
async def handle_message(event):
    message = event.message
    sender = await event.get_sender()
    if message.text:
        text = message.text.strip().lower()
        if text == '/riddle':
            random_teaser = random.choice(brain_teasers)
            await message.reply(f"Here's a riddle for you:\n\n{random_teaser['question']}")
        else:
            user_answer = text
            for teaser in brain_teasers:
                if user_answer == teaser['answer']:
                    await message.reply("Oh, you have won, but you don't win anything 🗿")
                    break
            else:
                await message.reply("Sorry to say, but that is not correct 🗿")

# Start the bot
async def start_bot():
    await client.start()
    await client.run_until_disconnected()

# Run the bot
if name == 'main':
    client.loop.run_until_complete(start_bot())
