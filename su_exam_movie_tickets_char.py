# Въвеждане на целите числа a1, a2 и n от потребителя
a1 = int(input())
a2 = int(input())
n = int(input())

# Проверка за валидност на входните данни
if not (65 <= a1 <= 89) or not (66 <= a2 <= 91) or not (1 <= n <= 10):
    pass
else:
    # Итерираме през символите с ASCII кодове от a1 до a2 - 1
    for char_code in range(a1, a2):
        char1 = chr(char_code)  # Преобразуваме ASCII кода в символ

        # Итерираме през цифрите от 1 до n - 1 за символ 2
        for digit2 in range(1, n):
            # Итерираме през цифрите от 1 до n // 2 - 1 за символ 3
            for digit3 in range(1, n // 2):
                char4 = str(char_code)  # Преобразуваме ASCII кода на символ 1 в низ

                # Проверка дали числовата репрезентация на символ 1 е нечетна
                if char_code % 2 != 0:
                    # Изчисляваме сбора на символ 2, символ 3 и символ 4
                    total = digit2 + digit3 + int(char4)

                    # Проверка дали сборът е нечет
                    # Проверка дали сборът е нечетен
                    if total % 2 != 0:
                        # Генерираме и отпечатваме билетния номер
                        ticket_number = f"{char1}-{digit2}{digit3}{char4}"
                        print(ticket_number)
