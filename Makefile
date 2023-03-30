.DEFAULT_GOAL := help

# Set python
export PYTHONPATH=.
python = python

.PHONY: help
help:
	@echo "USAGE"
	@echo "  make <commands>"
	@echo ""
	@echo "AVAILABLE COMMANDS"
	@echo "  run		Start the bot"
	@echo "  install 	Install the dependencies"
	@echo "  run_docker	Start the bot in a docker container"
	@echo "	 start_service 	Start linux service"
	@echo "  flake		Run flake8"
	@echo "  black		Run black"
	@echo "  isort		Run isort"
	@echo "  lint		Reformat code"


# ================================================================================================
# Commands
# ================================================================================================

.PHONY:	black
black:
	$(python) -m black .

.PHONY: isort
isort:
	$(python) -m isort .

.PHONY: flake
flake:
	$(python) -m flake8 .

.PHONY: bandit
bandit:
	$(python) -m bandit -r src --severity=medium

.PHONY: pylint
pylint:
	$(python) -m pylint src

.PHONY: lint
lint: black isort flake bandit pylint

.PHONY: install
install:
	$(python) -m pip install -r requirements.txt

src/config.py:
	@echo TOKEN = 'ENTER THE TOKEN' > src/config.py

.PHONY: run
run: src/config.py
	@echo "Running in development mode"
	$(python) src/main.py

.PHONY: run_docker
run_docker: src/config.py
	@echo "Running in docker mode"
	docker build -t yousha_generate_qr_bot .
	docker run -p 8080:8080 yousha_generate_qr_bot

.PHONY: start_service
start_service: src/config.py
	@echo "Starting docker container in autoreboot mode"
	bash start_service.sh
