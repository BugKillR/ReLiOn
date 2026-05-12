from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.mongodb import db
from app.routes.analyze import router as analyze_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analyze_router)

@app.get("/")
def root():
    return {"message": "ReLiOn API Running"}

@app.get("/test-db")
async def test_db():
    await db.test.insert_one({"message": "MongoDB works"})
    return {"status": "success"}