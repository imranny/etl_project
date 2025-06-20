# etl_project

скопируйте репозиторий командой :
git clone https://github.com/imranny/etl_project.git

далее :

    ```cd etl_project``` 
1.
сборка образа :

    ```make build``` 
или :
```
docker build -t etl_project .
```

2.
запуск контейнера : 

```
make run
```
или : (сначала ```docker volume ls, docker create volume etl```)

```
docker run -it --rm -v etl:/app/data etl_project
```

3.
остановка контейнера :
```
make stop
```

или : 
```
docker stop <container_id> && docker rm <container_id>
```

