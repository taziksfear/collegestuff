import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import g4f

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = '' # не дам я вам свой токен для бота :)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

SYSTEM_PROMPT = "Ты чат-бот созданный Артемом из группы ИС-26. У тебя нет имени, но придерживайся своего наименования, которое тебе могут дать. Общайся непринужденно, будто разговариваешь с другом."

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Чем я могу помочь сегодня?")

@dp.message_handler()
async def echo_message(message: types.Message):
    try:
        async with types.ChatActions.typing():
            response = await g4f.ChatCompletion.create_async(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": message.text}
                ],
            )

        if not response:
            raise ValueError("Пустой ответ от API")
            
        if len(response) > 4096:
            response = response[:4093] + "..."
            
        await message.reply(response)
        
    except Exception as e:
        logging.exception("Ошибка при обработке сообщения")
        await message.reply("Извините, произошла ошибка при обработке вашего запроса. Попробуйте позже.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)