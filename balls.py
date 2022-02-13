import uvicorn
from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI, Request
from fastapi.openapi.utils import get_openapi
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse,FileResponse,PlainTextResponse,RedirectResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI(redoc_url=None,docs_url=None)
app.mount("/static", StaticFiles(directory="static"), name="static")    
templates = Jinja2Templates(directory="templates")

@app.get("/",)
async def main():
  return "hello world"


uvicorn.run(app,host="0.0.0.0",port="8080")
