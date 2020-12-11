# Certificates Telegram Bot

## Installation:
```sh
$ cp .env.example .env  # set services env vars here
$ make start
```
## Database Migration:
```sh
$ make migrate
```
## Bot commands:
/create [title] [recipient name] [days to expire, 0 - not expiring] - to create a certificate <br>
/delete [number] - to delete a certificate <br>
/get [number] - to get a certificate
