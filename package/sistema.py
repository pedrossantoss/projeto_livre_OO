from package.jogador import Jogador
from package.ranking import Ranking
from package.quiz import Quiz
from package.pergunta import MultiplaEscolha, VerdadeiroFalso


class Sistema:
    def __init__(self):
        from package.ranking import Ranking        
        self._ranking = Ranking()
        self._ranking.carregar_de_arquivo()

    def jogar_quiz(self):
        quiz = Quiz()

        p1 = MultiplaEscolha("Quem venceu a NBA em 2020?", ["Lakers", "Heat", "Celtics"], "Lakers")
        p2 = VerdadeiroFalso("Michael Jordan jogou pelo Chicago Bulls.", "Verdadeiro")

        quiz.adicionar_pergunta(p1)
        quiz.adicionar_pergunta(p2)

        nome = input("Digite seu nome: ")
        pontuacao = quiz.jogar()

        jogador = Jogador(nome, pontuacao)
        self._ranking.adicionar_jogador(jogador)
        self._ranking.salvar_em_arquivo()

    def menu_principal(self):
        while True:
            print("\n=== Quiz de Basquete ===")
            print("1. Jogar")
            print("2. Ver ranking")
            print("3. Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self.jogar_quiz()
            elif escolha == "2":
                self._ranking.exibir()

            elif escolha == "3":
                print("Saindo...")
                break
            else:
                print("Opção inválida!")
