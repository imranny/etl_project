# Сборка образа
build:
	docker build -t etl_project .

# Запуск контейнера
run:
	docker run -it --rm -v etl:/app/data etl_project

# Остановка контейнера
stop:
	docker stop 
	docker rm 

# Полная очистка
clean:	
	docker rmi etl_project

# Зайти в контейнер
bash:
	docker run -it --rm -v etl:/app/data etl_project bash


do:
	poetry run python main.py