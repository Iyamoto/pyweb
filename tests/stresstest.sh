#!/usr/bin/env bash

docker run -d --name pywebstresstest -p 8080:8080 iyamoto/pyweb:test
sleep 2
ab -n 10000 -v debug -c 100 http://127.0.0.1:8080/ping
docker rm -f pywebstresstest