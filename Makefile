check:
	flake8 .
	mypy .
	python -m pytest --cov=flake8_cognitive_complexity --cov-report=xml
	mdl README.md
