from fastapi import FastAPI

app = FastAPI(
    title="Matcha API",
    version="0.1.0",
)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Matcha API"}


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}