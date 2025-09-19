#==========Calculo de areas y perimetros de figuras geometricas==========#

class Cuadrado:
    def __init__(self, lado: float):
        self.lado = lado 
    
    def area(self):
        return self.lado ** 2
    
    def perimetro(self):
        return 4 * self.lado
    
    def __str__(self):
        return f"Cuadrado de lado {self.lado}" 


class Rectangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)
    
    def __str__(self):
        return f"Rectangulo de base {self.base} y altura {self.altura}"


class Circulo:
    def __init__(self, radio: float):
        self.radio = radio
    
    def area(self):
        return 3.1416 * self.radio ** 2
    
    def perimetro(self):
        return 2 * 3.1416 * self.radio
    
    def __str__(self):
        return f"Circulo de radio {self.radio}"


class Triangulo:
    def __init__(self, base: float, altura: float, ladoiz: float, ladode: float):
        self.base = base
        self.altura = altura
        self.ladoiz = ladoiz
        self.ladode = ladode
    
    def area(self):
        return (self.base * self.altura) / 2
    
    def perimetro(self):
        return self.base + self.ladoiz + self.ladode
    
    def __str__(self):
        return f"Triangulo de base {self.base} y altura {self.altura}"

#==========Fin del calculo de areas y perimetros de figuras geometricas==========#