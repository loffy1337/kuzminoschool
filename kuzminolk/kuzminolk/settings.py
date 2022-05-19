from pathlib import Path
import os

# Путь к базовой директории проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ
SECRET_KEY = 'django-insecure-_lmics1^)4v41^hwl4&_nna@li2wcxcf0pdi$z9@bop%mazwqc'

# Константа отвечающая за режим (True - при тестировании на локальном сервере, False - при загрузке на хостинг)
DEBUG = True
# Список доменов, на которых будет веб-приложение (по стандарту: 127.0.0.1:8000 или localhost:8000)
ALLOWED_HOSTS = []

# Список установленных в проект модулей
INSTALLED_APPS = [
    # Модуль отвечающий за работу с панелью администратора
    'django.contrib.admin',
    # Модуль отвечающий за стандартную аутентификацию и модель User
    'django.contrib.auth',
    # Модуль отвечающий за работу с моделями
    'django.contrib.contenttypes',
    # Модуль отвечающий за работу с сессиями
    'django.contrib.sessions',
    # Модуль отвечающий за обработку и отображение сообщений
    'django.contrib.messages',
    # Модуль отвечающий за хранение статических файлов в проекте (CSS, JS, FONTS, IMAGES)
    'django.contrib.staticfiles',
    # Модуль отвечающий за главную страницу и аутентификацию
    'mainlk.apps.MainlkConfig',
    # Модуль отвечающий за отображение материалов для обучения и методических материалов
    'materialslk.apps.MaterialslkConfig',
    # Модуль отвечающий за отображение списков предподавателей и проводимых мероприятий
    'infolistlk.apps.InfolistlkConfig',
    # Модуль отвечающий за удаление медиа-файлов, при удалении данных из БД
    'django_cleanup',
]

# Список промежуточных слоев для обработки запросов и ответов
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Константа отвечающая за путь к главному файлу маршрутов
ROOT_URLCONF = 'kuzminolk.urls'

# Список отвечающий за обработку шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Константа отвечающая за путь к WSGI-конфигурацию
WSGI_APPLICATION = 'kuzminolk.wsgi.application'

# Словарь отвечающий за работу с базой данных
DATABASES = {
    'default': {
        'NAME': 'kuzminoschool',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'kuzmino45',
        'PASSWORD': 'kuzminoschool_45',
        'HOST': 'localhost',
    }
}

# Список валидаторов паролей
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Константа отвечающая за язык, который будет использоваться в отображение стандартных данных
LANGUAGE_CODE = 'ru-ru'
# Константа отвечающая за часовой пояс, который будет использоваться в отображнии стандартной даты или времени
TIME_ZONE = 'Europe/Moscow'
# Константа отвечающая за формат отображения даты или времени
USE_I18N = True
# Константа отвечающая за использование в дате и времени часового пояса
USE_TZ = True

# Путь вида URL к статическим файлам (CSS, JS, FONTS, IMAGES)
STATIC_URL = 'static/'
# Файловый путь к статическим файлам (CSS, JS, FONTS, IMAGES)
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, "static"),
]

# Стандартный тип поля первичного ключа
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# URL-адрес на который будет производиться переадресация, при аутентификации
LOGIN_REDIRECT_URL =  '/'
# URL-адрес на который будет производиться переадресация, при необходимости аутентификации
LOGIN_URL = '/login/'

# Путь вида URL к медиа-файлам
MEDIA_URL = '/media/'
# Файловый путь к медиа-файлам
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')