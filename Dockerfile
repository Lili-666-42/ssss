# Используем образ с Python для Django
FROM python:3.8-slim as django

# Устанавливаем рабочую директорию для приложения Django
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы приложения в контейнер
COPY . .

# Определяем переменные среды для Django
ENV DJANGO_SETTINGS_MODULE=myproject.settings
ENV PYTHONUNBUFFERED=1

# Запускаем сборку статических файлов Django

# Определяем порт, который будет использоваться Django
EXPOSE 8000

# Запускаем сервер Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# -*- coding: utf-8 -*-