"""
    This is a simple bot that generates QR codes from text.
"""

import asyncio
import logging
from io import BytesIO

import qrcode
from aiogram import Bot, Dispatcher, types

from src import config

bot = Bot(token=config.TOKEN)  # Ваш токен
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    """Start command handler"""
    await message.answer(
        "<b>Привет, я QR Бот. \nЯ помогу вам сгенерировать QR-Код. \n"
        "Отправь мне текст для кодирования.</b>",
        parse_mode="HTML",
    )


@dp.message_handler(commands=["help"])
async def cmd_help(message: types.Message):
    """Help command handler"""
    await message.answer(
        "<b>Если у вас возникли проблемы.</b> \n"
        "<b>Напишите мне</b> <a href='https://t.me/quakumei'>"
        "@Quakumei</a><b>.</b>\n"
        "<b>Доступные команды:</b> /start , /help",
        disable_web_page_preview=True,
        parse_mode="HTML",
    )


# If media is sent to the bot, it will be processed here
@dp.message_handler(
    content_types=[
        "photo",
        "video",
        "audio",
        "document",
        "sticker",
        "location",
        "contact",
        "venue",
        "animation",
        "dice",
        "game",
        "poll",
        "invoice",
        "successful_payment",
        "passport_data",
        "voice_chat_scheduled",
        "voice_chat_started",
        "voice_chat_ended",
        "voice_chat_participants_invited",
    ]
)
async def error(message: types.Message):
    """Wrong media type handler"""
    await message.answer(
        "<b>❌ Ошибка! \nВы отправили неподдерживаемый тип медиа. \n"
        "Пожалуйста, отправьте текст для кодирования.</b>",
        parse_mode="HTML",
    )


@dp.message_handler(commands=["qr"])
async def send_text_based_qr(message: types.Message):
    """/qr command handler"""

    def gen_qr(text: str) -> BytesIO:
        """Generate QR code from text"""
        qr_code = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=20,
            border=2,
        )
        qr_code.add_data(text)
        qr_code.make(fit=True)

        img = qr_code.make_image(fill_color="black", back_color="white")
        buf = BytesIO()
        img.save(buf, format="PNG")
        buf.seek(0)

        return buf

    logging.info("Генерирую QR для сообщения: %s", message.text)
    qr_code = gen_qr(message.text)
    logging.info("Код сгенерирован для: %s", message.text)

    await message.reply_photo(
        qr_code,
        caption=f"<b>✅ Ваш QR успешно сгенерирован: {message.text}\n"
        "Сделано с помощью @yousha_generate_qr_bot</b>",
        parse_mode="HTML",
    )


@dp.message_handler()
async def general(message: types.Message):
    """Any text message will be processed here"""
    await send_text_based_qr(message)


async def main():
    """Start the bot"""
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
