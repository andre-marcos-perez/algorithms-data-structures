.PHONY: help
help: ## Show this help message
	@grep -h -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: format
format: ## Format code
	@isort structures --profile black
	@black structures

.PHONY: lint
lint: ## Lint code
	@flake8 structures --count --show-source --statistics --max-line-length 88

.PHONY: test
test: ## Run unit tests
	@python3 -m unittest discover -v -s structures/sequences -p "*_test.py"