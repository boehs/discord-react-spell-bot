def is_isogram(string):
   for i in string:
       if string.count(i) > 1:
           return False
   return True

lettersdict = {
    'a': "🇦",
    'b': "🇧",
    'c': "🇨",
    'd': "🇩",
    'e': '🇪',
    'f': '🇫',
    'g': '🇬',
    'h': '🇭',
    'i': '🇮',
    'j': '🇯',
    'k': '🇰',
    'l': '🇱',
    'm': '🇲',
    'n': '🇳',
    'o': '🇴',
    'p': '🇵',
    'q': '🇶',
    'r': '🇷',
    's': '🇸',
    't': '🇹',
    'u': '🇺',
    'v': '🇻',
    'w': '🇼',
    'x': '🇽',
    'y': '🇾',
    'z': '🇿',
    ' ': '⬜',
    '.': '⏺️',
    '!': '❕',
    '?': '❔',
}

import discord
import config

client = discord.Client()

@client.event
async def on_ready():
    global channel
    print(f'> Logged in as: {client.user}')
    print(client.user.id)
    print('-----READY----- \n')
    channel = client.get_channel(int(input("> Enter the channel you wish to send messages in: ")))
    await console_input()
    

@client.event
async def console_input():
    global channel
    await client.wait_until_ready()
    while True:
        msg = input('> Message to send: ')
        if is_isogram(msg) and len(msg) <= 20:
            break
        else:
            print("not quite! you can only use one letter once (including spaces) and your message must be less than 20 letters")
    async for message in channel.history(limit=1):
        for l in msg.lower():
            await message.add_reaction(lettersdict[l])
    
    print('')
    await console_input()

if config.bot == True:
    client.run(config.token)
if config.bot == False:
    client.run(config.token, bot = False)