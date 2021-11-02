APP_VERSION = 1.0.3
APP_NAME    = ppeppi

#################### DOCKER TASKS ####################
## Build the container
setup: 
	@docker build -t $(APP_NAME):v$(APP_VERSION) .


## Run the container
run: 
	@docker run -dit --rm -p 1000:1000 --name $(APP_NAME) $(APP_NAME):v$(APP_VERSION)

## Output the current version
version: 
	@echo $(APP_VERSION)
