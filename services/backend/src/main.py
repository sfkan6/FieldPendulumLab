from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from storing_data_samples import data_samples_router
from data_streaming import data_streaming_router
from charting import charting_router
import uvicorn


app = FastAPI()

origins = [
    'http://localhost:5000',
    'http://127.0.0.1:5000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(data_samples_router)
app.include_router(data_streaming_router)
app.include_router(charting_router)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
