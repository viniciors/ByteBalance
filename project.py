def apresentacao():
    print("""
            Bem Vindo ao ByteBalance!
      
            Este programa traz uma calculadora de IMC, uma calculadora de quantidade de água a ser ingerida e um contador de calorias.
            Tudo isso integrado tem o objetivo e ajudar a trazer uma rotina mais saudável a quem o utiliza.
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

def copoDeAgua(peso):
   quantidade = peso * 0.035
   return quantidade

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


