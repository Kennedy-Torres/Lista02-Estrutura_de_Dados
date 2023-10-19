#CONDIÇÕES
#validações de menu (ex: Opção inválida para cada entrada)
#Em uma lista (produtos) cada elemento será um dicionário (produto) ... ok
#

import os

# Função para carregar os produtos a partir do arquivo
def carregarProdutos():
    produtos = []#lista de produtos que armazena produto[] -> logo armazena dicionários
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

# Função para listar produtos em ordem alfabética (crescente ou decrescente)
def listarProdutosOrdemAlfabetica(produtos, ordem='crescente'):
    if ordem == 'crescente':
        produtos_ordenados = sorted(produtos, key=lambda x: x['Nome'])
    elif ordem == 'decrescente':
        produtos_ordenados = sorted(produtos, key=lambda x: x['Nome'], reverse=True)
    else:
        print("Opção inválida para a ordem de classificação.")
        return

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
                7. Sair do programa
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
            ordem = input("Digite 'crescente' para ordem crescente ou 'decrescente' para ordem decrescente: ").lower()
            listarProdutosOrdemAlfabetica(produtos, ordem)
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
