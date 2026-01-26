CMD=docker compose


up: clean
	@$(CMD) --profile deploy up --build

test: clean
	@$(CMD) --profile test up --build

clean:
	@docker image prune -f