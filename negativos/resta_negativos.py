"""
Equipo: Bug Hunters (eq02) | HU: HU-201
Encargado: [Persona C]
"""

def resta_con_negativos():
    print("--- RESTA ENTRE NÚMEROS NEGATIVOS ---")
    
    num1 = float(input("Ingresa el primer número negativo"))
    num2 = float(input("Ingresa el segundo número negativo "))
    
   
    resultado = num1 - num2
    
    print("\n--- Desglose de la operación ---")
    print(f"Expresión inicial : {num1} - ({num2})")
    print(f"Aplicando signos  : {num1} + {abs(num2)}")
    print(f"Resultado final   : {resultado}")
    
  
    if resultado < 0:
        print("El resultado final es NEGATIVO.")
    elif resultado > 0:
        print("El resultado final es POSITIVO.")
    else:
        print("El resultado es CERO.")

if __name__ == "__main__":
    resta_con_negativos()
