# FieldPendulumLab

Приложение для выполнения лабораторной работы по маятнику поля

http://localhost:5000/

> [!WARNING]
> Приложение использует камеру, в зависимости от **OS** измените строку **devices** в **docker-compose.yml**. По умолчанию работает с Linux.


## Development

[backend](https://github.com/sfkan6/FieldPendulumLab/tree/main/services/backend)

[frontend](https://github.com/sfkan6/FieldPendulumLab/blob/main/services/frontend/README.md)


## Docker

Собрать:
```
sudo docker-compose build
```

Запустить:

```
sudo docker-compose up
```

> [!TIP]
> Для автоматического запуска при включении оборудования раскомментируйте `restart: always` в **docker-compose.yml** и запустите. Для отмены закомментируйте и запустите.