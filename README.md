QUESTÃO 1 de 2 – Lista Encadeada
Enunciado: Com a finalidade de melhorar o atendimento e priorizar os casos mais urgentes, a direção de um hospital criou um sistema de triagem em que um profissional da saúde classifica a ordem de atendimento com base numa avaliação prévia do paciente, entregando-lhe um cartão numerado verde (V) ou amarelo (A), que define o menor ou maior grau de urgência da ocorrência, respectivamente. Para informatizar esse processo, a direção do hospital contratou você para desenvolver uma fila de chamada seguindo as seguintes regras:

	Pacientes com cartão numerado amarelo (A) são chamados antes dos pacientes com cartão numerado verde (V)
	Entre os pacientes com cartão numerado amarelo (A), os que tem numeração menor são atendidos antes.
	Entre os pacientes com cartão numerado verde (V), os que tem numeração menor são atendidos antes.
	As numerações dos cartões amarelos (A) iniciam em 201.
	As numerações dos cartões verdes (V) inicial em 1.

Elabore um programa em Python que:
	 Deve-se implementar uma Lista Encadeada Simples em que: [EXIGÊNCIA DE CÓDIGO 1 de 7];
	O Nodo representa um cartão numerado contendo: número, cor e um ponteiro para o próximo;
	A lista contém um ponteiro para a cabeça da lista (head);
	 Deve-se implementar a função inserirSemPrioridade(nodo) em que: [EXIGÊNCIA DE CÓDIGO 2 de 7];
	 Deve-se andar pela lista a partir da cabeça (head) e inserir o nodo no final da lista.
	 Deve-se implementar a função inserirComPrioridade(nodo) em que: [EXIGÊNCIA DE CÓDIGO 3 de 7];
	 Deve-se andar pela lista a partir da cabeça (head) e inserir o nodo após todos os nodos com cor “A” que estão na lista.
	 O nodo inserido deve sempre estar antes de todos os nodos com cor “V”.
	 Deve-se implementar a função inserir() em que: [EXIGÊNCIA DE CÓDIGO 4 de 7];
	 Deve-se solicitar ao usuário a cor (“A” ou “V”) e o número (inteiro).
	 Deve-se criar um nodo com a cor e o número fornecidos pelo usuário.
	 Se a lista estiver vazia, a cabeça (head) da lista deve apontar para o nodo criado.
	 Senão, se a cor do nodo for “V”, deve-se chamar a função inserirSemPrioridade(nodo).
	 Senão, se a cor do nodo for “A”, deve-se chamar a função inserirComPriordade(nodo).
	 Deve-se implementar a função imprimirListaEspera() em que: [EXIGÊNCIA DE CÓDIGO 5 de 7];
	 Deve-se imprimir todos os cartões e seus respectivos números a partir do primeiro até o último da lista.
	 Deve-se implementar a função atenderPaciente() em que: [EXIGÊNCIA DE CÓDIGO 6 de 7];
	 Deve-se remover o primeiro paciente da fila e imprimir uma mensagem chamando o paciente para atendimento informando o número do seu cartão.
	 Deve-se implementar um menu para utilização do sistema em que: [EXIGÊNCIA DE CÓDIGO 7 de 7];
	 Deve-se apresentar as opções (1 – adicionar paciente a fila, 2 – mostrar pacientes na fila, 3 – chamar paciente, 4 – sair)
	 Se escolhida a opção 1, chamar a função inserir().
	 Se escolhida a opção 2, chamar a função imprimirListaEspera().
	 Se escolhida a opção 3, chamar a função atenderPaciente().
	 Se escolhida a opção 4, encerrar o programa.
	 Se escolhida uma opção diferente as opções disponíveis, voltar ao item G.a.

Para testar o software, execute os seguintes passos e apresente a saída do console conforme exemplo de saída de console (próxima página):
	Deve-se testar o sistema inserindo três (3) pacientes com cartão de cor “V”, dois (2) pacientes com cartão de cor “A”, dois (2) pacientes com cartão “V” e três (3) pacientes com cartão de cor “A”, nessa respectiva ordem. [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 3];
	Deve-se apresentar na saída de console a impressão da lista de espera (opção 2 do menu principal). [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 3];  
	Deve-se apresentar na saída de console o atendimento de dois (2) pacientes (opção 3 do menu principal) e em seguida mostrar a lista de espera (opção 2 do menu principal). [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 3];  


EXEMPLO DE SAÍDA DE CONSOLE:
     
Figura 1: Exemplo de saída de console que o aluno deve fazer.  Em que se insere 10 pacientes (5 com cartão verde e 5 com cartão amarelo) conforme [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 3];
 
Figura 2: Exemplo de saída de console que o aluno deve fazer.  Em que mostra a lista de pacientes, conforme [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 3];
 
Figura 3: Exemplo de saída de console que o aluno deve fazer.  Em que ele chama dois pacientes para atendimento e em seguida mostra a lista de pacientes, conforme [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 3];

Apresentação de Código da Questão 1:

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

 
Apresentação de Saída do Console da Questão 1:
 


QUESTÃO 2 de 2 – Tabela Hash
Enunciado: Com o objetivo de criar um sistema novo de emplacamento de veículos, deputados em do Distrito Federal – DF, decidiram que o último número da placa dos veículos, irá representar o estado de registro dele. Para isso, sua equipe de desenvolvedores foi encarregada de desenvolver uma Tabela Hash com endereçamento em cadeia de 10 posições (cada posição do vetor deve ser uma lista encadeada), representando os números de 0 a 9 que irão representar os 26 estados e o Distrito Federal (total 27).

A função hash deve seguir as seguintes regras:
	A entrada da função hash deve ser uma string com 2 letras, representando a sigla do estado e/ou distrito federal.
	Caso a sigla seja DF (Distrito Federal), por questões de superstição, os deputados solicitaram que o retorno da função seja 7 sempre.
	Caso contrário, a função deve retornar a posição com base no valor ASCII das duas letras e seguindo a seguinte regra:

posição=(〖CHAR1〗_ASCII+ 〖CHAR2〗_ASCII )MOD 10

Onde 〖CHAR1〗_ASCII e 〖CHAR2〗_ASCII são os valores ASCII da primeira e segunda letra, respectivamente (Tabela ASCII no final do documento).

Elabore um programa em Python que: 
	Deve-se implementar a tabela Hash com 10 posições, onde inicialmente todas as posições possuem valor None [EXIGÊNCIA DE CÓDIGO 1 de 7];
	Deve-se implementar as Listas Encadeadas Simples em que: [EXIGÊNCIA DE CÓDIGO 2 de 7];
	O Nodo representa um Estado contendo: sigla, nomeEstado e um ponteiro para o próximo;
	As 10 posições da tabela hash, representam a cabeça de cada lista (head).
	Deve-se implementar a inserção no início da lista encadeada (cada elemento novo deve ser sempre inserido no início da lista) [EXIGÊNCIA DE CÓDIGO 3 de 7];
	Deve-se implementar a impressão da tabela hash, onde devem ser impressas as siglas de todos os nodos que estão na tabela hash separados por posição [EXIGÊNCIA DE CÓDIGO 4 de 7];
	Deve-se implementar a função hash, conforme enunciado. [EXIGÊNCIA DE CÓDIGO 5 de 7];
	Deve-se implementar a inserção dos estados e distrito federal (todos os 27 com nome e sigla) na tabela hash utilizando a função hash (não precisa solicitar ao usuário, pode inserir no código mesmo) [EXIGÊNCIA DE CÓDIGO 6 de 7];
	Deve-se inserir na Tabela, além dos estados e distrito federal, um estado fictício, sendo que esse estado tenha seu nome completo e como siglas, a primeira letra do seu nome e a primeira letra do seu último sobrenome. Exemplo: Bruno Kostiuk – BK. EXIGÊNCIA DE CÓDIGO 7 de 7];

Para testar o software, execute os seguintes passos e apresente a saída do console conforme exemplo de saída de console (próxima página):
	Deve-se apresentar na saída de console, a impressão da tabela hash antes de inserir qualquer informação [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 3];
	Deve-se apresentar na saída de console, a impressão da tabela hash após inserir os 26 estados e o Distrito Federal - DF [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 3]; 
	Deve-se apresentar na saída de console, a impressão da tabela hash após inserir os 26 estados, Distrito Federal – DF e o estado fictício com seu nome completo. [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 3];

 
EXEMPLO DE SAÍDA DE CONSOLE:

 

Figura 1: Exemplo de saída de console que o aluno deve fazer.  Impressão da tabela hash antes de inserir qualquer informação, conforme [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 3];

 

Figura 1: Exemplo de saída de console que o aluno deve fazer.  Impressão da tabela hash após inserir os 26 estados e o Distrito Federal - DF, conforme [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 3];
 

Figura 1: Exemplo de saída de console que o aluno deve fazer.  Impressão da tabela hash após inserir os 26 estados, Distrito Federal – DF e o estado fictício com seu nome completo (No caso foi inserido BK na posição 1), conforme [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 3];
 
Apresentação de Código da Questão 2:
class Nodo:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

class TabelaHash:
    def __init__(self):
        self.tabela = [None] * 10  # Tabela hash com 10 posições
    
    def funcao_hash(self, sigla):
        if sigla == "DF":
            return 7
        else:
            return (ord(sigla[0]) + ord(sigla[1])) % 10
    
    def inserir(self, sigla, nomeEstado):
        indice = self.funcao_hash(sigla)
        novo_nodo = Nodo(sigla, nomeEstado)
        if not self.tabela[indice]:
            self.tabela[indice] = novo_nodo
        else:
            novo_nodo.proximo = self.tabela[indice]
            self.tabela[indice] = novo_nodo
    
    def imprimir(self):
        for i in range(10):
            print(f"Posição {i}: ", end="")
            atual = self.tabela[i]
            while atual:
                print(f"{atual.sigla} ", end="")
                atual = atual.proximo
            print()

# Inserindo os estados e Distrito Federal na tabela hash
estados = [
    ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"), ("BA", "Bahia"),
    ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"), ("GO", "Goiás"), 
    ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"), ("MG", "Minas Gerais"), 
    ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"), ("PE", "Pernambuco"), ("PI", "Piauí"), 
    ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"), ("RS", "Rio Grande do Sul"), 
    ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"), ("SP", "São Paulo"), 
    ("SE", "Sergipe"), ("TO", "Tocantins")
]

tabela_hash = TabelaHash()

# Exigência de Saída de Console 1: Impressão inicial da tabela hash
print("Tabela Hash Inicial:")
tabela_hash.imprimir()
print()

# Inserindo os estados na tabela hash
for sigla, nome in estados:
    tabela_hash.inserir(sigla, nome)

# Exigência de Saída de Console 2: Impressão da tabela hash após inserir os estados
print("Tabela Hash após inserir os estados:")
tabela_hash.imprimir()
print()

# Inserindo o estado fictício
tabela_hash.inserir("DO", "Daniel Ortega")

# Exigência de Saída de Console 3: Impressão da tabela hash após inserir o estado fictício
print("Tabela Hash após inserir os estados e o estado fictício:")
tabela_hash.imprimir()

Apresentação de Saída do Console da Questão 2:
 

