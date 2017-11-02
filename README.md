# PYWEB
Python Bottle with Gunicorn/Gevent in Docker container.

## Installation and testing

### Docker based

    git clone https://github.com/Iyamoto/pyweb.git
    cd pyweb
    bash tests/buildimage.sh
    bash tests/stresstest.sh
    python3 tests/indockertests.py

## To read
* https://docs.docker.com/engine/reference/builder/
* https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/#the-dockerfile-instructions
* https://bottlepy.org/docs/dev/tutorial.html
* https://bottlepy.org/docs/dev/recipes.html
