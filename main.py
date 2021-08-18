import base64
from fastapi.responses import FileResponse
from fastapi.middleware.gzip import GZipMiddleware

from fastapi import FastAPI

app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=1000)


def to_base64_str():
    file = open('example-pdf-base64.txt', 'r')
    base64str = 'data:application/pdf;base64,' + file.read()
    return base64str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/pdf/get-pdf")
def read_item():

    return FileResponse('pdf-test.pdf')
