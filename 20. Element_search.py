# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
import random

def busqueda_binaria(lista, comienzo, final, objetivo):
  if (comienzo > final):
    return False

  medio = (comienzo + final) //2
  if lista [medio] == objetivo:
    return True
  elif lista[medio] < objetivo:
    return busqueda_binaria(lista, medio+1, final, objetivo)
  else:
    busqueda_binaria(lista, comienzo, medio-1, objetivo)

if __name__ == '__main__':
  tamano_lista = int(input('De qué tamaño es la lista? '))
  objetivo = int(input('Número a encontrar: '))
  lista = sorted([random.randint(0, 100) for i in range(0, tamano_lista)])

  encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

  print(lista)
  print('el elemento {} {} en la lista'.format(objetivo, 'esta' if encontrado else 'no está'))

