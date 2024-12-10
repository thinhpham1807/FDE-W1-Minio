# Define default compose file (if needed)
COMPOSE_FILE = docker-compose.yml

# Start services in detached mode
up:
	docker-compose -f $(COMPOSE_FILE) up -d

# Stop and remove services
down:
	docker-compose -f $(COMPOSE_FILE) down

# Restart services
restart:
	docker-compose -f $(COMPOSE_FILE) down
	docker-compose -f $(COMPOSE_FILE) up -d

# View service logs
logs:
	docker-compose -f $(COMPOSE_FILE) logs -f
