class Carro:

    def __init__(self, marca, modelo, andando = False, velocidade = 0) -> None:
        self.__andando = andando
        self.marca = marca
        self.modelo = modelo
        self.__velocidade = velocidade

    def andar(self) -> None:
        self.__andando = True
        print(f"Carro andando...")

    def parar(self) -> None:
        self.__andando = False
        print(f"Carro parado")
    
    def get_estado(self) -> bool:
        return self.__andando
    
    def acelerar(self) -> int:
        if self.__andando == True:
            self.__velocidade += 20
            print(f"A velocidade do carro aumentou para {self.__velocidade}Km/h")
        else:
            print("Carro nao esta andando")
    
    def reduzir(self) -> int:
        if self.__andando == True:
            self.__velocidade -= 20
            print(f"A velocidade do carro reduziu para {self.__velocidade}Km/h")
        else:
            print("Carro nao esta andando")


objcar1 = Carro('Ford', 'Ford Ka')

objcar1.andar()

objcar1.acelerar()
objcar1.acelerar()
objcar1.acelerar()
objcar1.parar()
objcar1.reduzir()





        