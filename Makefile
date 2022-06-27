install:
	pip install -r requirements.txt

test:
	pytest

report:
	pytest --cov=consent_user_information --cov-report=html tests

coverage:
	pytest --cov=consent_user_information tests

release:
	git tag -a $(shell python -c "from consent_user_information import __version__; print(__version__)") -m "$(m)"
	git push origin --tags
