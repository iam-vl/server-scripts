# Chunk 2: Delete links + Link expiry  


Migration - add delete token: 

```sql
ALTER TABLE urls ADD COLUMN delete_token TEXT;
```

Enable deletions and tokens: 

```py
def create_url(original_url: str) -> tuple[str, str]:
    pass 
    return "1", "1" # short id + delete token 
def delete_url(short_id: str, token:str) -> bool:
    pass
    return True # True if deleted, False if invalid 
```

Add / update the routes: 

```py 
@app.route('/', methods=['GET', 'POST'])
def home():
    pass 
@app.route('/delete/<short_id>/<token>')
def delete(short_id, token):
    pass
```