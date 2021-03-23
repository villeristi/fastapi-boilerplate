# FastAPI Boilerplate

FastAPI boileplate with sane defaults on:
* Foo
* Bar


## Getting started

1. Get to tha ~~choppa~~ container

```bash
docker exec -it fabp_app
```

2. Initialize base DB-schema
```bash
aerich init-db
```

3. Create superuser
```bash
docker exec -it fabp_app ./bin/createsuperuser
```

## Migrations

1. Create migrations after initializing new models / changing existing models
```bash
aerich migrate
```

2. Apply migrations
```bash
aerich upgrade
```

## TODO:
