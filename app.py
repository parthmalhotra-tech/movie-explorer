from fastapi import FastAPI,Request
import uvicorn
from  fastapi.templating import Jinja2Templates 
app=FastAPI()
templates=Jinja2Templates(directory="templates")
@app.get("/")
def start(req:Request):
     return templates.TemplateResponse(name="main_page.html",request=req,)
if __name__=="__main__":
     uvicorn.run("app:app",host="127.0.0.1",port=8000,reload=True)