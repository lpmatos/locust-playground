FROM locustio/locust:latest

WORKDIR /mnt/locust/

COPY [ "./.master.conf", "." ]
COPY [ "./.worker.conf", "." ]
COPY [ "./*.py", "." ]

CMD [ "--conf", "/mnt/locust/.master.conf" ]
