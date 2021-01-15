# This time, we’re going to do exactly the opposite. You, the user,
# will have in your head a number between 0 and 100. The program
# will guess a number, and you, the user, will say whether it is
# too high, too low, or your number.

# At the end of this exchange, your program should print out how
# many guesses it took to get your number.

import random


def busqueda_binaria(lista, comienzo, final, objetivo):
  if (comienzo > final):
    return False

  medio = (comienzo + final) // 2
  res = (input(f'El número es {lista[medio]}? '))

  if res == 'yes':
    objetivo = lista [medio]
    return True
  elif res == 'muy bajo':
    return busqueda_binaria(lista, medio+1, final)
  elif res == 'muy alto':
    busqueda_binaria(lista, comienzo, medio-1)

if __name__ == '__main__':
  tamano_lista = int(input('De qué tamaño es la lista? '))
  lista = [i for i in range(0, tamano_lista)]
  objetivo = 0
  encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
  

  if encontrado:
    print('El número es: {}'.format(objetivo))
  else:
    print('El número no está en la lista')


#revisar!!