datos = {
    "informacion":
    [
        {
            "nombre","jeo el trapeador",
            "tipo entrada","general",
            "codigo de validacion",123,
        },
        {
            "nombre","jose",
            "tipo entrada","vip",
            "codigo de validacion",321,
        },
    ]
}

print("1 - Comprar entrada")
print("2 - Consultar comprador")
print("3 - Cancelar compra")
print("4 - Salir")

opc = int(input("ingrese una opcion"))


def buscar_informacion(informacion:str):
    for i in datos["informacion"]:
        if i["informacion"] == informacion:
            return
        
def validar_codigo(mensaje):
    while True:
        try:
            codigo = int(input(mensaje))
            if codigo <= 0:
                print("solo se permiten numeros enteros")
                continue
            return codigo
        except ValueError:
            print("solo se puede ingresar numeros enteros")
            continue

def validar_texto(mensaje_input:str):
    while True:
        texto = input(mensaje_input)
        if len(texto) == 0:
            print("el texto esta vacio, no es valido")
            continue
        else:
            return texto


def validar_tipo_entrada():
    while True:
        if validar_tipo_entrada == "general" or validar_tipo_entrada =="vip":
            return validar_tipo_entrada
        else:
            print("tipo de entrada no es valida")
            continue


nombre = input("ingrese su nombre")
tipo_entrada = input("ingrese tipo de entrada que desea")


def validar_datos():
    for i in datos["informacion"]:
        if opc == 1:
            nombre = input("ingrese su nombre")
            tipo_entrada = input("ingrese tipo de entrada que desea")
            print("su codigo de: ")
            print("su compra fue hecha con exito")
        elif opc == 2:
            nombre = input("ingrese su nombre")
            print(datos["informacion"])
        elif opc == 3:
            print("Ingrese nombre de comprador a cancelar")
            nombre =input("ingrese su nombre")
            print("¡Compra cancelada!")
        elif opc == 4:
            print("Programa terminado...")
        else:
            continue
        print("Debe ingresar una opción válida!!")
