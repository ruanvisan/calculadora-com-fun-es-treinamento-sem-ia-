print ("calculadora")


def inserir_a():
    a = int(input("escreva seu primeiro numero: "))
    return a

primeiro = inserir_a()

print ("a operação esta: " , primeiro)

def inserir_b():
    b = int(input("escreva o segundo numero: "))
    return b

segundo = inserir_b()
print ("a operação esta: " , primeiro, "?", segundo)

def operacao():
   print ("escolha a operacao:\n" 
   "1 - soma\n" \
   "2 - subtracao\n" \
   "3 - mutiplicacao\n" \
    "4 - divicao\n")
   escolha = int(input())
   return escolha

op = operacao()

if op == 1:
    simbolo = "+"
    resultado = primeiro + segundo
elif op == 2:
    simbolo = "-"
    resultado = primeiro - segundo
elif op == 3:
    simbolo = "*"
    resultado = primeiro * segundo
elif op == 4:
    simbolo = "/"
    if segundo != 0:
        resultado = primeiro / segundo
    else:
        resultado = "Erro (divisão por zero)"
else:
    simbolo = "?"
    resultado = "Operação inválida"

print("A operação é:", primeiro, simbolo, segundo)
print("Resultado:", resultado)