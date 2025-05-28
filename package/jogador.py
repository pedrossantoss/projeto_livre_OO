class Jogador:
    def __init__(self, nome, pontuacao):
        self._nome = nome
        self._pontuacao = pontuacao

    def __str__(self):
        return f"{self._nome} - {self._pontuacao} pontos"
