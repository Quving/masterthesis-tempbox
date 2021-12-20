FROM python:3.8

LABEL maintainer="vinh-ngu@hotmail.com"

WORKDIR /app
ADD . .

RUN chmod +x entrypoint.sh
RUN pip install -r requirements.txt

CMD ["./entrypoint.sh"]
