while True:
    q = float(input("Ваш возвраст: "))
    print()
    if q < 18:
        print(' Вам еще нет 18 лет!')
        break
    a = int(input("Количество денег: " + str("грн ")))
    print()
    if a > 100:
        print("Ошибка! Нельзя поставить больше чем 100 лет")
    if a < 0 or a == 0:
        print("Ты что-то сделал не так")
        break
    b = int(input("Количество месяцев(Не больше 12.): "))
    print()
    if b > 12 or b < 0:
        print("Ты что-то сделал не так")
        break
    c = int(input("Количество годов: "))
    if q >= 18 and q < 23:
        print("Ваш вклад 'молодежный', (11% годовых)")
        print()
        for i in range(c):
            a = a + a * 0.11
        for j in range(b):
            v = a * 0.11 / 12 * b
        a = v + a
    if q >= 23 and q <= 60:
        print("Ваш вклад 'стандарт',  (10% годовых)")
        print()
        for i in range(c):
            a = a + a * 0.1
        for j in range(b):
            v = a * 0.1 / 12 * b
        a = v + a
    if q >= 61:
        print("Ваш вклад 'пеньсионый', (12% годовых)")
        print()
        for i in range(c):
            a = a + a * 0.12
        for j in range(b):
            v = a * 0.12 / 12 * b
        a = v + a
    print()
    if c == 0 and b == 0:
        print("Ты что-то сделал не так")
        break
    if c < 0:
        print("Ты что-то сделал не так")
        break
    print("Через", c, "год(а)/лет и", b, "месяцев у вас будет",  round(a, 2), "грн.")
    print()
    print("Команда '?' покажет список команд.")
    print()
    w = str(input(""))
    if w == "?":
        print("dol - посмотреть сколько у вас будет долоров через введеное время(вверху).")
        print()
        print("end - конец работы.")
        print()
        m = str(input(""))
    if m == "end":
        print("Работа окончена.")
        break
    if m == "dol":
        n = a / 37.43
        print("У вас будет", round(n, 2), "$")
        print()

