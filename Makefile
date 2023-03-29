.DEFAULT_GOAL := help

# Set python
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

.PHONY: lint
lint: black isort flake

.PHONY: install
install:
	$(python) -m pip install -r requirements.txt

config.py:
	@echo TOKEN = 'ENTER THE TOKEN' > config.py

.PHONY: run
run: config.py
	@echo "Running in development mode"
	$(python) main.py

.PHONY: run_docker
run_docker: config.py
	@echo "Running in docker mode"
	docker build -t yousha_generate_qr_bot .
	docker run -p 8080:8080 yousha_generate_qr_bot

