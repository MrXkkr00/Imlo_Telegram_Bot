import logging
from transliterate import to_cyrillic,to_latin
from aiogram import Bot,Dispatcher,executor,types
from check import checkWords

API_TOKEN = '1903749937:AAEI72c2tb3cCE_fyNcvqsFZxhKcP8vkL3s'

logging.basicConfig(level=logging.INFO)

bot =Bot(token = API_TOKEN)
dp =Dispatcher(bot)

@dp.message_handler(commands='start' or 'help')
async def send_welcome(message: types.Message):
    await message.reply("Uz imlo botga hush kelibsiz")

@dp.message_handler()
async def checkImlo(message:types.Message):



    for word in message.text.split():
        word=to_cyrillic(word)
        results=checkWords(word)
        if results['avalible']:
            respons=f"True   {word}\n"
        else:
            respons=f"False  {word}\n"
            for text in results['matches']:
                respons +=f"             {text}\n"
        await message.answer(to_latin(respons))

if __name__== '__main__':
    executor.start_polling(dp,skip_updates=True)
