FROM locustio/locust:latest

WORKDIR /mnt/locust/

COPY [ "./.locust.conf", "." ]
COPY [ "./*.py", "." ]

CMD [ "--conf", "/mnt/locust/.locust.conf" ]
