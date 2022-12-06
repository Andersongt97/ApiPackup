#funcion cliente

def clienteEntity(item) -> dict:
    return{
        "id":str(item["_id"]),
        "cedula" : item["cedula"],
        "nombre" : item["nombre"],
        "telefono" : item["telefono"],
        "password": item["password"],
        "email" : item["email"],
        "ciudad" : item["ciudad"],
        "direccion" : item["direccion"],
    }
    
def clientesEntity(items) -> list:
    return [clienteEntity(item) for item in items]

#funcion destinatario

def destinatarioEntity(item) -> dict:
    return{
        "id":str(item["_id"]),
        "nombre" : item["nombre"],
        "direccion" : item["direccion"],
        "telefono" : item["telefono"],
        "pais" : item["pais"],
        "ciudad_pueblo" : item["ciudad_pueblo"],
    }
    
def destinatariosEntity(items) -> list:
    return [destinatarioEntity(item) for item in items]

#funcion factura

def facturaEntity(item) -> dict:
    return{
        "id":str(item["_id"]),
        "fecha" : item["fecha"],
        "envio_cantidad" : item["envio_cantidad"],
        "descripcion" : item["descripcion"],
        "precio_envio" : item["precio_envio"],
        "categoria" : item["categoria"],
    }
    
def facturasEntity(items) -> list:
    return [facturaEntity(item) for item in items]