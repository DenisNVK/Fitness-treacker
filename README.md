# Фитнес-трекер: сбор и анализ данных

Проект для работы с фитнес-данными через Docker.

## Запуск:
1. Установите Docker и Docker Compose
2. Выполните: docker-compose up -d
3. Ждите 1-2 минуты

## Сервисы:
- Redash: http://localhost:5000
- Jupyter: http://localhost:8888 (пароль: fitness)
- PostgreSQL: localhost:5432 (логин/пароль: fitness)

## Структура:
- generator/ - генератор данных
- db/ - база данных  
- notebooks/ - анализ в Jupyter
- redash1/ - дашборды

## SQL подключение:
Host: fitness-db
Database: fitness
User: fitness  
Password: fitness
Port: 5432

## Работает автономно:
- Генератор создает данные каждые 0.5 сек
- Данные сохраняются в PostgreSQL
- Доступны для анализа в Jupyter и Redash
EOF
