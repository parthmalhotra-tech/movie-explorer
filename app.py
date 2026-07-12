import uvicorn,requests
from models import User,Watchlist
from database import Base,engine,sessionlocal
from crud import create
from fastapi import FastAPI,Request,Form
from fastapi.staticfiles import StaticFiles
from  fastapi.templating import Jinja2Templates 
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware

app=FastAPI()

templates=Jinja2Templates(directory="templates")

app.mount("/static",StaticFiles(directory="static"),name="static")

Base.metadata.create_all(bind=engine)

db=sessionlocal()

app.add_middleware(SessionMiddleware,secret_key="this is my key for movie_explorer")

@app.get("/")
def start(req:Request):
    user_id=req.session.get("user_id")
    username=req.session.get("username")
    logged_in=False
    if user_id:
         logged_in=True
    movies = [
    "Sultan",
    "3 Idiots",
    "Dangal",
    "PK",
    "Shershaah",
    "Bajrangi Bhaijaan",
    "War",
    "Pathaan",
    "Jawan",
    "Animal",
    "Drishyam",
    "Bhool Bhulaiyaa",
    "Chhichhore",
    "Kabir Singh",
    "Zindagi Na Milegi Dobara"]
    movie_list = []
    for title in movies:
           response = requests.get(f"http://www.omdbapi.com/?apikey=904d2141&t={title}")
           movie_list.append(response.json())
    return templates.TemplateResponse("main_page.html", {
        "request": req,
        "movie": movie_list,
        "logged_in":logged_in,
        "username":username,
    })

@app.get("/search")
def search(req:Request,movie_id:str):
     return RedirectResponse(url=f"/movie/{movie_id}")

@app.get("/movie/{movie_id}")
def movie_details(req:Request,movie_id :str):
    movie_id.capitalize()
    url = f"https://www.omdbapi.com/?apikey=904d2141&t={movie_id}"
    response = requests.get(url)
    movie = response.json()
    if movie["Response"]=="False":
         return templates.TemplateResponse("movie_not_found.html",
                                           {"request":req,
                                           "movie_id":movie_id})
    return templates.TemplateResponse("movie_details.html",
                                      {"request":req,
                                       "movie_id":movie_id,
                                       "movie_title":movie["Title"],
                                       "movie_poster":movie["Poster"],
                                       "movie_imdb_rating":movie["imdbRating"],
                                       "movie_year":movie["Year"],
                                       "genre":movie["Genre"],
                                       "runtime":movie["Runtime"],
                                       "director":movie["Director"],
                                       "actors":movie["Actors"],
                                       "country":movie["Country"],
                                       "language":movie["Language"],
                                       "plot":movie["Plot"]})

@app.get("/login")
def login(req:Request):
     return templates.TemplateResponse(name="login.html",request=req,)
@app.post("/login")
def login_info(req:Request,email : str = Form(...),password : str = Form(...)):
     user=db.query(User).filter(User.email== email).first()
     if user is None:
          return templates.TemplateResponse("login.html",
                                                 {"request":req,
                                                  "error1":"email doesn't exist"})
     else:
          if password==user.password:
               req.session["user_id"]=user.id
               req.session["username"]=user.username
               return RedirectResponse(url="/",status_code=303)
          else:
               return templates.TemplateResponse("login.html",
                                                 {"request":req,
                                                  "error":"wrong password"})
@app.get("/signup")
def signup(req:Request):
     return templates.TemplateResponse(name="signup.html",request=req)
@app.post("/signup")
def signup_info(req:Request,
                email : str = Form(...),
                password : str = Form(...),
                confirm_password : str = Form(...),
                username : str = Form(...)):
     
     signup_details={"username":username,"email":email,"password":password}
     create(db,User,signup_details)
     return RedirectResponse(url="/",status_code=303)

@app.get("/profile")
def profile(req:Request):
     user_id=req.session.get("user_id")
     username=req.session.get("username")
     return templates.TemplateResponse("profile.html",
                                       {"request":req,
                                        "username":username})
@app.get("/logout")
def logout(req:Request):
     req.session.clear()
     return RedirectResponse(url="/",status_code=303)
@app.post("/movie/{movie_id}")
def add_watchlist(req:Request,movie_id:str):
    user_id=req.session.get("user_id")
    username=req.session.get("username")
    if user_id is None:
         return RedirectResponse(url="/login",status_code=303)
    movie_id.capitalize()
    url = f"https://www.omdbapi.com/?apikey=904d2141&t={movie_id}"
    response = requests.get(url)
    movie = response.json()
    data={"user_id":user_id,"imdb_id":movie["imdbID"],"title":movie["Title"],"poster":movie["Poster"]}
    create(db,Watchlist,data)
    return RedirectResponse(url="/",status_code=303)

@app.get("/watchlist")
def watchlist(req:Request):
     user_id=req.session.get("user_id")
     if user_id is None:
          return {"please login first"}
     else:
          movie=db.query(Watchlist).filter(Watchlist.user_id==user_id).all()
                 
          return templates.TemplateResponse("watchlist.html",{"request":req,"movie":movie})

if __name__=="__main__":
     uvicorn.run("app:app",host="127.0.0.1",port=8000,reload=True)