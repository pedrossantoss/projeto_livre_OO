class Pergunta:
    def __init__(self, enunciado, resposta_correta):
        self._enunciado = enunciado
        self._resposta_correta = resposta_correta

    def apresentar(self):
        """Apresenta a pergunta (será sobrescrito nas subclasses)."""
        print(self._enunciado)

    def verificar_resposta(self, resposta_usuario):
        """Verifica se a resposta está correta."""
        return resposta_usuario.strip().lower() == self._resposta_correta.strip().lower()


class MultiplaEscolha(Pergunta):
    def __init__(self, enunciado, opcoes, resposta_correta):
        super().__init__(enunciado, resposta_correta)
        self._opcoes = opcoes  # lista de opções

    def apresentar(self):
        print(self._enunciado)
        for i, opcao in enumerate(self._opcoes, start=1):
            print(f"{i}. {opcao}")

    def verificar_resposta(self, resposta_usuario):
        try:
            indice = int(resposta_usuario) - 1
            return self._opcoes[indice].strip().lower() == self._resposta_correta.strip().lower()
        except (ValueError, IndexError):
            return False


class VerdadeiroFalso(Pergunta):
    def __init__(self, enunciado, resposta_correta):
        super().__init__(enunciado, resposta_correta)

    def apresentar(self):
        print(f"{self._enunciado} (Verdadeiro/Falso)")
