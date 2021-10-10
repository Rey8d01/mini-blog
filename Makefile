pip:
	python -m pip install pip -U
	python -m pip install -r requirements.txt -U

pip-dev:
	make pip
	python -m pip install -r requirements-dev.txt -U

lint:
	mypy --install-types --non-interactive .

test:
	pytest

prepare:
	make lint
	make test

serve:
	export FLASK_APP=main && \
	export FLASK_ENV=development && \
	flask run

gunicorn:
	gunicorn main:app -b 0.0.0.0:5000 -w 2 --log-level error --access-logfile - --max-requests 500

docker:
	docker build -t local/mini-blog:0.1.0 .
	docker volume create mini-blog-tmp
	docker run --rm -it -v mini-blog-tmp:/usr/src/app/tmp -p 5000:80 --name=mini-blog local/mini-blog:0.1.0
