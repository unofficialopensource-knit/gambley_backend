from fastapi import FastAPI


def create_app():
    app = FastAPI()

    @app.get("/health")
    def health():
        return {"status": "healthy"}

    return app
