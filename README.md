# FastAPI Boilerplate

Dockerized [FastAPI](https://fastapi.tiangolo.com/) boilerplate for a quick environment setup with some (opinionated) sane defaults.

Build with:

* [Tortoise-ORM](https://tortoise-orm.readthedocs.io/en/latest/index.html) with [PostgreSQL](https://www.postgresql.org/)
* Migrations by [aerich](https://github.com/tortoise/aerich)
* User management by [FastAPI-users](https://frankie567.github.io/fastapi-users/)
* [Uvicorn](https://www.uvicorn.org/)

## Getting started

**1. Clone the repo**

```bash
$ git clone git@github.com:villeristi/fastapi-boilerplate.git
```

**2. Create the `.env`-file**

```bash
$ cp .env.example .env
```

**3. Start the containers**

```bash
$ docker-compose up -d
```

**4. Get to tha ~~choppa~~ container**

```bash
$ docker exec -it fabp_app
```

**5. Initialize base DB-schema**

```bash
$ aerich init-db # inside the container
```

**6. Create superuser**

```bash
$ ./bin/createsuperuser  # inside the container
```

**7. Logging**

Default logging is configured in `src/util/logger.py` and logs everything to `stdout`. To actually see what's going on in your application, just grab the logs from the container using

```bash
$ docker logs fabp_app -f
```

Uvicorn is watching the `src` directory by default and reloads application accordingly.

**8. Done!**

Now everything's set up and one can start building something useful!


## Migrations

1. Create migrations after initializing new models / changing existing models
```bash
aerich migrate # inside the container
```

2. Apply migrations
```bash
aerich upgrade  # inside the container
```

## TODO:
- [ ] Fake data
- [ ] Testing
- [ ] Production
