FROM tiangolo/uvicorn-gunicorn:python3.8

ENV PYTHONUNBUFFERED 1

RUN addgroup --system fastapi \
    && adduser --system --ingroup fastapi fastapi

COPY ./requirements /requirements

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /requirements/base.txt \
    && rm -rf /requirements

COPY --chown=fastapi:fastapi ./src /app/src

USER fastapi

WORKDIR /app
