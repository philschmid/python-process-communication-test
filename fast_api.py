from fastapi import FastAPI, Request, Response, Query
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


uvicorn.run(app, host="0.0.0.0")
