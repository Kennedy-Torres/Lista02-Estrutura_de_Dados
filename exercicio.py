import os
import re
import getpass

# Função para carregar os produtos a partir do arquivo
def carregarProdutos():
    produtos = []
    if os.path.exists('produtos.txt'):
        with open('produtos.txt', 'r') as file:
            for linha in file:
                if linha.startswith('ID: '):
                    id_str = linha.split(': ')[1].split(',')[0]
                    id = int(id_str)
                    nome = linha.split('Nome: ')[1].split(',')[0]
                    peso = float(linha.split('Peso: ')[1].split(',')[0])
                    valor = float(linha.split('Valor: ')[1].split(',')[0])
                    fornecedor = linha.split('Fornecedor: ')[1].strip()

                    produto = {'ID': id, 'Nome': nome, 'Peso': peso, 'Valor': valor, 'Fornecedor': fornecedor}
                    produtos.append(produto)
    return produtos

# Função para salvar os produtos no arquivo
def salvarProdutos(produtos):
    with open('produtos.txt', 'w') as file:
        for produto in produtos:
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

# Função para atualizar os dados do produto escolhido pelo usuário com base no ID
def atualizarProduto(produtos, idEscolhidoParaAtualizarProduto):
    for produto in produtos:
        if produto['ID'] == idEscolhidoParaAtualizarProduto:
            print(f"Produto atual: {produto}")
            novo_nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ")
            
            while True:
                novo_peso_input = input("Digite o novo peso (ou pressione Enter para manter o atual): ")
                if novo_peso_input == '':
                    break
                if re.match(r'^[0-9.]+$', novo_peso_input):
                    novo_peso = float(novo_peso_input)
                    break
                else:
                    print("Peso inválido. Certifique-se de que você digitou um valor numérico válido.")
            
            while True:
                novo_valor_input = input("Digite o novo valor (ou pressione Enter para manter o atual): ")
                if novo_valor_input == '':
                    break
                if re.match(r'^[0-9.]+$', novo_valor_input):
                    novo_valor = float(novo_valor_input)
                    break
                else:
                    print("Valor inválido. Certifique-se de que você digitou um valor numérico válido.")
            
            novo_fornecedor = input("Digite o novo fornecedor (ou pressione Enter para manter o atual): ")
            
            if novo_nome:
                produto['Nome'] = novo_nome
            if novo_peso_input:
                produto['Peso'] = novo_peso
            if novo_valor_input:
                produto['Valor'] = novo_valor
            if novo_fornecedor:
                produto['Fornecedor'] = novo_fornecedor

            print("Produto atualizado com sucesso!")
            return
    
    print(f"Nenhum produto encontrado com o ID {idEscolhidoParaAtualizarProduto}.")

def adicionarUsuario(nome_sobrenome_usuario, senha):
    with open('usuario.txt', 'a') as file:
        file.write(f"Nome: {nome_sobrenome_usuario}, Senha: {senha}\n")
        
def validarLogin(nome_sobrenome_usuario, senha):
    with open('usuario.txt', 'r') as file:
        for line in file:
            if f"Nome: {nome_sobrenome_usuario}, Senha: {senha}" in line:
                return True
    return False

def leValidaMetodo():
    metodo_escolhido = input("MÉTODOS:\n(a) - Bubble Sort\n(b) - Insertion Sort\n(c) - Selection Sort\nEscolha o método (a, b, c): ").lower()
    while metodo_escolhido not in ['a', 'b', 'c']:
        print("Opção inválida para o método. Tente novamente.")
        metodo_escolhido = input("MÉTODOS:\n(a) - Bubble Sort\n(b) - Insertion Sort\n(c) - Selection Sort\nEscolha o método (a, b, c): ").lower()
    return metodo_escolhido

def leValidaOrdem():
    ordem = input("ORDEM:\n(d) - crescente\n(e) - decrescente\nEscolha a ordem (d, e): ").lower()
    while ordem not in ['d', 'e']:
        print("Opção inválida para a ordem. Tente novamente.")
        ordem = input("ORDEM:\n(d) - crescente\n(e) - decrescente\nEscolha a ordem (d, e): ").lower()
    return ordem

def leValidaCampo():
    campo_ordenacao = input("CAMPO:\n (f) - ID\n(g) - Nome\n(h) - Peso\n(i) - Valor\n(j) - Fornecedor\nEscolha o campo (f, g, h, i, j): ").lower()
    while campo_ordenacao not in ['f', 'g', 'h', 'i', 'j']:
        print("Campo de ordenação inválido. Tente novamente.")
        campo_ordenacao = input("CAMPO:\n (f) - ID\n(g) - Nome\n(h) - Peso\n(i) - Valor\n(j) - Fornecedor\nEscolha o campo (f, g, h, i, j): ").lower()
    return campo_ordenacao

def crescente(produtos_ordenados, campo_ordenacao):
    chave_ordenacao = campo_ordenacao
    produtos_ordenados = sorted(produtos_ordenados, key=lambda x: x[chave_ordenacao])

def decrescente(produtos_ordenados, campo_ordenacao):
    chave_ordenacao = campo_ordenacao
    produtos_ordenados = sorted(produtos_ordenados, key=lambda x: x[chave_ordenacao], reverse=True)

def bubble_sort(produtos, chave):
    qtd_produtos = len(produtos)
    for i in range(qtd_produtos-1):
        for j in range(0, qtd_produtos-i-1):
            if produtos[j][chave] > produtos[j+1][chave]:
                produtos[j], produtos[j+1] = produtos[j+1], produtos[j]

def insertion_sort(produtos, chave):
    for i in range(1, len(produtos)):
        chave_atual = produtos[i][chave]
        j = i-1
        while j >= 0 and chave_atual < produtos[j][chave]:
            produtos[j+1] = produtos[j]
            j -= 1
        produtos[j+1] = produtos[i]

def selection_sort(produtos, chave):
    qtd_produtos = len(produtos)
    for i in range(qtd_produtos):
        min_idx = i
        for j in range(i + 1, qtd_produtos):
            if produtos[j][chave] < produtos[min_idx][chave]:
                min_idx = j
        produtos[i], produtos[min_idx] = produtos[min_idx], produtos[i]

def listarProdutosOrdenados(produtos, metodo, ordem, campo):
    dicionarioCampo = {'f': 'ID', 'g': 'Nome', 'h': 'Peso', 'i': 'Valor', 'j': 'Fornecedor'}
    campo_ordenacao = dicionarioCampo[campo]

    produtos_copia = produtos.copy()

    if metodo == 'a':
        bubble_sort(produtos_copia, campo_ordenacao)
    elif metodo == 'b':
        insertion_sort(produtos_copia, campo_ordenacao)
    elif metodo == 'c':
        selection_sort(produtos_copia, campo_ordenacao)

    if ordem == 'e':
        produtos_copia.reverse()

    if produtos_copia:
        for produto in produtos_copia:
            print(produto)
    else:
        print("Nenhum produto para listar.")

def excluirProduto(produtos, idEscolhidoParaExcluirProduto):
    for produto in produtos:
        if produto['ID'] == idEscolhidoParaExcluirProduto:
            produtos.remove(produto)
            print(f"Produto com ID {idEscolhidoParaExcluirProduto} excluído com sucesso.")
            return

    print(f"Nenhum produto encontrado com o ID {idEscolhidoParaExcluirProduto}.")

def main():
    produtos = carregarProdutos()
    
    logado = False
    
    while not logado:
        opcao = input("1 - Cadastrar usuário\n2 - Fazer login\n3 - Sair\nEscolha uma opção: ") 
        
        if opcao == '1':
            
            cadastroUsuario = input("Cadastre um nome de usuário: ")
            cadastroSenha = getpass.getpass("Cadastre uma senha: ")
            adicionarUsuario(cadastroUsuario, cadastroSenha)
        elif opcao == '2':
            nomeSobrenome = input("Digite seu nome e sobrenome: ")
            senha = getpass.getpass("Digite sua senha: ")
            if validarLogin(nomeSobrenome, senha):
                print("Acesso permitido. Bem-vindo")
                logado = True
            else:
                print("Acesso negado, tente novamente.")
        elif opcao == '3':
            exit(1)

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
            metodo_escolhido = leValidaMetodo()
            ordem_escolhida = leValidaOrdem()
            campo_ordenacao = leValidaCampo()
            listarProdutosOrdenados(produtos, metodo_escolhido, ordem_escolhida, campo_ordenacao)
        elif opMenu == '4':
            nomeProduto = input("Digite o nome do produto: ")

            while True:
                pesoProduto_input = input("Digite o peso do produto: ")
                if re.match(r'^[0-9.]+$', pesoProduto_input):
                    pesoProduto = float(pesoProduto_input)
                    break
                else:
                    print("Peso inválido. Certifique-se de que você digitou um valor numérico válido.")

            while True:
                valorProduto_input = input("Digite o valor do produto: ")
                if re.match(r'^[0-9.]+$', valorProduto_input):
                    valorProduto = float(valorProduto_input)
                    break
                else:
                    print("Valor inválido. Certifique-se de que você digitou um valor numérico válido.")

            fornecedorProduto = input("Informe o fornecedor do produto: ")
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
            salvarProdutos(produtos)
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()