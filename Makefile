install:
	pip install -r requirements.txt

test:
	pytest

report:
	pytest --cov=consent_user_information --cov-report=html tests

coverage:
	pytest --cov=consent_user_information tests
