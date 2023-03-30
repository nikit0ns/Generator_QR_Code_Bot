"""This is a simple bot that generates QR codes from text."""

import asyncio
import logging

from aiogram import Bot, Dispatcher, types

from src import config
from src.gen_qr import gen_qr

bot = Bot(token=config.TOKEN)  # Ваш токен
dp = Dispatcher(bot)

# Set logging level
logging.basicConfig(level=logging.INFO)


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


@dp.message_handler()
async def send_text_based_qr(message: types.Message):
    """QR generation command handler"""
    qr_code = gen_qr(message.text)
    await message.reply_photo(
        qr_code,
        caption=f"<b>✅ Ваш QR успешно сгенерирован: {message.text}\n"
        "Сделано с помощью @yousha_generate_qr_bot</b>",
        parse_mode="HTML",
    )


@dp.inline_handler()
async def inline_ad(inline_query: types.InlineQuery):
    """Отправить ссылку на бота"""
    await bot.answer_inline_query(
        inline_query.id,
        results=[
            types.InlineQueryResultArticle(
                id="1",
                title="Yousha QR-code generator bot",
                input_message_content=types.InputTextMessageContent(
                    "<b>Перейди в @yousha_generate_qr_bot, "
                    "чтобы сгенерировать QR-код!</b>",
                    parse_mode="HTML",
                ),
                description="Бот для генерации QR-кодов по тексту",
                thumb_url="https://github.com/Quakumei/"
                "QR_Code_Bot/raw/main/assets/bot_logo.jpg",
                thumb_width=512,
                thumb_height=512,
            )
        ],
        cache_time=1,
    )


async def main():
    """Start the bot"""
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
