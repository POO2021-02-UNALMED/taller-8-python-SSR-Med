class Deportista:
    def __init__(self,deporte,añospracticando):
        self._deporte = deporte
        self._añospracticando = añospracticando
    def getDeporte(self):
        return self._deporte
    def setDeporte(self,deporte):
        self._deporte = deporte
    def getAñosPracticando(self):
        return self._añospracticando
    def setAñosPracticando(self,añospracticando):
        self._añospracticando = añospracticando
    