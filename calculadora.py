class Calculadora:

    def __init__(self, a, b):
        self.__Alpha = a
        self.__Beta = b

    def soma(self):
        return self.__Alpha + self.__Beta

    def subtrair(self):
        return self.__Alpha - self.__Beta

if __name__ == '__main__':
    Calculadora(0, 0)
