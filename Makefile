CMD=docker compose


up: clean
	@$(CMD) --profile deploy up --build

#test: clean
#	@$(CMD) up database_test -d
#	@$(CMD) up backend_test --build
#	@$(CMD) down database_test

clean:
	@docker image prune -f