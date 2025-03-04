from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, oath2
from ..database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import func


router = APIRouter(
    prefix="/post",
    tags=["Posts"]
)

@router.get("/", response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oath2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
   
    # posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all() 
    # cursor.execute("""SELECT * FROM posts """)
    # posts = cursor.fetchall()
    posts = db.query(models.Post, func.count(models.Vote.post_id)).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oath2.get_current_user)):
    new_post = models.Post(owner_id=current_user.id, **post.dict())
    
    # cursor.execute("""INSERT INTO posts (title, content) VALUES (%s, %s) RETURNING *""", (posts.title, posts.content))
    # new_post = cursor.fetchone()
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/{id}", response_model=schemas.PostOut)
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oath2.get_current_user)):
    
    # post = db.query(models.Post).filter(models.Post.id == id).first()
    
    post = db.query(models.Post, func.count(models.Vote.post_id)).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with {id} was not found"} 
        
    return post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oath2.get_current_user)):
    # deleting a post is mainly trying to figure out which dictionary from my post array sould we delete.
    # first find the index with the required id in you array
    # my_posts.pop(index)
    post = db.query(models.Post).filter(models.Post.id == id)
    
    
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exis")
    post.delete(synchronize_session=False)
    db.commit()
    if post.owner_id != oauth2.get_current_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized to perfomed this action")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    # we send this because we dont want to send any data back since we deleted the code Response(status_code=status.HTTP_204_NO_CONTENT)
    

@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oath2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post_query == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exis")
    
    if post.owner_id != oauth2.get_current_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized to perfomed this action")
    
    post_query.update(post.dict(),synchronize_session=False)
    return post_query.first()