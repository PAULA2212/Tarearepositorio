from ejerciciov1 import sum
operacion=("suma"| "resta" | "multiplicacion")
def calcular_resultado(n1,n2):
    if operacion=="suma":
        resultado = sum(n1,n2)
    return f'el resultado de esta operacion es {resultado}'
