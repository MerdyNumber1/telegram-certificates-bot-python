build:
	docker-compose --file docker-compose.yml build
start:
	docker-compose --file docker-compose.yml up
stop:
	docker-compose --file docker-compose.yml stop