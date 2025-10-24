# EVIAS Backend

EVIAS (Electronic Veterinary Information and Appointment System) - система для управления ветеринарными клиниками и питомцами.

## Технологии

- Python 3.13+
- Django 5.2
- Django REST Framework
- PostgreSQL
- JWT для аутентификации
- AWS S3 для хранения файлов
- Swagger/ReDoc для документации API

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/STANKIN-EVIAS/EVIAS.git
cd EVIAS/backend
```

2. Создайте виртуальное окружение и активируйте его:
```bash
python -m venv .venv
source .venv/bin/activate  # для Linux/Mac
.venv\Scripts\activate     # для Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Создайте файл `.env` и заполните его необходимыми переменными:
```env
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=postgresql://user:password@localhost:5432/evias
AWS_ACCESS_KEY_ID=your-aws-key
AWS_SECRET_ACCESS_KEY=your-aws-secret
AWS_STORAGE_BUCKET_NAME=your-bucket-name
```

5. Примените миграции:
```bash
python manage.py migrate
```

6. Запустите сервер разработки:
```bash
python manage.py runserver
```

## Структура проекта

- `app/` - основные настройки проекта
  - `settings/` - модульные настройки
    - `base.py` - базовые настройки
    - `dev.py` - настройки разработки
    - `aws_storage.py` - настройки AWS S3
    - `logging.py` - настройки логирования
- `users/` - приложение для управления пользователями
- `pets/` - приложение для управления питомцами
- `vet_clinics/` - приложение для управления клиниками

## API

Документация API доступна по следующим URL:
- Swagger UI: `/swagger/`
- ReDoc: `/redoc/`

### Основные эндпоинты:

#### Аутентификация
- POST `/auth/register/` - регистрация
- POST `/auth/login/` - вход
- POST `/auth/token/refresh/` - обновление токена

#### Пользователи
- GET/PUT `/users/profile/` - профиль текущего пользователя
- GET `/users/` - список пользователей (для админов)

#### Питомцы
- GET/POST `/pets/` - список/создание питомцев
- GET/PUT `/pets/{id}/` - получение/обновление питомца
- GET `/pets/my/` - питомцы текущего пользователя

## Разработка

### Добавление новых моделей

1. Создайте модель в `models.py`
2. Создайте и примените миграции:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Тестирование

Запуск тестов:
```bash
python manage.py test
```

## Развертывание

1. Установите зависимости продакшена:
```bash
pip install -r requirements.txt
```

2. Настройте переменные окружения для продакшена
3. Соберите статические файлы:
```bash
python manage.py collectstatic
```

4. Настройте веб-сервер (например, nginx + gunicorn)