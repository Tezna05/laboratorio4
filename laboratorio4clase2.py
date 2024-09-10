from decimal import Decimal, getcontext
# Establecemos un contexto de precisión alta
getcontext().prec = 50
# Realizamos una operación matemática precisa
numero1 = Decimal('1.123456789123456789')
numero2 = Decimal('2.987654321987654321')
resultado = numero1 * numero2
# Mostramos el resultado con alta precisión
print(f"Resultado preciso: {resultado}")

