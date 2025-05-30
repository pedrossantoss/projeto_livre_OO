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
        p2 = MultiplaEscolha("LeBron James foi a primeira escolha do Draft de que ano?", ["1999", "2001", "2003"], "2003")
        p3 = MultiplaEscolha("Quem é o maior pontuador da história da NBA?", ["Kareem", "Jordan", "LeBron"], "LeBron")
        p4 = MultiplaEscolha("Quanto tempo dura um quarto no NBB?", ["15min", "12min", "10min"], "10min")
        p5 = MultiplaEscolha("Qual time da NBB ganhou o mundial de clubes em 2023?", ["Franca", "Flamengo", "Minas"], "Franca")
        p6 = VerdadeiroFalso("Michael Jordan jogou pelo Wizards.", "Verdadeiro")
        p7 = VerdadeiroFalso("Leandinho foi o primeiro brasileiro a ganhar um título da NBA.", "Falso")
        p8 = VerdadeiroFalso("A maior pontuação em um jogo da NBA foi de 100 pontos", "Verdadeiro")
        p9 = VerdadeiroFalso("Kobe foi o melhor pivô da história dos Lakers", "Falso")
        p10 = VerdadeiroFalso("Apenas um brasileiro ganhou algum prêmio individual na NBA.", "Verdadeiro")


        quiz.adicionar_pergunta(p1)
        quiz.adicionar_pergunta(p2)
        quiz.adicionar_pergunta(p3)
        quiz.adicionar_pergunta(p4)
        quiz.adicionar_pergunta(p5)
        quiz.adicionar_pergunta(p6)
        quiz.adicionar_pergunta(p7)
        quiz.adicionar_pergunta(p8)
        quiz.adicionar_pergunta(p9)
        quiz.adicionar_pergunta(p10)

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
            print("4. Limpar ranking")
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self.jogar_quiz()
            elif escolha == "2":
                self._ranking.exibir()

            elif escolha == "3":
                print("Saindo...")
                break

            elif escolha == "4":
                self.limpar_ranking()

            else:
                print("Opção inválida!")

    def limpar_ranking(self):
        confirmacao = input("Tem certeza que deseja limpar o ranking? (s/n): ")
        if confirmacao.lower() == 's':
            self._ranking._jogadores = []
            self._ranking.salvar_em_arquivo()
            print("Ranking limpo com sucesso!")
        else:
            print("Operação cancelada.")

