test: .venv
	pytest
test-watch: .venv
	pytest-watch

.venv:
	python -m venv .venv
	. .venv/bin/activate
	pip -q install -r requirements.prod.lock -r requirements.dev.lock
