# Ejercicio 4
class Coche:
    def __init__(self, nombre, velocidad_maxima, aceleracion):
        self.nombre = nombre
        self.velocidad_maxima = velocidad_maxima
        self.aceleracion = aceleracion
        self.posicion = 0.0
        self.velocidad = 0.0
    
    def mover(self, tiempo):
        nueva_velocidad = self.velocidad + self.aceleracion * tiempo
        self.velocidad = min(nueva_velocidad, self.velocidad_maxima)  
        self.posicion += self.velocidad * tiempo

class Carrera:
    def __init__(self):
        self.coches = []

    def agregar_coche(self, coche):
        self.coches.append(coche)

    def iniciar_carrera(self, duracion, intervalo):
        tiempo_actual = 0.0
        while tiempo_actual < duracion:
            print(f"Tiempo: {tiempo_actual} segundos")
            for coche in self.coches:
                coche.mover(intervalo)
                print(f"{coche.nombre} - Posición: {coche.posicion} metros, Velocidad: {coche.velocidad} m/s")
            tiempo_actual += intervalo
            print("-" * 40)
        print("Resultados finales:")
        for coche in self.coches:
            print(f"{coche.nombre}: Posición final: {coche.posicion} metros")

        ganador = max(self.coches, coche.posicion)
        print(f"El ganador es {coche.nombre} con una posicion {coche.posicion}")

if __name__ == "__main__":
   
    coche1 = Coche("Coche1", 150, 5)
    coche2 = Coche("Coche2", 140, 6)
    coche3 = Coche("Coche3", 160, 4.5)

    carrera = Carrera()
    carrera.agregar_coche(coche1)
    carrera.agregar_coche(coche2)
    carrera.agregar_coche(coche3)

    carrera.iniciar_carrera(60, 1)
