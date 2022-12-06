from fastapi import FastAPI
from routers.route import cliente, destinatario, factura
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="PACKUP",
    description="This is a App of mesage",
    version="1.0.0"
)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cliente)
app.include_router(destinatario)
app.include_router(factura)