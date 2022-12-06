from datetime import datetime
from typing import Optional
from pydantic import BaseModel
  
class Cliente(BaseModel):
    
    id : Optional[str]
    cedula : Optional[int]
    nombre : Optional[str]
    password : Optional[str]
    telefono : Optional[int]
    email : Optional[str]
    ciudad : Optional[str]
    direccion : Optional[str]
    
class Destinatario(BaseModel):
    id : Optional[str]
    nombre : Optional[str]
    direccion : Optional[str]
    telefono : Optional[int]
    pais : Optional[str]
    ciudad_pueblo : Optional[str]

class Factura(BaseModel):
    id : Optional[str]
    fecha : Optional[str]
    envio_cantidad : Optional[int]
    descripcion : Optional[str]
    precio_envio : Optional[float]
    categoria : Optional[str]
    
   


    
