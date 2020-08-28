FROM locustio/locust:latest

WORKDIR /mnt/locust/

COPY [ "./.master.conf", "." ]
COPY [ "./.worker.conf", "." ]
COPY [ "./src", "." ]

CMD [ "--conf", "/mnt/locust/.master.conf" ]
