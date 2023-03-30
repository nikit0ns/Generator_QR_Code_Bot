#  [@yousha_generate_qr_bot](https://t.me/yousha_generate_qr_bot) - Телеграм Бот

<!-- Center image -->
<p align="center">
  <img src="assets/bot_logo.jpg" alt="qr" width="200"/>

## Функционал
- Телеграм бот для генерации QR-кода.
- Бот может сгенерировать QR-код для ссылок и текста.
- Подключена библиотека `'qrcode'`.
- У бота две команды: `/start` , `/help`
- Бот сейчас работает! --> [@yousha_generate_qr_bot](https://t.me/yousha_generate_qr_bot)

Обновления:
- *У бота имеется обработка ошибок.*
- *Бот контейниризован*
- *Можно ссылаться на бота в любом чате*
- *CI и make lint*
- *make run*

---

## Запуск проекта

```bash
pip3 install -r requirements.txt
echo "TOKEN='ТОКЕН:БОТА'" > src/config.py
make run
```

## Скриншоты

<!-- Use fixed width for screenshots -->

<img src="assets/showcase/ux_1.png" alt="Взаимодействие" width="512"/>
<img src="assets/showcase/ux_2.png" alt="Обработка ошибок" width="512"/>
<img src="assets/showcase/ux_3.jpg" alt="Ссылка из чата" width="512"/>


## Связь с автором

[@Quakumei](t.me/Quakumei) - Telegram
