class Animal:
    def __init__(self, tipo, idade, cor, porte, particularidade):
        self.tipo = tipo
        self.idade = idade
        self.cor = cor
        self.porte = porte
        self.particularidade = particularidade

class Pessoa:
    def __init__(self, nome, contato, especie_interesse, preferencia):
        self.nome = nome
        self.contato = contato
        self.especie_interesse = especie_interesse
        self.preferencia = preferencia

class Prefeitura:
    def __init__(self):
        self.animais = []
        self.pessoas_interessadas = []
        
    #MÉTODO PARA CADASTRAR ANIMAL PARA ADOÇÃO
    def cadastrar_animal(self, tipo, idade, cor, porte, particularidade):
        animal = Animal(tipo, idade, cor, porte, particularidade)
        self.animais.append(animal)
        
    #MÉTODO PARA CADASTRAR PESSOA INTERESSADA NA ADOÇÃO
    def cadastrar_pessoa_interessada(self, nome, contato, especie_interesse, preferencia):
        pessoa = Pessoa(nome, contato, especie_interesse, preferencia)
        self.pessoas_interessadas.append(pessoa)

    
    #MÉTODO PARA PESQUISAR ANIMAL PARA RELATÓRIO
    def pesquisar_animal_relatorio(self, especie, preferencia=None):
        animais_encontrados = []
        for animal in self.animais:
            if animal.tipo == especie:
                if preferencia is None or animal.particularidade == preferencia:
                    animais_encontrados.append(animal)
        return animais_encontrados
    
    #MÉTODO PARA PESQUISAR ANIMAIS POR TIPO/IDADE/COR/PORTE/PARTICULARIDADE  
    def pesquisar_animal(self):
        print('='*42)
        print("Menu Pesquisa Animal:")
        print("\n1. Pesquisar animal pelo tipo")
        print("\n2. Pesquisar animal pela idade")
        print("\n3. Pesquisar animail pela cor")
        print("\n4. Pesquisar animal pelo porte")
        print("\n5. Pesquisar animal pela particularidade")
        print("\n6. Sair\n")
        print('='*42)
        opcao = input('Escolha a opção de pesquisa: ')
        
        if opcao == '1':
            tipo_animal = input('\nDigite o tipo desejado: ').lower()
            print('='*42)
            print("\nAnimais encontrados:")
            contador = 0 #REGISTRAR O TOTAL DE ANIMAIS ENCONTRADOS COM ESSA CARACTERÍSTICA
            for a in self.animais:
                if a.tipo == tipo_animal:
                    contador += 1
                    print("\n----------")
                    print(f"Tipo: {a.tipo}")
                    print(f"Idade: {a.idade}")
                    print(f"Cor: {a.cor}")
                    print(f"Porte: {a.porte}")
                    print(f"Particularidade: {a.particularidade}")
            if contador == 0:
                print('\n>> Nenhum registro encontrado <<')
                 
        elif opcao == '2':
            idade_animal = input('\nDigite a idade desejada: ')
            print('='*42)
            print("\nAnimais encontrados:")
            contador = 0 #REGISTRAR O TOTAL DE ANIMAIS ENCONTRADOS COM ESSA CARACTERÍSTICA
            for a in self.animais:
                if a.idade == idade_animal:
                    contador += 1
                    print(f"\nTipo: {a.tipo}")
                    print(f"Idade: {a.idade}")
                    print(f"Cor: {a.cor}")
                    print(f"Porte: {a.porte}")
                    print(f"Particularidade: {a.particularidade}")
                    print("----------")
            if contador == 0:
                print('\n>> Nenhum registro encontrado <<')
         
        elif opcao == '3':
            cor_animal = input('\nDigite a cor desejada: ').lower()
            print('='*42)
            print("\nAnimais encontrados:")
            contador = 0 #REGISTRAR O TOTAL DE ANIMAIS ENCONTRADOS COM ESSA CARACTERÍSTICA
            for a in self.animais:
                if a.cor == cor_animal:
                    contador += 1
                    print(f"\nTipo: {a.tipo}")
                    print(f"Idade: {a.idade}")
                    print(f"Cor: {a.cor}")
                    print(f"Porte: {a.porte}")
                    print(f"Particularidade: {a.particularidade}")
                    print("----------")
            if contador == 0:
                print('\n>> Nenhum registro encontrado <<')
                    
        elif opcao == '4':
            porte_animal = input('\nDigite o porte desejado: ').lower()
            print('='*42)
            print("\nAnimais encontrados:")
            contador = 0 #REGISTRAR O TOTAL DE ANIMAIS ENCONTRADOS COM ESSA CARACTERÍSTICA
            for a in self.animais:
                if a.porte == porte_animal:
                    contador += 1
                    print(f"\nTipo: {a.tipo}")
                    print(f"Idade: {a.idade}")
                    print(f"Cor: {a.cor}")
                    print(f"Porte: {a.porte}")
                    print(f"Particularidade: {a.particularidade}")
                    print("----------")
            if contador == 0:
                print('\n>> Nenhum registro encontrado <<')
        
        elif opcao == '5':
            part_animal = input('\nDigite a prticularidade desejada: ').lower()
            print('='*42)
            print("\nAnimais encontrados:")
            contador = 0 #REGISTRAR O TOTAL DE ANIMAIS ENCONTRADOS COM ESSA CARACTERÍSTICA
            for a in self.animais:
                if a.particularidade == part_animal:
                    contador += 1
                    print(f"\nTipo: {a.tipo}")
                    print(f"Idade: {a.idade}")
                    print(f"Cor: {a.cor}")
                    print(f"Porte: {a.porte}")
                    print(f"Particularidade: {a.particularidade}")
                    print("----------")
            if contador == 0:
                print('\n>> Nenhum registro encontrado <<')
         
        else:
            print('\nNenhum animal foi encontrado com as características dessa pessoa.')
    
    
    #MÉTODO PARA PESQUISAR PESSOAS
    def pesquisar_pessoas(self, nome):
        pessoas_encontradas = []
        for pessoa in self.pessoas_interessadas:
            if pessoa.nome == nome:
                pessoas_encontradas.append(pessoa)
        return pessoas_encontradas

    #MÉTODO PARA GERAR RELATÓRIO
    def gerar_relatorio(self):
        print()
        print('='*42)
        print("="*15,'RELATÓRIO','='*15)
        print('='*42)
        contador = 1
        for pessoa in self.pessoas_interessadas:
            animais_disponiveis = self.pesquisar_animal_relatorio(pessoa.especie_interesse, pessoa.preferencia)
            print('='*21)
            print(f'Retorno {contador}')
            print(f"Nome: {pessoa.nome}")
            print(f"Contato: {pessoa.contato}")
            print('='*21)
            print(f"Animais disponíveis para >> {pessoa.nome} << :")
            contador += 1
            if len(animais_disponiveis) == 0:
                print('Nenhum animal encontrado com as características requeridas.')
            else:
                for animal in animais_disponiveis:
                    print(f"Tipo: {animal.tipo}")
                    print(f"Idade: {animal.idade}")
                    print(f"Cor: {animal.cor}")
                    print(f"Porte: {animal.porte}")
                    print(f"Particularidade: {animal.particularidade}")
                    print("----------")
        print('='*42)

