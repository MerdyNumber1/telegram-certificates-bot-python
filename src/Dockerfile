FROM python:3.9

COPY . /usr/local/src/app
WORKDIR /usr/local/src/app

RUN pip install pipenv && \
    pipenv install

CMD ["pipenv", "run", "start"]