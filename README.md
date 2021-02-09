### Simple Python project as Example Python in Docker-Compose

Runs DB & python server with connection to DB
If all ok - you will see a print with Success message like 'Connected to PostgreSQL'.

DB settings stored as environment variables:

- DB_PASS
- DB_LOGIN
- DB_HOST
- DB_PORT
- DB_NAME

To test, what you can access server from localhost send get request to '/ping' endpoint, like:

http://0.0.0.0:8080/ping

Answer will be 'pong'.


### How to use


```bash

    git clone https://github.com/xnuinside/python-docker-sample.git
    cd python-docker-sample
    docker-compose up --build

```