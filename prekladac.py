class Prekladac:
    slovnik = {  # zadefinovany slovnik s celymi nazvami a skratkami
        "DMR": "Digitálni modely reliéfu",  # kluc : hodnota
        "APU": "Algoritmizace prostorových úloh",
        "ZPD": "Zdroje prostorových dat",
        "DPZ": "Dálkový průzkum země",
        "DBS": "Databázové systémy",
    }

    def hladanie_nazvu(self, skratka):  # definovanie funkcie pre hladanie nazvu
        # funkcia get vyberie zo slovniku hodnotu na zaklade zadaneho kluca
        # pokial sa skratka nenachadza v slovniku tak funkcia get vrati "None"
        # funkcia upper automaticky kapitalizuje zadanu skratku
        # funkcia strip nam osetri to, pokial by sme pred input omylom zadali medzeru
        nazov = self.slovnik.get(skratka.upper().strip())
        # pokial sa nazov nenachadza v slovniku vypise chybovu hlasku
        if nazov is None:
            return "Nazov nebol najdeny."
        else:
            return nazov

    def hladanie_skratky(self, nazov):
        najdena_skratka = ""  # vytvorili sme prazdu premmenu, do ktorej budeme ukladat najdenu skratku
        for i in self.slovnik.items():  # cyklus ktory prechadza hodnoty v definovanom slovniku
            if nazov.strip() in i:  # pokial sa nazov nachadza v dvojici (kluc : hodnota)
                najdena_skratka = i[
                    0]  # tak priradime najdenej skratke prvu hodnotu z dvojice (kluc) v tomto pripade skratku
        if najdena_skratka == "":  # cyklus presiel celym slovnikom, pokial nenasiel zhodu vypise chybovu hlasku
            return "Skratka nebola najdena."
        else:
            return najdena_skratka