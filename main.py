from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f"Здраствуй {message.from_user.first_name}, я самый первый бот созданный моим создателем")
async def info_bot(message):
    print(message)

@dp.message_handler(commands=['myinfo'])
async def info_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f"Вас зовут {message.from_user.first_name}, ваш ник {message.from_user.username}, фамилия ваша {message.from_user.last_name}, ваш id {message.from_user.id}")
@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    await bot.send_message(message.from_user.id, 'я имею 4 команды:\n'
                                                   '/start - команда start должна приветствовать по имени\n'
                                                   '/myinfo -команда myinfo должна отправлять пользователю его данные(id, first_name, username)\n'
                                                   '/help - поможет с командами\n'
                                                   '/picture -  скинет фото котика\n')




@dp.message_handler(commands=['pic'])
async def pic(message: types.Message):
    photo = open('media/img.png', 'rb')
    await message.answer_photo(photo)





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
