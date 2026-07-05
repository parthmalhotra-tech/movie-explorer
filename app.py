import uvicorn
import requests
from fastapi import FastAPI,Request
from fastapi.staticfiles import StaticFiles
from  fastapi.templating import Jinja2Templates 
from fastapi.responses import RedirectResponse
app=FastAPI()
templates=Jinja2Templates(directory="templates")
app.mount("/static",StaticFiles(directory="static"),name="static")
@app.get("/")
def start(req:Request):
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
        "movie": movie_list
    })
@app.get("/search")
def search(req:Request,movie_id:str):
     return RedirectResponse(url=f"/movie/{movie_id}")
@app.get("/movie/{movie_id}")
def movie_details(req:Request,movie_id :str):
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
@app.get("/signup")
def signup(req:Request):
     return templates.TemplateResponse(name="signup.html",request=req,)
@app.get("/profile")
def profile(req:Request):
     return templates.TemplateResponse(name="profile.html",request=req,)
if __name__=="__main__":
     uvicorn.run("app:app",host="127.0.0.1",port=8000,reload=True)