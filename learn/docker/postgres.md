# Postgres on Docker 

```sh 
docker run --name my-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres
```
where:  
* `-name`: Assigns a custom name to your container
* `-e POSTGRES_PASSWORD=your_password`: Set the PostgreSQL root password to your_password.
* `-p 5432:5432`: Map port 5432 on the host machine to port 5432 on the container, allowing you to connect to the database from your host.
* `-d`: Run the container in detached mode (in the background)
* `postgres`: Specifies the PostgreSQL Docker image to use.

Enter the container shell: 
```
docker exec -it postgres1 psql -U postgres
```
Create a test db: 
```sql
CREATE DATABASE testdb001;
\l               -- List databases
\c testdb001        -- Connect to a DB
CREATE TABLE users (id SERIAL, name VARCHAR(30));
INSERT INTO users (name) VALUES ('Alice');
SELECT * FROM users;
```

How to run migrations: 

1. First, Ensure Your Docker Container is Running  
```bash
docker run --name my-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres
```
2. Copy the migrations.sql File into the Container  
```bash
docker cp migrations.sql my-postgres:/migrations.sql
```
3. Execute the Migration Inside the Container  
```bash
docker exec -it my-postgres psql -U postgres -d postgres -f /migrations.sql
```
