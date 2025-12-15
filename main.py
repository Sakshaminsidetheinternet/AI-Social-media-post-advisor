from fastapi import FastAPI , UploadFile, Form, File

app = FastAPI(title = 'AI Social media post advisor')

@app.post('/analyze')
async def analyzer(platform : str = Form(...), file : UploadFile = File(...) ):
    return{
        'status' : 'ok',
        'platform' : platform,
        'filename' : file.filename,



    }
