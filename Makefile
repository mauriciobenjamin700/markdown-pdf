lint:
	ruff check src/
	black src/ --check
	flake8 src/
	isort src/ --check-only

lint-fix:
	ruff check src/ --fix --unsafe-fixes
	black src/
	isort src/