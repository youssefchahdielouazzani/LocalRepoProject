# calculator.py

print("Bienvenue dans la calculatrice simple !")

# Demander les nombres et l'opération
num1 = float(input("Entrez le premier nombre : "))
op = input("Entrez l'opération (+, -, *, /) : ")
num2 = float(input("Entrez le deuxième nombre : "))

# Effectuer le calcul
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Erreur : division par zéro !"
else:
    result = "Opération invalide !"

print("Résultat :", result)
