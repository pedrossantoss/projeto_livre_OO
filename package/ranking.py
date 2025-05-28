import json

class Ranking:
    def __init__(self):
        self._jogadores = []

    def adicionar_jogador(self, jogador):
        self._jogadores.append(jogador)

    def exibir(self):
        if not self._jogadores:
            print("Ranking vazio!")
        else:
            print("\n=== Ranking ===")
            for i, jogador in enumerate(sorted(self._jogadores, key=lambda x: x._pontuacao, reverse=True), start=1):
                print(f"{i}. {jogador}")

    def salvar_em_arquivo(self, arquivo="ranking.json"):
        with open(arquivo, "w") as f:
            json.dump([{"nome": j._nome, "pontuacao": j._pontuacao} for j in self._jogadores], f)

    def carregar_de_arquivo(self, arquivo="ranking.json"):
        try:
            with open(arquivo, "r") as f:
                dados = json.load(f)
                from package.jogador import Jogador
                self._jogadores = [Jogador(d["nome"], d["pontuacao"]) for d in dados]
        except FileNotFoundError:
            self._jogadores = []