# tentativas da ideia inicial

# from package.sistema import Sistema
# from package.pergunta import MultiplaEscolha, VerdadeiroFalso

# def main():
#     sistema = Sistema()
#     sistema.menu_principal()

# def testar_perguntas():
#     # Criando exemplos
#     p1 = MultiplaEscolha("Quem venceu a NBA em 2020?", ["Lakers", "Heat", "Celtics"], "Lakers")
#     p2 = VerdadeiroFalso("Michael Jordan jogou pelo Chicago Bulls.", "Verdadeiro")

#     # Testando apresentação e verificação
#     p1.apresentar()
#     resposta = input("Sua resposta: ")
#     print("Correta!" if p1.verificar_resposta(resposta) else "Errado!")

#     p2.apresentar()
#     resposta = input("Sua resposta: ")
#     print("Correta!" if p2.verificar_resposta(resposta) else "Errado!")

# # if __name__ == "__main__":
# #     testar_perguntas()


from package.quiz import Quiz
from package.pergunta import MultiplaEscolha, VerdadeiroFalso

def testar_quiz():
    quiz = Quiz()

    p1 = MultiplaEscolha("Quem venceu a NBA em 2020?", ["Lakers", "Heat", "Celtics"], "Lakers")
    p2 = VerdadeiroFalso("Michael Jordan jogou pelo Chicago Bulls.", "Verdadeiro")

    quiz.adicionar_pergunta(p1)
    quiz.adicionar_pergunta(p2)

    quiz.jogar()

if __name__ == "__main__":
    testar_quiz()
