NAME = quantum

MOUNT = ./files
DEST = /data

build:
	docker build -t $(NAME) .

run:
	docker run -it -v $(MOUNT):$(DEST) $(NAME)

clean:
	docker system prune -af

all: build run

re : clean all
