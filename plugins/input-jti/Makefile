PWD=$(shell pwd)

all: build start

build:
	docker build --rm -t local/input-jti .
start:
	docker run --rm -ti \
		-v $(PWD)/fluent.conf:/fluentd/fluent.conf \
	        -e PORT_JTI=3000 \
	        -e OUTPUT_STDOUT=false \
	        -e OUTPUT_PROMETHEUS=true \
		-p 3000:3000/udp \
		-p 24231:24231 \
                --name input-jti \
                local/input-jti		

stop:
	docker stop input-jti

shell:
	docker exec -ti input-jti bash

start-dev:
	docker run --rm -ti \
		-v $(PWD)/fluent.conf:/fluentd/fluent.conf \
	        -e PORT_JTI=3000 \
	        -e OUTPUT_STDOUT=true \
	        -e OUTPUT_PROMETHEUS=false \
		-p 3000:3000/udp \
		-p 24231:24231 \
                --name input-jti-dev \
                local/input-jti bash

stop-dev:
	docker stop input-jti-dev

shell-dev:
	docker exec -ti input-jti-dev bash
