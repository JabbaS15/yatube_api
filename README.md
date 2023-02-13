# RESTful API для проекта Yatube - Социальная сеть для блогеров.
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=013220)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=ffffff&color=013220)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=ffffff&color=013220)](https://www.django-rest-framework.org/)
[![JWT](https://img.shields.io/badge/-JWT-464646?style=flat&color=013220)](https://jwt.io/)

## Описание проекта:
Данный API могут использовать: любые прилоения взаимодействующие с API, серверы приложения, мобильные приложения телеграмм боты и другие.
Через данный API можно передавать и получать данные.
Сервис для блогеров, позволяет пользователям публикацию постов с изображениями, распределение постов по группам, имеются личные страницы пользователей со стеной, подписка на авторов и комментирование записей.

## Работа с API:

### Доступные запросы:
| Запрос | Эндпоинт | Метод |
|--------|:---------|-------|
| Получение всех постов | `.../api/v1/posts/` | GET |
| Редактирование поста | `.../api/v1/posts/{id}/` | PUT |
| Добавление комментария | `.../api/v1/posts/{post_id}/comments/` | POST |
| Получение подписок пользователя | `.../api/v1/follow/` | GET |
| Получение списка групп | `.../api/v1/groups/` | GET |

> Пример запроса:  
> _**GET /api/v1/posts/**_
>```JSON
>{
>  "count": 123,
>  "next": "http://api.example.org/accounts/?offset=400&limit=100",
>  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
>  "results": [
>    {}
>   ]
>}
>```

> Пример запроса:  
> _**POST /api/v1/posts/**_
>```JSON
>{
> "text": "string",
> "image": "string",
> "group": 0
>}
>```
>Пример ответа (200):
>```JSON
>{
> "id": 0,
> "author": "string",
> "text": "string",
>"pub_date": "2019-08-24T14:15:22Z",
> "image": "string",
> "group": 0
>}
>```

> Пример запроса:  
> _**GET /api/v1/follow/**_
>```JSON
>[
>  {
>    "user": "string",
>    "following": "string"
>  }
>]
>```

> Пример запроса:  
> _**POST /api/v1/follow/**_
>```JSON
>{
>  "following": "string"
>}
>```
> Пример ответа (200):
>```JSON
>{
>  "user": "string",
>  "following": "string"
>}
>```

## Инструкция по развёртыванию:
1. Загрузите проект:
```
git clone https://github.com/JabbaS15/yatube_api.git
```
2. Установите и активируйте виртуальное окружение:
```bash
python -m venv venv
source venv/Scripts/activate
python3 -m pip install --upgrade pip
```
3. Установите зависимости:
```bash
pip install -r requirements.txt
```
4. Выполнить миграции:
```bash
python manage.py migrate
```
5. В папке с файлом manage.py выполните команду запуска:
```bash
python3 manage.py runserver
```

### Автор проекта:
[Шведков Роман](https://github.com/JabbaS15)
