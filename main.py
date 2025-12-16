from fastapi import FastAPI , UploadFile, Form, File
import cv2
import numpy as np
from analyzer.quality import quality_checker, brightness_check
app = FastAPI(title = 'AI Social media post advisor')

@app.post('/analyze')
async def analyzer(platform : str = Form(...), file : UploadFile = File(...) ):
    contents = await file.read()
    np_img = np.frombuffer(contents, np.uint8)
    cv_img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
    is_clear , brightness_score = quality_checker(cv_img)
    exposure = brightness_check(cv_img)
    
    return{
        'platform' : platform,
        'analysis' : {
            'blur_score' : brightness_score,
            'is_cleae' : is_clear,
            'brightness' : exposure
        },
        'filename' : file.filename,



    }
