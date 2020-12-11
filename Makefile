build:
	docker-compose build
start:
	docker-compose up
stop:
	docker-compose stop
migrate:
	docker-compose exec bot pipenv run migrate