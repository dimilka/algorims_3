def part1():
    n = int(input("Количество экспонатов "))
    print("Для каждого экспоната укажите название, вес и стоимость.")
    d = {}
    for i in range(n):
        name, w, c = input(f"{i + 1}. ").split()
        w, c = int(w), int(c)
        d[c] = [name, w]
    d = dict(sorted(d.items(), key=lambda x: x[0], reverse=True))
    m = int(input("Количество заходов "))
    k = int(input(f"Вместительность "))
    summ, array = 0, []
    for _ in range(m):
        all_weight = 0
        for i in d.keys():
            if all_weight + d[i][1] <= k and d[i][0] != '':
                all_weight += d[i][1]
                summ += i
                array.append(d[i][0])
                d[i] = ['', d[i][1]]
        if len(array) == 0:
            print("Ничего украсть не удалось.")
            break
    if len(array) > 0:
        print(f"Украденная сумма: {summ}")
        print(f"Украденные экспонаты: {' '.join(array)}")


part1()