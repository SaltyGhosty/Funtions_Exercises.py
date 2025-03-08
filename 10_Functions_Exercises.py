


def personalized_greeting():
    desconocido = str(input("Cual es tu nombre? "))
    print(f"Hola, {desconocido}!")
    if desconocido == str(""):
        print("Hola, desconocido!")

personalized_greeting()



def multiply(first_number, second_number):
    product = (first_number * second_number)
    return product

my_result = multiply(5, 5)
print(my_result)


#3

def is_even(par_number):
    if par_number % 2 == 0:
        return True
    else:
        return False
print(is_even(16))

#4

def convert_to_uppercase(*textos):
    for texto in textos:
        print(texto.upper())

convert_to_uppercase("SaltyGhosty")

#5

def arbitrary_sum(*numbers):
    return sum(numbers)

print(arbitrary_sum(1, 2, 3, 4, 5))


#6


def generate_full_greeting(name, surname):
    return f"{name} {surname}"

print("Hola " + generate_full_greeting(name = "Lucho", surname = "Labbo"))

#7

def power(first_value, second_value):
    return first_value ** second_value

first_value = 2
second_value = 6
print(power(first_value, second_value))

#8

def calculate_average(first_value, second_value, third_value):
    return (first_value + second_value + third_value) / 3

print("El promedio de la suma es", calculate_average(3, 4, 5))

#9

def count_characters(big_world):
    print(len(big_world))

count_characters("Asadito")

#10

def display_messages(*palabras):
    for palabra in palabras:
        print(palabra.upper())

display_messages("Salchicha", "Salty", "China", "Ravioli", "Anatra")
