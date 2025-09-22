class Nota:
    def __init__(self, texto: str):
        self.texto = texto


class GestorNotas:
    def __init__(self):
        self.notas = []

    def agregar(self, texto):
        self.notas.append(Nota(texto))

    def listar(self):
        return [nota.texto for nota in self.notas]

    def editar(self, indice, nuevo_texto):
        if 0 <= indice < len(self.notas):
            self.notas[indice].texto = nuevo_texto
        else:
            raise IndexError("Nota no encontrada")

    def eliminar(self, indice):
        if 0 <= indice < len(self.notas):
            self.notas.pop(indice)
        else:
            raise IndexError("Nota no encontrada")
