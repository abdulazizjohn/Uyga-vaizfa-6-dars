from typing import Annotated
from fastapi import FastAPI,Body, File
from pydantic import Field
import uvicorn

app = FastAPI(title="Users Project")

users = [
    {"id": 1, "name": "Ali", "manzil": "Fergana"},
    {"id": 2, "name": "Vali", "manzil": "Buxara"},
    {"id": 3, "name": "Eshmat", "manzil": "Toshkent"},
    {"id": 4, "name": "Hoshim", "manzil": "Namangan"},
    {"id": 5, "name": "Olim", "manzil": "Quva"},
    {"id": 6, "name": "Guli", "manzil": "Samarqand"}
]



@app.get("/")
def hello():
    return {"message": "Hello world!"}

@app.get("/users/") 
def read_users() -> list[dict]: 
    return users




@app.get("/users/{user_id}")
def read_user(user_id: int) -> dict:
    for user in users:
        if user.get("id") == user_id:
            return user



@app.get("/users/manzil/{manzil}")
def read_user_manzil(manzil: str):
    for user in users:
        if user["manzil"].lower() == manzil.lower():
            return user
    

@app.post("/users/")
def create_user(name: Annotated[str, Field(max_length=150)] =  Body(),
                manzil: Annotated[str, Field(max_length=150)] = Body()) -> dict:
    
    users.append(
        {
            "id":len(users) + 1,
            "name": name,
            "manzil": manzil
        }
    )
    return {"message":"User created successful!"}






# Qoshimcha yuqori bal uchun  
@app.delete("/users/{user_id}")
def delete_user(user_id: int) -> dict:
    for user in users:
        if user.get("id") == user_id:
            users.remove(user)
            return {"message":"User delete successful!"}




if __name__ == "__main__":
    uvicorn.run(app,port=8001)


