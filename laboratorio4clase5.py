# Función que combina valores numéricos y maneja valores nulos
def sumar_o_default(a, b):
    # Si uno de los valores es None, retornamos 0 como valor predeterminado
    return (a or 0) + (b or 0)

# Ejemplo con diferentes combinaciones de enteros y valores None
print(sumar_o_default(5, None))  # Debería retornar 5
print(sumar_o_default(None, None))  # Debería retornar 0
print(sumar_o_default(10, 20))  # Debería retornar 30
