from model.notas_model import GestorNotas
from view.notas_view import NotasView

class NotasController:
    def __init__(self):
        self.model = GestorNotas()
        self.view = NotasView()

    def ejecutar(self):
        while True:
            opcion = self.view.menu()
            if opcion == "1":
                texto = self.view.pedir_texto()
                self.model.agregar(texto)
                self.view.mostrar_mensaje("✅ Nota agregada.")
            elif opcion == "2":
                self.view.mostrar_notas(self.model.listar())
            elif opcion == "3":
                try:
                    idx = self.view.pedir_indice()
                    nuevo = self.view.pedir_texto("Nuevo texto: ")
                    self.model.editar(idx, nuevo)
                    self.view.mostrar_mensaje("✏️ Nota actualizada.")
                except Exception as e:
                    self.view.mostrar_mensaje(str(e))
            elif opcion == "4":
                try:
                    idx = self.view.pedir_indice()
                    self.model.eliminar(idx)
                    self.view.mostrar_mensaje("🗑️ Nota eliminada.")
                except Exception as e:
                    self.view.mostrar_mensaje(str(e))
            elif opcion == "5":
                self.view.mostrar_mensaje("👋 Saliendo del gestor de notas.")
                break
            else:
                self.view.mostrar_mensaje("❌ Opción inválida.")
