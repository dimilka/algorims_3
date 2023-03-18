def part1():
    print("Ввод формата: номинал количество")
    s1, m1 = map(int, input('1 ').split())
    s2, m2 = map(int, input('2 ').split())
    s3, m3 = map(int, input('3 ').split())
    s4, m4 = map(int, input('4 ').split())
    z = int(input('Сумма '))
    money = sorted([[s1, m1], [s2, m2], [s3, m3], [s4, m4]], reverse=True)
    answer = []
    summ = 0
    for i in range(len(money)):
        val = money[i]
        while summ + val[0] <= z and val[1] != 0:
            summ += val[0]
            val[1] -= 1
            answer.append(val[0])
    if summ == z:
        print(f"Количество монет: {len(answer)}.\nКомбинация монет: {answer}.")
    else:
        print("Подходящей комбинации нет")





part1()