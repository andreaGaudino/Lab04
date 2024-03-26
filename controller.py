import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, e):
        txtIn = self._view._testoUtente.value
        modality = self._view._tipoRicerca.value
        language = self._view._menuLingua.value
        txtIn = replaceChars(txtIn.lower())
        self._stampa = ft.ListView()



        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                self._stampa.controls.append(ft.Text(f"Frase inserita: {self._view._testoUtente.value}"))
                self._stampa.controls.append(ft.Text(f"Le parole errate sono: {paroleErrate}"))
                self._stampa.controls.append(ft.Text(f"Tempo impiegato: {t2-t1}"))
                self._view.page.add(self._stampa)



            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                self._stampa.controls.append(ft.Text(f"Frase inserita: {self._view._testoUtente.value}"))
                self._stampa.controls.append(ft.Text(f"Le parole errate sono: {paroleErrate}"))
                self._stampa.controls.append(ft.Text(f"Tempo impiegato: {t2 - t1}"))
                self._view.page.add(self._stampa)


            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                self._stampa.controls.append(ft.Text(f"Frase inserita: {self._view._testoUtente.value}"))
                self._stampa.controls.append(ft.Text(f"Le parole errate sono: {paroleErrate}"))
                self._stampa.controls.append(ft.Text(f"Tempo impiegato: {t2 - t1}"))
                self._view.page.add(self._stampa)

            case _:
                return None


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text