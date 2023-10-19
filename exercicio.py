import os

# Função para carregar os produtos a partir do arquivo
def carregarProdutos():
    produtos = []#lista de produtos que armazena produto{} -> logo armazena dicionários
    if os.path.exists('produtos.txt'):
        with open('produtos.txt', 'r') as file:
            for linha in file:
                if linha.startswith('ID: '):
                    # Extrai informações do produto da linha do arquivo e cria um dicionário para representar o produto
                    id_str = linha.split(': ')[1].split(',')[0]
                    id = int(id_str)
                    nome = linha.split('Nome: ')[1].split(',')[0]
                    peso = float(linha.split('Peso: ')[1].split(',')[0])
                    valor = float(linha.split('Valor: ')[1].split(',')[0])
                    fornecedor = linha.split('Fornecedor: ')[1].strip()
                    
                    produto = {'ID': id, 'Nome': nome, 'Peso': peso, 'Valor': valor, 'Fornecedor': fornecedor} #discionario
                    produtos.append(produto)
    return produtos

# Função para salvar os produtos no arquivo
def salvarProdutos(produtos):
    with open('produtos.txt', 'w') as file:
        for produto in produtos:
            # Escreve informações do produto no arquivo
            file.write(f"ID: {produto['ID']}, Nome: {produto['Nome']}, Peso: {produto['Peso']}, Valor: {produto['Valor']}, Fornecedor: {produto['Fornecedor']}\n")

# Função para adicionar um produto
def adicionarProduto(produtos, nome, peso, valor, fornecedor):
    ultimo_id = 0
    if produtos:
        ultimo_id = max(produto['ID'] for produto in produtos)
    novo_id = ultimo_id + 1
    novo_produto = {'ID': novo_id, 'Nome': nome, 'Peso': peso, 'Valor': valor, 'Fornecedor': fornecedor}
    produtos.append(novo_produto)
    return produtos
#--

# Função para adicionar usuario
## abre o arquivo 'usuario.txt' e adicionar os dados ao final do arquivo
def adicionarUsuario(nome_sobrenome_usuario, senha):
    with open('usuario.txt', 'a') as file:
        file.write(f"Nome: {nome_sobrenome_usuario}, Senha: {senha}\n")
#--

# Função para atualizar os dados do produto escolhido pelo usuario com base no ID
def atualizarProduto(produtos, idEscolhidoParaAtualizarProduto):
    for produto in produtos:
        if produto['ID'] == idEscolhidoParaAtualizarProduto:
            print(f"Produto atual: {produto}")
            novo_nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ")
            novo_peso = input("Digite o novo peso (ou pressione Enter para manter o atual): ")
            novo_valor = input("Digite o novo valor (ou pressione Enter para manter o atual): ")
            novo_fornecedor = input("Digite o novo fornecedor (ou pressione Enter para manter o atual): ")

            # Atualiza os campos do produto com os novos valores, se fornecidos... usando chave-valor
            if novo_nome:
                produto['Nome'] = novo_nome
            if novo_peso:
                produto['Peso'] = float(novo_peso)
            if novo_valor:
                produto['Valor'] = float(novo_valor)
            if novo_fornecedor:
                produto['Fornecedor'] = novo_fornecedor

            print("Produto atualizado com sucesso!")
            return
    
    print(f"Nenhum produto encontrado com o ID {idEscolhidoParaAtualizarProduto}.")
#--
        
def excluirProduto(produtos, idEscolhidoParaExcluirProduto):
    for produto in produtos:
        if produto['ID'] == idEscolhidoParaExcluirProduto:
            produtos.remove(produto)
            print(f"Produto com ID {idEscolhidoParaExcluirProduto} excluído com sucesso.")
            return
    
    print(f"Nenhum produto encontrado com o ID {idEscolhidoParaExcluirProduto}.")
#--

#Metodos de ordenacao
def bubble_sort(produtos):
    qtd_produtos = len(produtos)
    for i in range(qtd_produtos-1):
        for j in range(0, qtd_produtos-i-1):
            if produtos[j]['Nome'] > produtos[j+1]['Nome']:
                produtos[j], produtos[j+1] = produtos[j+1], produtos[j]

def insertion_sort(produtos):
    for i in range (1, len(produtos)):
        chave = produtos[i]
        j = i-1
        while j>=0 and chave['Nome'] < produtos[j]['Nome']:
            produtos[j+1] = produtos[j]
            j -= 1
        produtos[j+1] = chave
    
def selection_sort(produtos):
    qtd_produtos = len(produtos)
    for i in range(qtd_produtos):
        min_idx = i
        for j in range(i + 1, qtd_produtos):
            if produtos[j]['Nome'] < produtos[min_idx]['Nome']:
                min_idx = j
        produtos[i], produtos[min_idx] = produtos[min_idx], produtos[i]
#--
    
# Função para listar produtos pelo metodo
def listarProdutosEmMetodos(produtos):
    metodos = {'a': bubble_sort,'b': insertion_sort,'c': selection_sort} # atraves desse dicionario da pra eu filtrar qual funcao eu vou chamar 
    metodo_escolhido = input("METODOS:\n(a) - Bubble Sort\n(b) - Insertion Sort\n(c) - Selection Sort\nEscolha o método(a, b, c): ").lower()
    #validacao do metodo q serah ordenado os produtos
    while metodo_escolhido not in ['a', 'b', 'c']:
        print("Opção inválida para o metodo. Tente novamente.")
        metodo_escolhido = input("METODOS:\n(a) - Bubble Sort\n(b) - Insertion Sort\n(c) - Selection Sort\nEscolha o método(a, b, c): ").lower()
    
    
    if metodo_escolhido in metodos: # filtrando
        metodo_escolhido = metodos[metodo_escolhido] #sobrescreve os dados de metodo_escolhido... a/b/c = bubble_sorte/insertion_sort/selection_sort 
        produtos_ordenados = produtos.copy()  # Copia a lista de produtos para evitar alterações na lista original
        metodo_escolhido(produtos_ordenados)  # Ordena a cópia dos produtos ... bubble_sort/insertion_sort/selection_sort(produtos_ordenados)
        listarProdutosOrdemAlfabetica(produtos_ordenados)
        ##RETIRAR DEPOIS ... !!!!!!!!!!!!!!!
        #for produto in produtos_ordenados:
        #    print(produto)
    
    
# Função para listar produtos em ordem alfabética (crescente ou decrescente)
def listarProdutosOrdemAlfabetica(produtos):
    #validação da Ordem dos produtos 
    ordem = input("ORDEM:\n(d) - crescente\n(e) - decrescente\nEscolha a ordem(d, e): ").lower()
    while ordem not in ['d', 'e']:
        print("Opção inválida para a ordem. Tente novamente.")
        ordem = input("ORDEM:\n(d) - crescente\n(e) - decrescente\nEscolha a ordem(d, e): ").lower()

    
    if ordem == 'd':
        produtos_ordenados = sorted(produtos, key=lambda x: x['Nome'])
    else:
        produtos_ordenados = sorted(produtos, key=lambda x: x['Nome'], reverse=True)

    if produtos_ordenados:
        for produto in produtos_ordenados:
            print(produto)
    else:
        print("Nenhum produto para listar.")
#--


# Função principal
def main():
    # Carrega os produtos do arquivo... evitará de resetar o ID dos produtos toda vez que abrir o programa
    produtos = carregarProdutos()

    #Solicitando nome.sobrenome e senha
    nomeSobrenome = input("Digite seu nome e sobrenome: ")
    senha = input("Digite sua senha: ")
    adicionarUsuario(nomeSobrenome, senha)

    while True:
        print('''
            ======== MENU ==========
                1. Listar todos os produtos
                2. Listar produto pelo ID
                3. Listar todos os produtos ordenados (A/Z)
                4. Cadastrar novo produto
                5. Editar produto
                6. Excluir produto
                7. Salvar e Sair do programa
            ========================
        ''')

        opMenu = input("Selecione uma das opções: ")

        if opMenu == '1':
            print("Listagem de todos os produtos:")
            for produto in produtos:
                print(produto)
        elif opMenu == '2':
            ids_para_listar = input("Digite os IDs dos produtos separados por vírgula: ").split(',')
            ids_para_listar = [int(id_str.strip()) for id_str in ids_para_listar]
            produtos_encontrados = [produto for produto in produtos if produto['ID'] in ids_para_listar]

            if produtos_encontrados:
                for produto in produtos_encontrados:
                    print(produto)
            else:
                print("Nenhum produto encontrado com os IDs especificados.")
        elif opMenu == '3':
            
            listarProdutosEmMetodos(produtos)
        elif opMenu == '4':
            nomeProduto = input("Digite o nome do produto: ")
            pesoProduto = float(input("Digite o peso do produto: "))
            valorProduto = float(input("Digite o valor do produto: "))
            fornecedorProduto = input("Informe o fornecedor do produto: ")

            # Adiciona um novo produto à lista de produtos
            produtos = adicionarProduto(produtos, nomeProduto, pesoProduto, valorProduto, fornecedorProduto)
            print("+--------------------------------+")
            print(f"Produto cadastrado com ID: {produtos[-1]['ID']}")
            print("+--------------------------------+")
        
        elif opMenu == '5':
            idEscolhidoParaAtualizarProduto = int(input("Digite o ID do produto que deseja atualizar: "))
            atualizarProduto(produtos, idEscolhidoParaAtualizarProduto)
        elif opMenu == '6':
            idEscolhidoParaExcluirProduto = int(input("Digite o ID do produto que deseja excluir: "))
            excluirProduto(produtos, idEscolhidoParaExcluirProduto)
        elif opMenu == '7':
            # Salva os produtos no arquivo antes de sair do programa
            salvarProdutos(produtos)
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
