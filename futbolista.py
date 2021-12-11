from deportista import Deportista
from persona import Persona
class Futbolista(Deportista,Persona):
    #Comentario para que se actualice
    listaFutbolistas = []
    def __init__(self,nombre,edad,altura,sexo,añospracticando,golesMarcados,tarjetasRojas,piernaHabil):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbol", añospracticando)
        self._tarjetasRojas = tarjetasRojas
        self._golesMarcados = golesMarcados
        self._piernaHabil = piernaHabil
        Futbolista.listaFutbolistas.append(self)
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    def setTarjetasRojas(self,tarjetasRojas):
        self._tarjetasRojas = tarjetasRojas
    def getGolesMarcados(self):
        return self._golesMarcados
    def setGolesMarcados(self,golesMarcados):
        self._golesMarcados = golesMarcados
    def getPiernaHabil(self):
        return self._piernaHabil
    def setPiernaHabil(self,piernaHabil):
        self._piernaHabil = piernaHabil
    def __str__(self):
        return "Mi nombre es " + str(self.getNombre()) + " soy profesional en el deporte " + str(self.getDeporte()) + " Tengo " + str(self.getEdad()) + " años de edad y llevo " + str(self.getAñosPracticando()) + " en el deporte"
        
    
