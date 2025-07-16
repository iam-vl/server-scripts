# PLAN: URL Shortener with Python & Flask 

## Learn more



## Initial planning 

Shortener is a learning project that will produce a URL shortener. Initial requirements: 

1. Can log in with Google, can sign in/sign up with email 
2. Can keep browser sessions for 30 days since previous visit 
3. Both logged-in users and not logged-in visitors can create shortened links 
4. The site produces a delete link upon generating a shortened link 
5. Registered users can also delete the shortened links from their account 
6. Links by unregistered users expire after 45 days inactivity (if not clicked for 30 days)
7. Links by registered users expire after 90 days inactivity. 


Details:  
* Stack: Python 3.10+, Flask, PostgreSQL (Docker), HTML/CSS  
* Design: Fewer files, session-based, works on Win11/Ubuntu  

## Project Structure (plan)  

Files to build (prliminary plan): 
```
/urlshortener  
├── app.py          # Flask app + routes  
├── models.py       # DB models & queries  
├── auth.py         # Google + email auth  
├── templates/      # Jinja2 HTML  
│   ├── index.html  # Shorten form  
│   └── dashboard.html  
└── migrations.sql  # DB schema  
```

## Planned steps 

Let's break the project in chunks: 

1. Basic shortener: Anonymous users create short links.
2. Delete Links + Expiry  
3. Authorization: Email signup + Google OAuth
4. User Dashboard  
5. Deployment   

Possible enhancements:  
* Rate limiting 
* QR code endpoint 
* Export links to CSV 

## Technical info   

> **INFO**  
> How to enter the Docker postgresql shell:  
> `docker exec -it postgres1 psql -U postgres`  
> How to create db s on Docker:  
> `docker exec -it postgres1 psql -U postgres -c "CREATE DATABASE pgr_shortener;"`  
> Ноw to run the migrations on Docker: 
> 1. Copy the migrations file into the container:  
> `docker cp migrations.sql postgres1:/migration.sql` 
> 2. Execute the migrations inside the container: 
> `docker exec -it psql -U postgres -d pgr_shortener -f /migrations.sql`