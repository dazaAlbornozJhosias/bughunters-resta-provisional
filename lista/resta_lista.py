"""
Equipo: Bug Hunters (eq02) | HU: HU-201
Encargado: [Persona D]
"""

def resta_lista(numeros: list) -> float:
    """Resta encadenada de todos los numeros de una lista: n1 - n2 - n3 - ..."""
    # TODO: implementar
    if not numeros:
        raise ValueError("La lista no puede estar vacia.")
            
    resultado = numeros[0]
    for elemento in numeros[1:]:
        resultado -= elemento
                
    return resultado
