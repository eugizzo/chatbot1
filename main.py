import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from fastapi.middleware.cors import CORSMiddleware
import schemas
origins = ["*"]
app =FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/static", StaticFiles(directory="static"), name="static")
templates=Jinja2Templates(directory="templetes")
@app.get("/")
def hello_word(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.get('/bases')
async def read_item(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@app.post("/predict")
async def predict(item: schemas.Item):
    response = get_response(item.message)
    message = {"answer": response}
    return message

if __name__ == "__main__":
    uvicorn.run(app)
