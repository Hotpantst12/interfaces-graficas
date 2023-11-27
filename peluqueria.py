class Cliente:
    def __init__(self, id, nombre, telefono, direccion):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.servicios_realizados = []
        self.productos_comprados = []
    def agregar_servicio(self, servicio):
        self.servicios_realizados.append(servicio)

    def comprar_producto(self, producto):
        self.productos_comprados.append(producto)   


class Servicio:
    def __init__(self, nombre, descripcion, duracion, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.duracion = duracion
        self.precio = precio


class Peluquero:
    def __init__(self, id, nombre, especializacion):
        self.id = id
        self.nombre = nombre
        self.especializacion = especializacion

class ProductoBelleza:
    def __init__(self, id, nombre, descripcion, precio):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

# Crear algunos servicios y productos constantes
servicios = [Servicio("Corte de pelo", "Un corte de pelo básico", 30, 15.0),
             Servicio("Coloración", "Coloración del cabello", 60, 30.0)]

productos = [ProductoBelleza(1, "Champú", "Champú para todo tipo de cabello", 10.0),
             ProductoBelleza(2, "Acondicionador", "Acondicionador para todo tipo de cabello", 10.0)]

# Solicitar datos del cliente
id_cliente = input("Introduce el ID del cliente: ")
nombre_cliente = input("Introduce el nombre del cliente: ")
telefono_cliente = input("Introduce el teléfono del cliente: ")
direccion_cliente = input("Introduce la dirección del cliente: ")

cliente = Cliente(id_cliente, nombre_cliente, telefono_cliente, direccion_cliente)

def generar_factura(cliente):
    print(f"Factura para el cliente {cliente.nombre} (ID: {cliente.id})")
    print(f"Dirección: {cliente.direccion}")
    print(f"Teléfono: {cliente.telefono}")
    print("\nServicios realizados:")
    for servicio in cliente.servicios_realizados:
        print(f"- {servicio.nombre} ({servicio.descripcion}): {servicio.precio}€")
    print("\nProductos comprados:")
    for producto in cliente.productos_comprados:
        print(f"- {producto.nombre} ({producto.descripcion}): {producto.precio}€")
import random

# Añadir un servicio y un producto aleatorios al cliente
servicio_aleatorio = random.choice(servicios)
producto_aleatorio = random.choice(productos)

cliente.agregar_servicio(servicio_aleatorio)
cliente.comprar_producto(producto_aleatorio)


# Generar la factura
generar_factura(cliente)
