#==========Menu de Figuras Geometricas==========#

from Figuras import Cuadrado, Rectangulo, Circulo, Triangulo
from blessed import Terminal 


term = Terminal()

def menu_figuras():
    print(term.bold_blue("Hola, bienvenido a mi programa de figuras geometricas, donde calcularemos areas y perimetros"))
    print(term.bold_blue("Catalogo de Figuras Geometricas para calcular:"))
    print(term.yellow("1.- Cuadrado"))
    print(term.yellow("2.- Rectangulo"))
    print(term.yellow("3.- Circulo"))
    print(term.yellow("4.- Triangulo"))
    print(term.yellow("5.- Nada, no quiero hacer nada"))
    opcion = input("¿Que queremos calcular el dia de hoy?: ")
    return opcion
def main():
    while True:
        opcion = menu_figuras()
        if opcion == "1":
            lado = float(input("Ingrese el lado del cuadrado: "))
            cuadrado = Cuadrado(lado)
            print(cuadrado)
            print(term.yellow(f"Look, area={cuadrado.area()}"))
            print(term.yellow(f"Look, perimetro={cuadrado.perimetro()}"))
        elif opcion == "2":
            base = float(input("Ingrese la base del rectangulo: "))
            altura = float(input("Ingrese la altura del rectangulo: "))
            rectangulo = Rectangulo(base, altura)
            print(rectangulo)
            print(term.yellow(f"MIRA, este es el area del rectangulo: {rectangulo.area()}"))
            print(term.yellow(f"MIRA, este es el perimetro del rectangulo: {rectangulo.perimetro()}"))
        elif opcion == "3":
            radio = float(input("Ingrese el radio del circulo: "))
            circulo = Circulo(radio)
            print(circulo)
            print(term.yellow(f"Aqui tienes el area del circulo: {circulo.area()}"))
            print(term.yellow(f"Aqui tienes el perimetro del circulo: {circulo.perimetro()}"))
        elif opcion == "4":
            base = float(input("Ingrese la base del triangulo: "))
            altura = float(input("Ingrese la altura del triangulo: "))
            ladoiz = float(input("Ingrese el lado izquierdo del triangulo: "))
            ladode = float(input("Ingrese el lado derecho del triangulo: "))

            triangulo = Triangulo(base, altura, ladoiz, ladode)
            print(triangulo)
            print(term.yellow(f"Este es el area del triangulo: {triangulo.area()}"))
            print(term.yellow(f"Este es el perimetro del triangulo: {triangulo.perimetro()}"))
        elif opcion == "5":
            print(term.green("Gracias por visitarme, nos vemos luego..."))
            break
        else:
            print(term.red("Esta no es ninguna de las opciones que te di, intenta de nuevo"))
if __name__ == "__main__":
    main()

#==========Fin del Menu de Figuras Geometricas==========#