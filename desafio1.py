print("\n------------Bem vindo a Verificação de TIPO ---------------")
print("Vamos iniciar digitando os dados iniciais para retornar seus resultados")

#Entrada de dados - Declaração de Variáveis
nome = input("\nDigite o seu nome: ")
idade = int(input("Digite a sua idade: "))
anoNascimento = int(input("Digite o ano do seu nascimento: "))
nomeCidade = input("Digite o nome da sua cidade: ")

#Saída de dados - Informação Completa do Usuário.
print("- - - - -"*5)
print(f"\n\t\tO seu nome é {nome}. \n\t\t\tTipo: {type(nome)}.\n\t\tVocê tem {idade} anos. \n\t\t\tTipo: {type(idade)}.\n\t\tVocê nasceu em {anoNascimento}. \n\t\t\tTipo: {type(anoNascimento)}.\n\t\tO nome da cidade em que você reside é: {nomeCidade} \n\t\t\tTipo: {type(nomeCidade)}\n")
print("- - - - -"*5)
