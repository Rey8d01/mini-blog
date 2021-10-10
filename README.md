# mini-blog

[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
![Test workflow](https://github.com/Rey8d01/mini-blog/actions/workflows/test.yml/badge.svg)

Минибложик, без авторизации, для ведения своих заметок.

## Запуск

См. детали команд запуска в Makefile.

Запуск локального сервера **Flask** на порту 5000

> make -f Makefile serve

Запуск сервера **gunicorn** на порту 5000

> make -f Makefile gunicorn

### Docker

Локальная сборка и запуск.

> docker build -t local/mini-blog:0.1.0 .
> 
> docker volume create mini-blog-tmp
> 
> docker run --rm -it -v mini-blog-tmp:/usr/src/app/tmp -p 5000:80 --name=mini-blog local/mini-blog:0.1.0
