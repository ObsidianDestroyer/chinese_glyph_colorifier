import uvicorn

from glypher.app import make_application

if __name__ == '__main__':
    uvicorn.run(make_application(), port=8080)
