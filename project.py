def apresentacao():
    print("""
            Bem Vindo ao ByteBalance!
      
            Este programa traz uma calculadora de IMC, uma calculadora de quantidade de água a ser ingerida e um contador de calorias.
            Tudo isso integrado tem o objetivo e ajudar a trazer uma rotina mais saudável a quem o utiliza.
          """)

def cadastro():                     #Realiza um cadastrado para que o usuário possa acessar o programa
    dadosUsuario = []
    print("""
            Para começar a utilizar o sistema, faça um simples cadastro com algumas poucas informações.
          """)
    
    nome = input("Digite seu nome completo: ")
    while not nome.replace(" ", "").isalpha():      #Verifica se o nome é composto apenas pro letras
        print("ERRO. O nome deve conter apenas letras.")
        nome=input("Digite seu nome completo: ")
 
    email = input("Digite o seu email: ")
    while "@" not in email or "." not in email or " " in email:         #Verifica se o email contém '@', '.' e não contém 'espaço'
        print("ERRO. O email deve ser válido.")
        email = input("Digite um email válido: ")
 
    while True:                             #Trata entradas que não sejam números inteiros
        try:
            idade = int(input("Digite sua idade: "))
            break
        except ValueError:
            print("ERRO. A idade deve ser preenchida com números inteiros.")
 
    global peso
    while True:                             #Trata entradas que não sejam números
        try:
            peso = float(input("Digite o seu peso em Kg: "))
            break
        except ValueError:
            print("ERRO. O peso deve ser preenchido com números.")
 
    global altura
    while True:                             #Trata entradas que não sejam números                       
        try:
            altura = float(input("Digite sua altura em M: "))
            break
        except ValueError:
            print("Erro. A altura deve ser preenchida com números e em metros.")
 
    usuario = {
            "Nome": nome,
            "Email": email,
            "idade": idade,
            "Peso": peso,
            "Altura": altura
    }
    dadosUsuario.append(usuario)
    print("Cadastro efetuado com sucesso.")
    print(f"Dados Cadastrados: {dadosUsuario}")

def exibeMenu():
    print("""
                 ----------------------------------
                |                                  |
                |  1. Descubra o seu IMC           |
                |  2. Quanta água deve consumir    |
                |  3. Contador de Calorias         |
                |  0. Encerrar o aplicativo        |
                |                                  |
                 ----------------------------------
          """)
    
def imc(peso, altura):
    imc = peso / altura ** 2
    return imc

def classificacaoImc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    
    elif 18.5 < imc < 24.9:
        return "Peso adequado"
    
    elif 25 <= imc < 30:
        return "Sobrepeso" 
    
    elif 30 < imc < 35:
        return "Obesidade Grau 1"
    
    elif 35 < imc < 40:
        return "Obesidade Grau 2"
    
    elif imc > 40:
        return "Obesidade extrema"

def copoDeAgua(peso):               #Calcula a quantidade de água a ser ingerida de acordo com as informações fornecidas no cadastro
   quantidade = peso * 0.035
   return quantidade

def verificaAlimento(alimento, caloriasAlimento):  # Verifica se o alimento está no dicionário criado
    if alimento in caloriasAlimento:
        return caloriasAlimento[alimento]
    
    else:
        return 0

def somaCalorias(caloriasAlimento):                # Inicia um loop para o usuário digitar o alimento e ver a soma total de calorias consumidas
    caloriasTotais = 0
 
    while True:
        alimento = input("Digite o nome do alimento para calcular as calorias ou 'sair' para encerrar: ").lower()
 
        if alimento == 'sair':
            break
        
        caloriasAlimentoAtual = verificaAlimento(alimento, caloriasAlimento)
 
        caloriasTotais += caloriasAlimentoAtual
 
        if caloriasAlimentoAtual != 0:
            print(f"Calorias do {alimento}: {caloriasAlimentoAtual}")
 
        else:
            print("Alimento não encontrado no banco de dados.")
 
    print(f"Calorias totais: {caloriasTotais}")
    
def main():
    peso = float(input("Digite seu peso em Kg: "))
    altura = float(input("Digite sua altura em m: "))
    resultado = imc(peso, altura)
    classificacao = classificacaoImc(resultado)
    quantidade = copoDeAgua(peso)
    print(f"Seu IMC é {resultado:.2f}")
    print(f"Sua classificação é {classificacao}")
    print(f"Você deve tomar {quantidade:.2f}")

main()


