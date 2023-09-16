import re

def _numero_cardinal(numero):
        # Validar si el número está dentro del rango manejado
    if 0 <= numero <= 11:
        numeros_hasta_20 = [
            "cero", "1ro", "2do", "3ro", "4to", "5to", 
            "6to", "7to", "8vo", "9no", "10mo", 
            "11mo"
        ]
    return numeros_hasta_20[numero]

class Estudiante():
    def __init__(self,nombre,edad,grado):
        self.validar_nombre(nombre)
        self.validar_edad(edad)
        self.validar_grado(grado)
        # self.grado = grado
    
    def validar_nombre(self, nombre):
        # Verificar longitud
        if len(nombre) < 2 or len(nombre) > 50:
            raise ValueError("El nombre debe ser mayor a 2 y menor a 50 caracteres")

        # Verificar caracteres permitidos (letras, espacios y apóstrofos)
        if not re.match(r"^[a-zA-Z\s']+$", nombre):
            raise ValueError("El nombre debe contener solo letras, espacios y apóstrofos")
        
        # Otras reglas de validación pueden agregarse aquí
        self.nombre = nombre
    
    def validar_edad(self, edad):
        if edad < 1 or edad > 100:
            raise ValueError("la edad debe ser mayor a 2 y menor a 100 años")
        self.edad = edad
        
    def validar_grado(self, grado):
        if grado <= 0 or grado > 11:
            raise ValueError("el grado debe ser mayor a 0 y menor a 11")
        self.grado = grado



    def estudiar(self):
        print(f"{self.nombre} estudiando.")

    def __str__(self):
        return f"""DATOS DEL ESTUDIANTE: \n Nombre: {self.nombre} \n Edad: {self.edad} \n Grado: {_numero_cardinal(self.grado)}\n"""
    

class ValidationInput():
    def __init__(self, message):
        self.message = message
    
    def text(self):
        while True:
            try:
                text = input(self.message)
                if text.isalpha():
                    return text
                else:
                    raise ValueError
            except ValueError:
                print("Ingrese solo letras.")

    def number(self):
        while True:
            try: 
                number = int(input(self.message))
                if number > 0:
                    return number
                else:
                    raise ValueError
            except ValueError:
                print("Ingrese solo números enteros positivos.")

def insert_estudiante():
    while True:
        try:
            nombre = ValidationInput("Ingrese nombre: ").text()
            edad = ValidationInput("Ingrese edad: ").number()
            grado = ValidationInput("Ingrese grado: ").number()
            return Estudiante(nombre,edad,grado)
        except ValueError:
                print("Vuelva ingresar los datos.")

def main():
    estudiante1 = Estudiante("Juan",10, 5)
    estudiante2 = insert_estudiante()
    print(estudiante1)
    print(estudiante2)
    estudiante1.estudiar()
    estudiante2.estudiar()


if __name__ == "__main__":
    main()