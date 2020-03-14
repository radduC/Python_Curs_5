import my_math
import my_string

try:
    print(my_math.is_perfect_square(
        int(input('Introduceti numarul de verificat daca e patrat perfect: '))))
    print(my_math.is_prime(
        int(input('Introduceti numarul de verificat daca e prim: '))))
except ValueError:
    print('Acesta nu este un numar!')
finally:
    print(my_string.capitalize_string(input('Introduceti stringul: ')))
    print(my_string.count_letters(input('Introduceti stringul: ')))
