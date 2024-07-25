FROM postgres:latest

WORKDIR /
COPY ./init/init.sql /docker-entrypoint-initdb.d

ENV POSTGRES_DB="db"
ENV POSTGRES_USER="dbuser"
ENV POSTGRES_PASSWORD="dbpassword"
ENV PGDATA="/var/lib/postgresql/data/pgdata"

VOLUME [ "/var/lib/postgresql/data" ]