from interprete import parse

while True:
    comando = input("Ingresa el comando: ")
    if (comando == "salir"):
        break
    resultado = parse(comando)
    resul = resultado.ejecutar() #polimorfismo donde todos los objetos heredan el metodo ejecutar