# api_final

## Описание:

REST API для проекта Yatube. 
Данный API могут использовать: любые прилоения взаимодействующие с API 
(серверы приложения, мобильные приложения телеграмм боты и другие.
Через данный API можно передавать и получать данные.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/JabbaS15/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source evenv/scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
cd yatube_api
```

```
python3 manage.py runserver
```
