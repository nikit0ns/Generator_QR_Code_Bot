from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import FSInputFile
import asyncio
import config
import qrcode


bot = Bot(token=config.TOKEN) #Ваш токен
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def cmd_start(message: types.Message):
    await message.answer('👋 <b>Привіт, я QR-Код Бот. \n🔒 Я зможу вам згенерувати QR-Код. \n🔗 Надішліть мені текст або посилання.</b>', parse_mode = 'HTML')


@dp.message(Command(commands=['help']))
async def cmd_help(message: types.Message):
    await message.answer("⁉️<b> Якщо у вас є проблеми.</b> \n✉️ <b>Напишіть мені</b> <a href='https://t.me/nikit0ns'>@nikit0ns</a><b>.</b>", disable_web_page_preview = True, parse_mode = 'HTML')


@dp.message()
async def send_text_based_qr(message: types.Message):
    qr = qrcode.QRCode(version=1,
                       error_correction = qrcode.constants.ERROR_CORRECT_L,
                       box_size = 20, 
                       border = 2)

    qr.add_data(message.text)
    qr.make(fit = True)  

    img = qr.make_image(fill_color = 'black', back_color = 'white')
    img.save('photo.png')
    img = FSInputFile('photo.png')

    await message.reply_photo(img, caption = f'<b>✅ Ваш QR-Code успішно згенеровано \n\n⚙️ Створено за допомогою @Generator_QR_Code_Bot</b>', parse_mode = 'HTML')



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())