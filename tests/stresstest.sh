#!/usr/bin/env bash

cd ..
git pull
docker build -t iyamoto/pyweb:test .
docker run -d --name pywebstresstest -p 8080:8080 iyamoto/pyweb:test
ab -n 5000 -v debug -c 10 http://127.0.0.1:8080/ping
docker rm -f pywebstresstest