from fastapi import FastAPI
from app.api.routes import router
from app.config import settings

app = FastAPI(title="DeepSolv OA linkedin scrapper API")

app.include_router(router)

@app.on_event("startup")
async def startup_event():
    # add startup logic here dumbooo
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)