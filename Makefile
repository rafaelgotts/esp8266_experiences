.PHONY: help

help:  ## This help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install:  ## Install project requirements
	pip install -r requirements.txt

run-file:  ## Run <file> on board
	ampy --port /dev/ttyUSB0 run $(file)

shell-board:  ## Run screen to acess python inside the board
	bash scripts/maintenance/access_serial.sh