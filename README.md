# PYWEB
PYWEB is a template for simple API backend based on Python Bottle framework. 

* Runs upon [Gunicorn WSGI HTTP Server](http://gunicorn.org/)
* Docker container configs included
* [Demo site](http://iyamoto.pythonanywhere.com/)
* Webhooks support

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
