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

.PHONY: run
run:
	@echo "Running in development mode"
	$(python) main.py

.PHONY: run_docker
run_docker:
	@echo "Running in docker mode"
	docker-compose up
