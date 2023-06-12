from classe import *

def exibir_menu():
    print()
    print('='*42)
    print("="*10,'SISTEMA DE REGISTROS','='*10)
    print('='*42)
    print("\nMenu:\n")
    print("1. Cadastrar animal")
    print("2. Cadastrar pessoa interessada")
    print("3. Pesquisar animais disponíveis")
    print("4. Pesquisar pessoas")
    print("5. Gerar relatório")
    print("6. Sair\n")
    print('='*42)

# Instanciar a classe Prefeitura
prefeitura = Prefeitura()

while True:
    exibir_menu()
    escolha = input("\nEscolha uma opção: ")


    if escolha == "1":
        tipo = input('\nTipo do animal: ').lower()
        idade = input("\nIdade do animal: ").lower()
        cor = input("\nCor do animal: ").lower()
        porte = input("\nPorte do animal: ").lower()
        particularidade = input("\nParticularidade do animal: ").lower()
        prefeitura.cadastrar_animal(tipo, idade, cor, porte, particularidade)
        print()
        print('='*42)
        print("Animal cadastrado com sucesso!")
        print('='*42)

    elif escolha == "2":
        nome = input("\nNome da pessoa interessada: ").lower()
        contato = input("\nContato da pessoa interessada: ").lower()
        especie_interesse = input("\nEspécie da interesse da pessoa: ").lower()
        preferencia = input("\nPreferência da pessoa (opcional): ").lower()
        prefeitura.cadastrar_pessoa_interessada(nome, contato, especie_interesse, preferencia)
        print()
        print('='*42)
        print("\nPessoa interessada cadastrada com sucesso!")
        print('='*42)

    elif escolha == "3":
        #especie = input("Espécie a pesquisar: ")
        #preferencia = input("Preferência (opcional): ")
        
        prefeitura.pesquisar_animal()
        #if animais_encontrados:
         #   print("Animais disponíveis:")
          #  for animal in animais_encontrados:
           #     print(f"Tipo: {animal.tipo}")
            #    print(f"Idade: {animal.idade}")
             #   print(f"Cor: {animal.cor}")
              #  print(f"Porte: {animal.porte}")
               # print(f"Particularidade: {animal.particularidade}")
                #print("----------")
        #else:
         #   print("Nenhum animal encontrado.")
    
    elif escolha == "4":
        pessoa = input("\nDigite o nome da pessoa: ").lower()
        pessoa_encontrada = prefeitura.pesquisar_pessoas(pessoa)
        if pessoa_encontrada:
            print("Pessoas: ")
            for pessoa in pessoa_encontrada:
                print(f"Tipo: {pessoa.nome}")
                print(f"Idade: {pessoa.contato}")
                print(f"Cor: {pessoa.especie_interesse}")
                print(f"Porte: {pessoa.preferencia}")
                print("----------")
        else:
            print("Nenhum dado encontrado.")

    elif escolha == "5":
        prefeitura.gerar_relatorio()

    elif escolha == "6":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Escolha novamente.")
