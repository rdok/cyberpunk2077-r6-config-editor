start: venv
	python3 --version

test: venv
	pytest

test-watch: venv
	ptw --poll

lint: venv
	flake8 src

venv: ~/.venv
	. ~/.venv/bin/activate

~/.venv:
	python3 -m venv ~/.venv

pip3-install:
	pip3 install -r requirements.lock

pip3-install-package: venv # package={name}
	pip3 install $(package) && pip3 freeze | grep $(package) >> requirements.lock

#     python -m pip install -r requirements-to-freeze.txt
