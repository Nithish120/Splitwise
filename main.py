from fastapi import FastAPI,HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.mount("/Images", StaticFiles(directory="Images"), name="Images")

@app.get("/")
async def main():
    return FileResponse("html/Splitwise.html")
@app.get("/New_group")  
async def new_group():
    return FileResponse("html/New_group.html")
@app.get("/Contact")
async def contact():
    return FileResponse("html/Contact.html")

# gand=[{'id':1,'name':'Alice'},{'id':2,'name':'Bob'},{'id':3,'name':'Charlie'}]

# @app.get("/")
# async def index():
#     return {"message": "Hello, World!"}
# @app.get("/about")
# def about():
#     return {"page": "about"}

# @app.get("/contact")
# def contact():
#     return {"page": "contact"}

# @app.get("/Gand")
# def Gand():
#     return gand
    
# @app.get("/Gand/{item_id}")

# async def Gand_id(item_id: int): #It is important to specify the type of item_id because Api needs it
#     if item_id<len(gand)-1:
#         return gand[item_id]
#     else:
#         raise HTTPException(status_code=404,detail='Band Not found')