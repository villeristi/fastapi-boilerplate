FROM python:3.8-slim

LABEL maintainer="Wille <villeristimaki@gmail.com>"

ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED 1

RUN addgroup --system fastapi \
    && adduser --system --ingroup fastapi fastapi

COPY ./requirements /requirements

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /requirements/base.txt \
    && rm -rf /requirements

COPY --chown=fastapi:fastapi app /app

USER fastapi

WORKDIR /app

EXPOSE 80
