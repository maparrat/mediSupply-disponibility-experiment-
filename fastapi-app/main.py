import os
from fastapi import FastAPI, Response, status

app = FastAPI()
# La app lee la variable de entorno SIMULATE_ERROR al inicio.
SIMULATE_ERROR = os.environ.get("SIMULATE_ERROR", "false").lower() in ("1","true","yes")

@app.get("/")
def root():
    # Respuesta normal (200) aunque SIMULATE_ERROR sea true,
    # el healthcheck fallará cuando corresponda.
    return {"message": "hello from fastapi", "simulate_error": SIMULATE_ERROR}

@app.get("/health")
def health():
    # Si la variable indica fallo, devolvemos 500 para que el healthcheck
    # marque la instancia como UNHEALTHY.
    if SIMULATE_ERROR:
        return Response(content="unhealthy", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return {"status": "ok"}
