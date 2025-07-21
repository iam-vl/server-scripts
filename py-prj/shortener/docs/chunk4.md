# User dash + email verification

Update `models.py`:

```py
def get_user_urls(user_id: str) -> list[dict]:
    conn = get_db_conn()
    with conn.cursor() as cur: 
        cur.execute(
            """
            SELECT id, original, created_at, expires_at FROM urls 
            WHERE user_id = %s ORDER BY created_at DESC;
            """,
            (user_id,)
        )
        columns = [desc[0] for desc in cur.description] # Get col names 
        return [dict(zip(columns, rows)) for row in cur.fetchall()]
```

Add the dash route to `app.py`:  
```py   
@app.route('dashboard')
@login_required
def dashboard(): 
    user_urls = models.get_user_urls(current_user.id)
    return render_template('dashboard.html', urls=user_urls)
```  
Add the link to index: 
```html
<p><a href="/dashboard">View Your Links</a></p>
```
Add the template: `dashboard.html`. 

```html
```