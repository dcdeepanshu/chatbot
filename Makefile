.PHONY: clean test lint

TEST_PATH=./

help:
	@echo "    run-actions"
	@echo "        Run the action server."
	@echo "    train-nlu"
	@echo "        Train the natural language understanding using Rasa NLU."
	@echo "    train-core"
	@echo "        Train a dialogue model using Rasa core."
	@echo "    run-bot"
	@echo "        Starts the bot on the command line"
	@echo "    visualize"
	@echo "        Saves the story graphs into a file"

run-actions:
	python -m rasa_core_sdk.endpoint --actions actions  

train-nlu:
	python -m rasa_nlu.train -c config_spacy.json --fixed_model_name current --data data/nlu/ -o models --project nlu --verbose
	
train-core:
	python -m rasa_core.train -d domain.yml -s data/core -c policy.yml -o models/dialogue/


run-bot:
	python -m rasa_core.run --enable_api -d models/dialogue -u models/nlu/current --debug --endpoints endpoints.yml --cors "*"


visualize:
	python -m rasa_core.visualize -d domain.yml -s data/core/stories.md -o graph.png


