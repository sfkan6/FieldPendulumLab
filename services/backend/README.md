# BACKEND

http://localhost:8000/

## Modules

- **storing_data_samples** - Собирает выборки данных, хранит их в виде файлов **.json** в папке **sample_storage**
- **data_streaming** - Занимается потоковой обработкой и передачей данных, **использует камеру** для получения данных
- **charting** - Выполняет построение графиков и аппроксимаций

## Development

```python
python -m venv venv

. venv/bin/activate

pip install -r requirements.txt

cd src

uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Docker

Собрать:
```
sudo docker build -t fpl-backend .
```

Запустить:

```
sudo docker run --device=/dev/video0 -p 8000:8000 fpl-backend
```

> [!WARNING]
> **data_streaming** использует камеру и opencv для распознавания углов маятника, в зависимости от **OS** аргумент **--device** должен быть изменён