#5 19 32
#36 10 72 4 50


amount, ideal_weigh, time = list(map(int, input().split()))
# amount, ideal_weigh, time = 4, 25, 10

sculptures = list(map(int, input().split()))
# sculptures = [1, 10, 42, 9]

result = []

w_tuple = [(num, abs(ideal_weigh - weight)) for num, weight in enumerate(sculptures, start=1)]
sorted_weight = (sorted(w_tuple, key=lambda x: x[1]))

for sculpture in sorted_weight:
    number = sculpture[0]
    weight = sculpture[1]
    if weight == 0:
        result.append(number)
    elif weight <= time:
        time -= weight
        result.append(number)
    else:
        break

print(len(result))
if result:
    print(*result)
