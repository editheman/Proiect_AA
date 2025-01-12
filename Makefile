PYTHON := python3

default: build

build: generate_data knapsack

generate_data:
	$(PYTHON) generate_data.py

knapsack:
	$(PYTHON) knapsack.py

clean:
	rm -rf knapsack_tests

.PHONY: default build generate_data knapsack clean
