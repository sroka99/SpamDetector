FROM mariadb:latest

ENV MYSQL_ROOT_PASSWORD=root_password
ENV MYSQL_DATABASE=test_db
ENV MYSQL_USER=test_user
ENV MYSQL_PASSWORD=test_password

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 3306
