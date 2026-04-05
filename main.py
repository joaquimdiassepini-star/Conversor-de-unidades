
def km_to_miles(km):
    return km * 1.609344

def miles_to_km(miles):
    return miles / 1.609344

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

def main():
    print("Bem-vindo ao Conversor de Unidades!")
    print("Escolha a conversão desejada:")
    print("1. Km para Milhas")
    print("2. Milhas para Km")
    print("3. Celsius para Fahrenheit")
    print("4. Fahrenheit para Celsius")
    print("5. Kg para Libras")
    print("6. Libras para Kg")

    choice = input("Digite o número da conversão: ")

    if choice == '1':
        km = float(input("Digite a distância em Km: "))
        print(f"{km} Km é igual a {km_to_miles(km)} Milhas.")
    elif choice == '2':
        miles = float(input("Digite a distância em Milhas: "))
        print(f"{miles} Milhas é igual a {miles_to_km(miles)} Km.")
    elif choice == '3':
        celsius = float(input("Digite a temperatura em Celsius: "))
        print(f"{celsius}°C é igual a {celsius_to_fahrenheit(celsius)}°F.")
    elif choice == '4':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        print(f"{fahrenheit}°F é igual a {fahrenheit_to_celsius(fahrenheit)}°C.")
    elif choice == '5':
        kg = float(input("Digite o peso em Kg: "))
        print(f"{kg} Kg é igual a {kg_to_pounds(kg)} Libras.")
    elif choice == '6':
        pounds = float(input("Digite o peso em Libras: "))
        print(f"{pounds} Libras é igual a {pounds_to_kg(pounds)} Kg.")
    else:
        print("Opção inválida. Por favor, escolha um número entre 1 e 6.")

main()
