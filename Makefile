NAME = quantum
MOUNT = ./
DEST = /data

run:
	docker run -it -v $(MOUNT):$(DEST) $(NAME)
	
build:
	mkdir $(MOUNT)/tmp
	docker build -t $(NAME) .

all: build run

clean:
	rm -rf $(MOUNT)/tmp
	docker system prune -af

re : clean all
