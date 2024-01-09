from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Welcome to my meme api'}


@app.get('/general-memes')
async def method_name():
    pass
