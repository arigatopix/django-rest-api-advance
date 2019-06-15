FROM python:3.7-alpine
MAINTAINER Arigato

ENV PYTHONUNBUFFERED 1

# copy จาก local ไปหา docker
COPY ./requirements.txt /requirements.txt
# update package alpine ไม่ต้อง save cache(ต้องการให้ image เล็กที่สุด) แล้วลง postgresql
RUN apk add --update --no-cache postgresql-client
RUN pip install -r requirements.txt

# สร้าง folder ใน docker image และให้ทำงานใน /app
RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user