FROM python:3.13-slim

WORKDIR /app

# Скопировать только необходимые файлы (dockerignore исключит .venv и т.п.)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY . .

# Прослушиваем порт, который проброшен в docker-compose (8000)
EXPOSE 8000

# Для разработки запускаем встроенный сервер на 0.0.0.0:8000
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]

