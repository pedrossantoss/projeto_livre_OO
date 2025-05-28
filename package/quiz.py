class Quiz:
    def __init__(self):
        self._perguntas = []
        self._pontuacao = 0

    def adicionar_pergunta(self, pergunta):
        self._perguntas.append(pergunta)

    def jogar(self):
        self._pontuacao = 0
        for pergunta in self._perguntas:
            pergunta.apresentar()
            resposta = input("Sua resposta: ")
            if pergunta.verificar_resposta(resposta):
                print("Correta!\n")
                self._pontuacao += 1
            else:
                print("Errado!\n")

        print(f"Você acertou {self._pontuacao} de {len(self._perguntas)} perguntas.")

        return self._pontuacao  # ← IMPORTANTE: retornar pontuação!

