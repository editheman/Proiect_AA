PYTHON := python3

default: build

build: generate_data knapsack

# Rule to generate data
generate_data:
	$(PYTHON) generate_data.py

# Rule to execute knapsack
knapsack:
	$(PYTHON) knapsack.py

# Rule to clean generated files
clean:
	rm -rf knapsack_tests

.PHONY: default build generate_data knapsack clean
