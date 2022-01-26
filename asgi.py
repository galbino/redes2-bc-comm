from app import create_app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:create_app", host="0.0.0.0", port=8080, reload=True, factory=True, workers=1)
else:
    g_app = create_app()
