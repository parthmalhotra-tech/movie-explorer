import uvicorn
from fastapi import FastAPI,Request
from fastapi.staticfiles import StaticFiles
from  fastapi.templating import Jinja2Templates 
app=FastAPI()
templates=Jinja2Templates(directory="templates")
app.mount("/static",StaticFiles(directory="static"),name="static")
@app.get("/")
def start(req:Request):
     return templates.TemplateResponse(name="main_page.html",request=req,)
@app.get("/movie/{movie_id}")
def movie_details(req:Request,movie_id :str):
     return templates.TemplateResponse(name="movie_details.html",request=req,)
@app.get("/login")
def login(req:Request):
     return templates.TemplateResponse(name="login.html",request=req,)
@app.get("/signup")
def signup(req:Request):
     return templates.TemplateResponse(name="signup.html",request=req,)
@app.get("/profile")
def profile(req:Request):
     return templates.TemplateResponse(name="profile.html",request=req,)
if __name__=="__main__":
     uvicorn.run("app:app",host="127.0.0.1",port=8000,reload=True)