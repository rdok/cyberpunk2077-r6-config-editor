check: test lint format

format: pip
	black --check src
	black --check tests

format-fix: pip
	black src
	black tests

test: pip
	pytest

test-watch: pip
	pytest-watch --poll # https://github.com/joeyespo/pytest-watch/issues/9

lint: pip
	flake8 src
	flake8 tests

.PHONY: pip
pip:
	pip -q install -r requirements.prod.lock -r requirements.dev.lock

shell:
	docker-compose run --rm python