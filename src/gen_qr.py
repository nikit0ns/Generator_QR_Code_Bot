"""Generate QR code from text"""

import logging
from io import BytesIO

import qrcode


def gen_qr(text: str) -> BytesIO:
    """Generate QR code from text"""
    logging.info("Генерирую QR для сообщения: %s", text)

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
    logging.info("Код сгенерирован для: %s", text)
    return buf
