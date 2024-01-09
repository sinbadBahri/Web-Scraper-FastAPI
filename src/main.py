from fastapi import FastAPI
from fastapi import responses as _responses

app = FastAPI()

import services as _services


@app.get('/')
async def root():
    return {'message': 'Welcome to my meme api'}


@app.get('/general-memes')
async def get_general_memes():
    image_path = _services.select_random_image("memes")
    return _responses.FileResponse(image_path)
