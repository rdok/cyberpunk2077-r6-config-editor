check: test lint

test: .venv
	pytest

test-watch: .venv
	pytest-watch --poll

lint: .venv
	flake8 src
	flake8 tests

.venv:
	python -m venv .venv
	. .venv/bin/activate
	pip -q install -r requirements.prod.lock -r requirements.dev.lock

shell:
	docker-compose run --rm python