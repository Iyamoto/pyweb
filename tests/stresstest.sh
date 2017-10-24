#!/usr/bin/env bash

git pull
docker build -t iyamoto/pyweb:test .
sleep 5
docker run -d --name pywebstresstest -p 8080:8080 iyamoto/pyweb:test
sleep 5
ab -n 5000 -v debug -c 10 http://127.0.0.1:8080/ping
docker rm -f pywebstresstest