def part1():
    print("Ввод формата: номинал количество")
    s1, m1 = map(int, input('1 ').split())
    s2, m2 = map(int, input('2 ').split())
    s3, m3 = map(int, input('3 ').split())
    s4, m4 = map(int, input('4 ').split())
    z = int(input('Сумма '))
    money = sorted([[s1, m1], [s2, m2], [s3, m3], [s4, m4]], reverse=True)
    func(0, money, [], z)
    if len(ans_ar) == 0:
        print("Подходящей комбинации нет")
    else:
        to_print = []
        k = float("inf")
        for val in ans_ar:
            if len(val) < k:
                to_print = val
                k = len(val)
        print(f"Количество монет: {len(to_print)}.\nКомбинация: {to_print}.")


def func(sum, array, answer, lim):
    global ans_ar
    if sum == lim:
        ans_ar.append(answer)
    for i in range(len(array)):
        val = array[i]
        if val[1] != 0 and sum + val[0] <= lim:
            array_copy = array.copy()
            array_copy[i][1] -= 1
            func(sum + val[0], array, answer + [val[0]], lim)


ans_ar = []
part1()