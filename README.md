# Simple API for Parsing Data from Module Bank

<p></p>

### Стэк:
<p align="center">
    <img src="https://img.shields.io/badge/aiogram-blue.svg"/>
    <img src="https://img.shields.io/badge/fastapi-blue.svg"/>
    <img src="https://img.shields.io/badge/scikit-blue.svg"/>
    <img src="https://img.shields.io/badge/uvicorn-blue.svg"/>
    <img src="https://img.shields.io/badge/Requests-2.26.0-yellow?logo=requests&style=flat"/>
    <img src="https://img.shields.io/badge/Docker%20Compose-1.29.2-blue?logo=docker&style=flat"/>
</p>

### Запуск приложения:
1. Клонируем репозиторий:
```
git clone git@github.com:leabrun/api_bank.git
```
2. Переходим в директорию проекта:
```
cd api_bank
```
3. Запускаем docker-compose:
```
docker-compose up -d --build
```

### Маршруты API:
#### Получить ответ:
 - Endpoint: /question/
 - Метод: POST
 - Параметры: question_str
 - Описание: Принимает на вход строковое значение вопроса и возвращает строковый ответ, предсказанный моделью.
