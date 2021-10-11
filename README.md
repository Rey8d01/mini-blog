# mini-blog

[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
![Test workflow](https://github.com/Rey8d01/mini-blog/actions/workflows/test.yml/badge.svg)

Минибложик, без авторизации, для ведения своих заметок.

## REST API

- GET /api/blog/posts - Список постов в блоге.
- GET /api/blog/posts?page=1&page_size=10 - Список постов в блоге c настройкой постраничной навигации.
- POST /api/blog/create-post - Добавление нового поста в блог.
- GET /api/blog/{{ alias }} - Вернет неудаленный пост в блоге по его псевдониму.
- PUT /api/blog/{{ alias }} - Обновление существующего поста в блоге.
- DELETE /api/blog/{{ alias }} - Удаление поста в блоге.

## Запуск

См. детали команд запуска в Makefile.

Перед первым запуском нужно произвести установку БД и заполнения ее начальными данными.
Для этого, а так же для генерации openapi.json выполнить команду

> make -f Makefile startup

Запуск тестов и линтеров

> make -f Makefile prepare

Запуск локального сервера **Flask** на порту 5000 в режиме отладки

> make -f Makefile serve

Запуск сервера **gunicorn** на порту 5000

> make -f Makefile gunicorn

### Docker

Локальная сборка и запуск с пробросом портов и передачей настроек через переменные окружения.

> docker build -t local/mini-blog:0.1.0 .
> 
> docker volume create mini-blog-tmp
> 
> docker run --rm -it -v mini-blog-tmp:/usr/src/app/tmp -p 5000:80 --env FLASK_DEBUG=0 --name=mini-blog local/mini-blog:0.1.0
