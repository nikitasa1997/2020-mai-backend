all: python

install:
	apt install build-essential curl gcc git libpq-dev libssl-dev nginx \
		postgresql-12 pycodestyle python3 python3-dev python3-pip python3-venv \
		python3-wheel -y

python:
	python3 -m venv .venv
	. .venv/bin/activate
	pip3 install -r requirements.txt

start-nginx:
	cp nginx/nginx.conf /etc/nginx
	cp -r static /var/www
	/etc/init.d/nginx stop
	/etc/init.d/nginx start

install-wrk:
	rm -fr wrk
	git clone https://github.com/wg/wrk.git wrk
	make -C wrk
	cp wrk/wrk /usr/local/bin
	rm -fr wrk
