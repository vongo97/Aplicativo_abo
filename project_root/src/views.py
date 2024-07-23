from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Crear y agregar widgets
        layout.add_widget(Label(text='Sistema de Gestión de Trámites', font_size='20sp', bold=True))
        
        button_texts = [
            "Historial de Trámites",
            "Alertas de Trámites Inactivos",
            "Fichas de Propuesta de Pago",
            "Gestión de Leasing",
            "Actualización de PRAIMER",
            "Tiempo Estimado del Proceso",
            "Organización de Estados Procesales",
            "Informe de Estados Procesales",
            "Políticas MIAE",
            "Alerta de Trámites sin Seguimiento Judicial",
            "Previsualización de Visto Bueno y Facturación",
            "Plantillas para Escritos de Recursos",
            "Lista de Verificación de Documentos",
            "Última Actuación en Liquidación Patrimonial",
            "Análisis de Duración de Trámites",
            "Seguimiento de Pagos de Gastos de Administración"
        ]

        for text in button_texts:
            button = Button(text=text, size_hint_y=None, height=40, background_color=(0, 0, 1, 1), color=(1, 1, 1, 1))
            layout.add_widget(button)
        
        return layout

if __name__ == "__main__":
    MainApp().run()
