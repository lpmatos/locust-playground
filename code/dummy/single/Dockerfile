FROM python:3.8.5-alpine3.12

WORKDIR /usr/src/dummy

COPY [ "requirements.txt", "." ]

RUN pip install --upgrade pip && \
    pip install --trusted-host pypi.python.org -r requirements.txt

COPY [ "app.py", "." ]

CMD [ "python", "app.py" ]
