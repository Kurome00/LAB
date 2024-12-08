import math

def radians_to_degrees(radians):
    return radians * (180 / math.pi)

def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)

def main():
    while True:
        print("Выберите действие:")
        print("1. Перевести радианы в градусы")
        print("2. Перевести градусы в радианы")
        print("3. Выход")

        choice = input("Введите номер действия (1/2/3): ")

        if choice == '1':
            radians = float(input("Введите величину в радианах: "))
            degrees = radians_to_degrees(radians)
            print(f"{radians} радиан = {degrees} градусов")

        elif choice == '2':
            degrees = float(input("Введите величину в градусах: "))
            radians = degrees_to_radians(degrees)
            print(f"{degrees} градусов = {radians} радиан")

        elif choice == '3':
            print("Выход из программы.")
            break

        else:
            print("Неверный ввод. Пожалуйста, выберите 1, 2 или 3.")

if __name__ == "__main__":
    main()
    
