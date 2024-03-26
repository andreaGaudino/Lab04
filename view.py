import flet as ft
import controller as ct

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here
        #Riga 1
        self._menuLingua = ft.Dropdown(width=200,label="Scegli una Lingua",
                                       options=[ft.dropdown.Option("italian"),
                                                ft.dropdown.Option("english"),
                                                ft.dropdown.Option("spanish")],
                                       )

        row1 = ft.Row([self._menuLingua])

        #Riga 2
        self._tipoRicerca = ft.Dropdown(width=150, label="Tipo di ricerca", options=[
                                        ft.dropdown.Option("Default"),
                                        ft.dropdown.Option("Linear"),
                                        ft.dropdown.Option("Dichotomic")])
        self._testoUtente = ft.TextField(label="Inserisci il testo", width=500)
        #self._stampa = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._correzione = ft.ElevatedButton("Avvia correzione", width=200, on_click=self.__controller.handleSentence)
        row2 = ft.Row([self._tipoRicerca, self._testoUtente, self._correzione])


        self.page.add(row1, row2)

        self.page.update()

    def update(self):
        self.page.update()
    def setController(self, controller):
        self.__controller = controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()

    """"def handle_sentence(self):
        tupla = self.__controller.handleSentence(self._testoUtente.value, self._menuLingua.value, self._tipoRicerca.value)
        self._stampa = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._stampa.controls.append(ft.Text(f"Frase inserita: {self._testoUtente.value}"))
        self._stampa.controls.append(ft.Text(f"Parole errate: {tupla}"))
        self._stampa.controls.append(ft.Text(f"Tempo richiesto per la ricerca: {tupla}"))
        row3 = ft.Row([self._stampa])
    """""

