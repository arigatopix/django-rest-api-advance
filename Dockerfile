# สร้าง image ของ project โดยเอา image ใน hub มาเป็นส่วนหนึ่ง
FROM python:3.7-alpine
MAINTAINER Arigato

ENV PYTHONUNBUFFERED 1

# copy จาก local ไปหา docker
COPY ./requirements.txt /requirements.txt
# install postgres update package alpine ไม่ต้อง save cache(ต้องการให้ image เล็กที่สุด) แล้วลง postgresql
RUN apk add --update --no-cache postgresql-client
# ลง apk ใน tmp (\ คือคำสั่งบรรทัดเดียวกัน)
RUN apk add --update --no-cache --virtual .tmp-build-deps \
  gcc libc-dev linux-headers postgresql-dev
RUN pip install -r requirements.txt
# remove temp หลังจาก install apk 
RUN apk del .tmp-build-deps

# สร้าง folder ใน docker image และให้ทำงานใน /app
RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user