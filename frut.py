class Fruta:
    def __init__(self, fruta, arrendamento, insumos, mudas, maodeobra, total):
        self.fruta = fruta
        self.arrendamento = arrendamento
        self.insumos = insumos
        self.mudas = mudas
        self.maodeobra = maodeobra
        self.total = total

    def gastos_total(self): 
        return self.arrendamento + self.insumos + self.mudas + self.maodeobra

    def lucro(self):
        return self.total - self.gastos_total()

    def resumo(self):  
        print(f"fruta: {self.fruta}")
        print(f"total de produto vendido: R$ {self.total}")
        print(f"arrendamento: R$ {self.arrendamento}")
        print(f"Insumos: R$ {self.insumos}")
        print(f"mudas/Sementes: R$ {self.mudas}")
        print(f"mão de Obra: R$ {self.maodeobra}")
        print(f"gato: R$ {self.gastos_total()}")
        print(f"lucro: R$ {self.lucro()}")



frutas = [
    Fruta("maçã", arrendamento=4500, insumos=5000, mudas=2000, maodeobra=5000, total=19000),
    Fruta("laranja", arrendamento=2500, insumos=4000, mudas=3000, maodeobra=4000, total=16000),
    Fruta("banana", arrendamento=2000, insumos=3000, mudas=1500, maodeobra=3500, total=13000),
    Fruta("melão", arrendamento=3000, insumos=4500, mudas=2000, maodeobra=4500, total=17000),
    Fruta("abacaxi", arrendamento=1500, insumos=3500, mudas=1500, maodeobra=3000, total=12000),
]

gasto_total = 0
for fruta in frutas:
    fruta.resumo()
    gasto_total += fruta.lucro()
    print()


