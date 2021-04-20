
build-docker:
	docker build . -t gem5-dev

start-docker:
	docker run  -v $(PWD):/gem5-dev --workdir /gem5-dev -it gem5-dev fish 
