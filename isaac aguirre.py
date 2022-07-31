productos={
"Olla arrocera":20.00,
"Tabla de planchar":18.00,
"Tv Plasma 50pulgadas":700.00,
"Cocina de induccion":400.00,
"laptop 8gb de ram":700.00,
"teclado inalambrico":20.00,
"Audifonos":10.00,
"Silla Gamer":30.00,
"Lavadora 8kg":200.00,
"Refrigeradora":150.00,
          }

clientes={
"0989147629" : "Ricardo Aguirre",
"0914763898" : "Jeremias Carpio",
"0910201040" : "Elias Ronquillo",
"0909210940" : "Nelly Calderon",
"0940107056" : "Kevin Borbor",
"0960903416" : "Joselyn Borbor",
"0909306070" : "Daniel Diaz",
"0945891410" : "Kelly Murillo",
"0923504010" : "Jonathan Martinez",
"0921904560" : "Juan Hernandez",
         }

facturacion={}

numerador=0
numeroCedula=input("Ingrese el CI del cliente: ")
for clave,valor in clientes.items():
    if numeroCedula==clave:
        print(f"Cliente: {valor}")
        nombreCliente=valor
        cedula=numeroCedula
        numerador=1

if numerador==0:
    print("Cliente no existe")
    nombreCliente="Consumidor Final"
    cedula=9999999999


print("")
agregador=0
contador=1
acumulador=0
Paso=True
print("\tProductos")
for clave1,valor1 in productos.items():
    print(f"{clave1}")
while(Paso):
    print("")
    nombreProducto=input(f"Ingrese nombre del producto {contador}: ")
    if nombreProducto=="":
        Paso=False
        break
    for clave1,valor1 in productos.items():
        if nombreProducto.lower()==clave1.lower():
            cantidad=int(input("Ingrese cantidad: "))
            unidad=valor1
            if cantidad==0:
                Paso=False
                break
            facturacion[clave1]=cantidad
            agregador+=1
            valor=cantidad*valor1
            break
    print(f"Cantidad: {cantidad} - {clave1}")
    print(f"P.Unitario: ${unidad:.2f} - Valor total: ${valor:.2f}")
    acumulador+=valor
    contador+=1

print("")
print("Datos del cliente")
print(f"Nombre: {nombreCliente}")
print(f"Cedula: {cedula}")
print("")
n=0
print("Lista de productos")
for product,cant in facturacion.items():
    print(f"Cantidad: {cant} - Producto: {product}")


totalPagar=(acumulador*1.12)
if totalPagar<50:
    descuento = 0
if totalPagar>=50:
    descuento = 5
if totalPagar>100:
    descuento = 10
if totalPagar>200:
    descuento = 15
    print("")
print(f"Subtotal: {acumulador:.2f}")
print(f"IVA 12%: {(acumulador * 0.12):.2f}")
print(f"Descuento: ${descuento:.2f}")
print(f"Total a pagar: {(acumulador*1.12)-descuento:.2f}")