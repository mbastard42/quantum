NAME = quantum
MOUNT = ./files
DEST = /data

run:
	docker run -it -v $(MOUNT):$(DEST) $(NAME)
	
build:
	docker build -t $(NAME) .

clean:
	docker system prune -af

all: build run

re : clean all
