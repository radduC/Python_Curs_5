import math

numere_verificate = 0
numere_prime = 0
patrate_perfecte = 0


def is_prime(n):
    global numere_prime
    global numere_verificate

    if n <= 1:
        numere_verificate += 1
        return False
    if n <= 3:
        numere_prime += 1
        numere_verificate += 1
        return True

    if n % 2 == 0 or n % 3 == 0:
        numere_verificate += 1
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            numere_verificate += 1
            return False
        i += 6

    numere_prime += 1
    numere_verificate += 1
    return True


def is_perfect_square(n):
    global patrate_perfecte

    square_root = math.sqrt(n)
    if square_root - math.floor(square_root) == 0:
        patrate_perfecte += 1

    return square_root - math.floor(square_root) == 0


if __name__ == "__main__":
    while True:
        choice = input('Verificati numar? y/n ')

        if choice == 'y':
            numar = int(input('n = '))
            print('numar prim: ', is_prime(numar))
            print('patrat perfect ', is_perfect_square(numar))
            print('numere prime, patrate perfecte, total numere verificate: ',
                  numere_prime, patrate_perfecte, numere_verificate)
        elif choice == 'n':
            print('numere prime, patrate perfecte, total numere verificate: ',
                  numere_prime, patrate_perfecte, numere_verificate)
            break
        else:
            print('Optiune gresita')
            print('numere prime, patrate perfecte, total numere verificate: ',
                  numere_prime, patrate_perfecte, numere_verificate)
