NAME = quantum

MOUNT = ./files
DEST = /data

build:
	sudo docker build -t $(NAME) .

run:
	sudo docker run -it -v $(MOUNT):$(DEST) $(NAME)

clean:
	sudo docker system prune -af

all: build run

re : clean all
