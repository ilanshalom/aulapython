# aprendendo python para desenvolver app 
nome =input ('digite seu nome')
nota = int(input('digite sua nota:'))
def multiplicacao():
    print('voce ira resolver um problema')
    a = int(input('digite um numero:'))
    b = int(input('digite um numero:'))
    resultado = a * b
    return resultado
    resposta = int(input('ual o resultado de multiplicacao' ))
    if (resposta == resultado):
     print('voce acerto!')
    else : print('voce errou')

    print('a nota de ',nome, 'sua nota é', nota)
if nota <= 5:
    print('voce foi Reprovado')
else:
    print('voce foi Aprovado')
    graduacao = input ('deseja fazer graduação')
    if graduacao == 'sim' : print('voce está matriculado!')
    else: print('ok!')
    resultado = multiplicacao ()

    nota1 = 5 
    nota2 = 9.5
    media = (nota1+nota2)/2
    nome = "ilan garcia"
    disciplina = "programação de computadores"
    print("nome do aluno:", nome)
    print("disciplina", disciplina)
    print("primeira nota =  %.2f \nsegunda nota = %.2f" %(nota1,nota2))
    nome = input("digite seu nome: ")
    idade = input("digite sua idade: ")
    print("seu nome é: ",nome)
    print("sua idade é: ", idade)
    n1 = input("informe o primeiro numero:  ")
    n2 = input("informe o segundo numero: ")
    soma = (n1+n2)
    print(soma)
    resolt = float (5*(2**2 - 5)+4*3**2-15*2)
    print(resolt)
    print('cientcias da computação')
    proffisao = input("digite sua profissão")
    print(proffisao)
    idades = input("por favor digite sua idade") 
    print(idades)    
    