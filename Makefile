PACKAGE_NAME=mytool
VENV_DIR=venv
PYTHON=$(VENV_DIR)/bin/python
PIP=$(VENV_DIR)/bin/pip

install:
	pip install -r requirements.txt
lint:
	pylint --disable=R,C src/mytool/*.py  test/test_mytool.py
format:
	black src/mytool/*.py  test/test_mytool.py
test:
	python -m pytest -vv test/test_mytool.py
package:
	pip install .


all: install lint format run
