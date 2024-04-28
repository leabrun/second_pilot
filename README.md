# Второй пилот для куратора. Проект в рамках хакатона "Цифровой Прорыв 2024" для GeekBrains.

<p>Этот проект - необходимо важный компонент для обеспечения автоматизации ответов. Благодаря его использованию, будет оптимизированно время использования человеческих
ресурсов в лице операторов поддержки, идентифицируя вопрос пользователя и предсказывая ответ на него с помощью модели, обученной по нейросети GigaChat. Модель в свою
очередь напрямую прикручена к API, позволяя тем самым организовать быстрый доступ к ней по человекочитаемым параметрам и в конце получать ответ такого же типа.</p> <p>Дополнительно в этом проекте реализован чат-бот на платформе Telegram, который базируется на взаимодействии с вышеупомянутым API. Бот получает вопрос от пользователя, 
отправляя ему обратно ответ, полученный в ходе обращения к API.</p>

### Стэк:
<p align="center">
    <img src="https://img.shields.io/badge/fastapi-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
    <img src="https://img.shields.io/badge/aiogram-2CA5E0?style=for-the-badge&logo=python&logoColor=white"/>
    <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
    <img src="https://img.shields.io/badge/uvicorn-008272?style=for-the-badge&logo=uvicorn&logoColor=white"/>
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
#### - Получить ответ:
 - Endpoint: /question/
 - Метод: POST
 - Параметры: question_str
 - Описание: Принимает на вход строковое значение вопроса и возвращает строковый ответ, предсказанный моделью.
