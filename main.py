from fastapi import FastAPI, status, UploadFile
from utility import get_file
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.get('/')
def main():
    return {"message": "Welcome to Sentimental Detection Analysis"}

@app.post('/upload/filename')
async def upload_file_xlsx(file: UploadFile):
    try:
        # Call the utility function to process the uploaded file
        status_code, message = await get_file(file)
        return JSONResponse(status_code=status_code, content={"message": message})
    except Exception as e:
        # Handle exceptions and return an appropriate error message
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bad request")
