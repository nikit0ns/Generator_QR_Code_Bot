FROM python:3.9-slim-bullseye as production
LABEL maintainer="Tampio I.S. <quakumei@gmail.com>" \
      description="@yousha_generate_qr_bot"

EXPOSE 8080

COPY . /app/
WORKDIR /app

RUN pip install -r requirements.txt
CMD ["python", "src/main.py"]