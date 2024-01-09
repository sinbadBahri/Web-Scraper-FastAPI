import fastapi as _fastapi
from fastapi import responses as _responses

app = _fastapi.FastAPI()

import services as _services


@app.get('/')
async def root():
    return {'message': 'Welcome to my meme api'}


@app.get('/programmer-memes')
def get_programmer_memes():
    image_path = _services.select_random_image("ProgrammerHumor")
    return _responses.FileResponse(image_path)


@app.post('/programmer-memes')
def create_programmer_meme(image: _fastapi.UploadFile = _fastapi.File(...)):
    file_path = _services.upload_images(
        directory_name='ProgrammerHumor', image=image
    )

    if file_path:
        return _responses.FileResponse(file_path)
    
    return _fastapi.HTTPException(
        status_code=409,detail="Incorrect File Type."
    )
