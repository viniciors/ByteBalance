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
    
def imc(peso, altura):              #Realiza o cálculo do IMC de acordo com as informações fornecidas no cadastro
    imc = peso / altura ** 2
    return imc

def classificacaoImc(imc):          #Filtra o IMC para fornecer uma classificação
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
    cadastro()
    exibeMenu()
    while True:
        try:
            opcao = int(input("Navegue pelo sistema. Escolha uma opção acima: "))
            if opcao == 0:
                print("Sistema encerrado.")
                break

            elif opcao == 1:
                resultadoImc = imc(peso, altura)
                print(f"O seu Índice de Massa Corporal é {resultadoImc:.2f}, e sua classificação é {classificacaoImc(resultadoImc)}.")

            elif opcao == 2:
                resultadoAgua = copoDeAgua(peso)
                print(f"Você devem ingerir uma quantidade de {resultadoAgua:.2f}L.")

            elif opcao == 3:
                somaCalorias(caloriasAlimento)

            else:
                print("Opção inválida.")
        except ValueError:
            print("ERRO. É necessário digitar um número inteiro.")

caloriasAlimento = {"abobrinha": 33, "beterraba cozida": 35, "morango": 4, "guacamole": 120, "queijo ricota": 174, "sopa de ervilha": 82, "maçã verde": 95,
    "azeite de abacate": 120, "café preto": 2, "abacaxi em cubos": 83, "berinjela": 20, "barra de cereal": 100, "cebola verde": 32,
    "manteiga de amendoim": 94, "tomate-cereja": 15, "ovos mexidos": 92, "alho-poró": 54, "tangerina": 47, "tempeh": 195, "couve-de-bruxelas": 38,
    "vinagre balsâmico": 14, "sorvete de baunilha": 137, "baguete integral": 82, "panquecas de trigo integral": 154, "muffin de mirtilo": 240,
    "pasta de amendoim": 190, "sopa de peixe": 230, "brócolis cozidos no vapor": 55, "camarão grelhado": 84, "frango assado": 165, 
    "lasanha de espinafre": 215, "frutas cítricas": 60, "bagel de grãos inteiros": 200, "pepino em conserva": 2, "pão de centeio": 65,
    "hummus": 27, "aspargo assado": 232, "peru assado": 135, "salada de frutas": 120, "molho de tomate": 30, "barra de proteína": 200, "repolho roxo": 22,
    "queijo feta": 99, "uvas vermelhas": 69, "alho-poró": 54, "molho de soja": 8, "batata assada": 130, "sopa de legumes": 80, "bife grelhado": 250,
    "abacate em fatias": 50, "purê de abóbora": 49, "cevada": 354, "vagem": 30, "lentilhas": 230, "mousse de chocolate": 250, "batata frita": 365,
    "biscoitos integrais": 50, "feijão cozido": 225, "beterraba": 35, "melão": 50, "kiwi": 61, "muffin de banana": 134, "frango ao curry": 260,
    "arroz frito": 235, "tortilla integral": 50, "iogurte de coco": 120, "arroz basmati": 190, "camarão scampi": 240, "geléia de morango": 50,
    "hamburguer de peru": 220, "chá de camomila": 2, "manteiga de amêndoa": 98, "baguete de trigo integral": 250, "alho-poró": 54,
    "molho de maçã": 49, "peito de frango assado": 165, "muffin inglês integral": 140, "sopa de abóbora": 80, "abacate": 234,
    "queijo suíço": 106, "toranja": 52, "repolho chinês": 15, "pepitas de abóbora": 30, "ravióli de queijo": 220, "pera cozida": 100,
    "sopa de cogumelos": 66, "quinoa": 222, "pepino em fatias": 8, "leite de amêndoa": 60, "queijo suíço": 106, "chá de hortelã": 2,
    "rabanete": 12, "tapioca": 96, "pimentão vermelho": 31, "hambúrguer vegetariano": 150, "avelã": 176, "azeitona verde": 4,
    "salsicha italiana": 230, "pão pita integral": 80, "uva passa": 299, "sopa de feijão": 200, "torta de maçã": 250,
    "bagel de mirtilo": 250, "chucrute": 19, "sopa de tomate": 74,"banana": 105, "maçã": 95, "arroz": 130, "frango": 165, "batata": 110,
    "cenoura": 30, "salada": 15, "iogurte": 150, "pão integral": 70, "salmão": 206, "abacate": 240, "espinafre": 23, "ovos cozidos": 68,
    "aveia": 150, "alface": 5,  "queijo cheddar": 110, "tomate": 22, "pêssego": 59, "melancia": 30, "abacaxi": 50, "pistache": 156,
    "morango": 4, "brócolis": 55, "pera": 100, "uva": 69, "castanha-do-pará": 69, "atum enlatado": 179, "kiwi": 61, "cenoura cozida": 54,
    "sopa de lentilha": 165}            #Dicionário com alguns alimentos e suas calorias

main()
