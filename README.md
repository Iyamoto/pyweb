# pyweb
Having fun with the bottle

## installation

    git clone https://github.com/Iyamoto/pyweb.git
    cd pyweb
    docker build -t iyamoto/pyweb:0.17 .
    docker run -d --name web -p 8080:8080 iyamoto/pyweb:0.17

## to read
* https://docs.docker.com/engine/reference/builder/
* https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/#the-dockerfile-instructions
* https://bottlepy.org/docs/dev/tutorial.html