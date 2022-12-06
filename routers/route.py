from fastapi import APIRouter,Response,status
from config.db import conn
from schemas.user import  clienteEntity, clientesEntity, destinatarioEntity, destinatariosEntity,facturaEntity,facturasEntity
from models.modelos import Cliente, Destinatario, Factura
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

#documentacion Cliente

cliente = APIRouter()

@cliente.get('/clientes', response_model=list[Cliente], tags= ["Clientes"])
def find_all_Clientes():
    return clientesEntity(conn.mensajeria.Clientes.find())

@cliente.post('/clientes', response_model=Cliente, tags= ["Clientes"])
def create_cliente(cliente: Cliente):
    new_cliente = dict(cliente)
    del new_cliente["id"]
    
    id = conn.mensajeria.Clientes.insert_one(new_cliente).inserted_id
    cliente = conn.mensajeria.Clientes.find_one({"_id": id})
    return clienteEntity(cliente)

@cliente.get('/clientes/{id}', response_model=Cliente, tags= ["Clientes"])
def find_cliente(id:str):
    return clienteEntity(conn.mensajeria.Clientes.find_one({"_id": ObjectId(id)}))

@cliente.get("/clientes/login/{usuario}/{clave}")
def login(usuario:str,clave:str):
    usuario = conn.mensajeria.Clientes.find_one({"nombre": usuario, "password": clave})
    if usuario:
        return clienteEntity(usuario)
    else:
        return Response(status_code=HTTP_404_NOT_FOUND)

@cliente.put('/clientes/{id}', response_model=Cliente, tags= ["Clientes"])
def update_cliente(id: str, cliente: Cliente):
    cliente_= dict(cliente)
    cliente_update={} 
    for key in cliente_:
        if cliente_[key] != None:
            cliente_update[key]= cliente_[key]
            
    conn.mensajeria.Clientes.find_one_and_update({"_id": ObjectId(id)}, {"$set": cliente_update})
    return clienteEntity(conn.mensajeria.Clientes.find_one({"_id": ObjectId(id)}))

@cliente.delete('/clientes/{id}', status_code=status.HTTP_204_NO_CONTENT, tags= ["Clientes"])
def delete_cliente(id: str):
    clienteEntity(conn.mensajeria.Clientes.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)

#documentacion destinatarios

destinatario = APIRouter()

@destinatario.get('/destinatarios', response_model=list[Destinatario], tags= ["Destinatarios"])
def find_all_destinatarios():
    return destinatariosEntity(conn.mensajeria.Destinatarios.find())

@destinatario.post('/destinatarios', response_model=Destinatario, tags= ["Destinatarios"])
def create_Destinatario(destinatario: Destinatario):
    new_destinatario = dict(destinatario)
    del new_destinatario["id"]
    
    id = conn.mensajeria.Destinatarios.insert_one(new_destinatario).inserted_id
    destinatario = conn.mensajeria.Destinatarios.find_one({"_id": id})
    return destinatarioEntity(destinatario)

@destinatario.get('/destinatarios/{id}', response_model=Destinatario, tags= ["Destinatarios"])
def find_destinatario(id:str):
    return destinatarioEntity(conn.mensajeria.Destinatarios.find_one({"_id": ObjectId(id)}))

@destinatario.put('/destinatarios/{id}', response_model=Destinatario, tags= ["Destinatarios"])
def update_destinatario(id: str, destinatario: Destinatario):
    destinatario_= dict(destinatario)
    destinatario_update={} 
    for key in destinatario_:
        if destinatario_[key] != None:
            destinatario_update[key]= destinatario_[key]
            
    conn.mensajeria.Destinatarios.find_one_and_update({"_id": ObjectId(id)}, {"$set": destinatario_update})
    return destinatarioEntity(conn.mensajeria.Destinatarios.find_one({"_id": ObjectId(id)}))

@destinatario.delete('/destinatarios/{id}', status_code=status.HTTP_204_NO_CONTENT, tags= ["Destinatarios"])
def delete_destinatario(id: str):
    destinatarioEntity(conn.mensajeria.Destinatarios.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)

#documentacion facturacion

factura = APIRouter()

@factura.get('/facturas', response_model=list[Factura], tags= ["Facturas"])
def find_all_facturas():
    return facturasEntity(conn.mensajeria.Facturas.find())

@factura.post('/facturas', response_model=Factura, tags= ["Facturas"])
def create_Factura(factura: Factura):
    new_factura = dict(factura)
    del new_factura["id"]
    id = conn.mensajeria.Facturas.insert_one(new_factura).inserted_id
    factura = conn.mensajeria.Facturas.find_one({"_id": id})
    return facturaEntity(factura)

@factura.get('/facturas/{id}', response_model=Factura, tags= ["Facturas"])
def find_factura(id:str):
    return facturaEntity(conn.mensajeria.Facturas.find_one({"_id": ObjectId(id)}))

@factura.put('/facturas/{id}', response_model=Factura, tags= ["Facturas"])
def update_factura(id: str, factura: Factura):
    factura_= dict(factura)
    factura_update={} 
    for key in factura_:
        if factura_[key] != None:
            factura_update[key]= factura_[key]
            
    conn.mensajeria.Facturas.find_one_and_update({"_id": ObjectId(id)}, {"$set": factura_update})
    return facturaEntity(conn.mensajeria.Facturas.find_one({"_id": ObjectId(id)}))

@factura.delete('/facturas/{id}', status_code=status.HTTP_204_NO_CONTENT, tags= ["Facturas"])
def delete_factura(id: str):
    facturaEntity(conn.mensajeria.Facturas.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)
