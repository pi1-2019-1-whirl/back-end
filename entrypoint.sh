#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z whirl-db 5432; do
    sleep 0.1
done

echo "PostgreSQL started"

flask run -h 0.0.0.0