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
