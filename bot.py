import discord
from bot_logic import gen_pass,new_word,gen_word,gen_emodji

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

mode = 0

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    global mode
    if message.author == client.user:
        return

    if mode == 1:
        new_word(message.content)
        await message.channel.send(f'В генератор слов добавлено слово: {message.content}')
        mode = 0

    elif message.content.startswith('$Привет'):
        await message.channel.send("Hi!")

    elif message.content.startswith('$Пока'):
        await message.channel.send("\U0001f642")

    elif message.content.startswith('/password'):
        await message.channel.send(f'Вот твой пароль из 10 символов:{gen_pass(10)}')

    elif message.content.startswith('/new_word'):
        await message.channel.send('Введи слово:')
        mode = 1

    elif message.content.startswith('/random_word'):
        await message.channel.send(gen_word())

    elif message.content.startswith('/smile'):
        await message.channel.send(gen_emodji())

    else:
        await message.channel.send(f'Что такое {message.content}?')

client.run("MYTOKEN") #MYTOKEN - токен бота
