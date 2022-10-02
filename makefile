#makefile
install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall  dist/*.whl

lint:
	poetry run flake8 page_loader

pytest:
	poetry run pytest