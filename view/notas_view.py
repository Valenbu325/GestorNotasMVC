class NotasView:
    def menu(self):
        print("\n1. Agregar nota\n2. Ver notas\n3. Editar nota\n4. Eliminar nota\n5. Salir")
        return input("Opción: ")

    def pedir_texto(self, msg="Escribe la nota: "):
        return input(msg)

    def pedir_indice(self):
        return int(input("Número de nota: ")) - 1

    def mostrar_notas(self, notas):
        for i, texto in enumerate(notas, 1):
            print(f"{i}. {texto}")

    def mostrar_mensaje(self, msg):
        print(msg)
