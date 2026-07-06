from sqlalchemy.orm import Session
from models import User,Watchlist
def create(db:Session,model,data):
    obj=model(**data)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


