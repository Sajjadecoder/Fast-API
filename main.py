from fastapi import FastAPI
from routes import users,blogs,auth
app = FastAPI(title="Blogs(learning fastAPI)")
@app.get('/')
def health():
    return {'data': 'server running perfectly'}


app.include_router(users.router)
app.include_router(auth.router)
app.include_router(blogs.router)

