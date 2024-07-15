class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserirSemPrioridade(self, nodo):
        if not self.head:
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = nodo

    def inserirComPrioridade(self, nodo):
        if not self.head:
            self.head = nodo
        else:
            if self.head.cor == 'V':
                nodo.proximo = self.head
                self.head = nodo
            else:
                atual = self.head
                while atual.proximo and atual.proximo.cor == 'A':
                    atual = atual.proximo
                nodo.proximo = atual.proximo
                atual.proximo = nodo

    def inserir(self):
        cor = input("Digite a cor do cartão (A ou V): ").strip().upper()
        numero = int(input("Digite o número do cartão: ").strip())
        novo_nodo = Nodo(numero, cor)
        if not self.head:
            self.head = novo_nodo
        else:
            if cor == 'V':
                self.inserirSemPrioridade(novo_nodo)
            elif cor == 'A':
                self.inserirComPrioridade(novo_nodo)
            else:
                print("Cor inválida. Use 'A' para amarelo e 'V' para verde.")

    def imprimirListaEspera(self):
        atual = self.head
        while atual:
            print(f"Cartão {atual.numero} - Cor: {atual.cor}")
            atual = atual.proximo

    def atenderPaciente(self):
        if not self.head:
            print("Nenhum paciente na fila.")
        else:
            paciente = self.head
            self.head = self.head.proximo
            print(f"Chamando paciente do cartão {paciente.numero}")


def menu():
    fila = ListaEncadeada()
    while True:
        print("1 – Adicionar paciente à fila")
        print("2 – Mostrar pacientes na fila")
        print("3 – Chamar paciente")
        print("4 – Sair")
        opcao = int(input("Escolha uma opção: ").strip())
        if opcao == 1:
            fila.inserir()
        elif opcao == 2:
            fila.imprimirListaEspera()
        elif opcao == 3:
            fila.atenderPaciente()
        elif opcao == 4:
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()
