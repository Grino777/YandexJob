AMOUNT_OF_DEALS = 4

# amount_of_days = int(input())
amount_of_days = 6

def get_min_price(sp):
    temp = sp[0]
    for i in sp:
        if i[1] <= temp[1]:
            temp = i
    return temp

def max_price(sp):
    temp = sp[0]
    for i in sp:
        if i[1] >= temp[1]:
            temp = i
    return temp

# price_per_day = tuple((day, int(price)) for day, price in enumerate(input().split(), start=1))
price_per_day = [(1, 1), (2, 4), (3, 2), (4, 3), (5, 3), (6, 5)] #[1 4 2 3 3 5]

sorted_price_per_day = [sorted(price_per_day, key=lambda x: x[1])]

def get_result(sp):
    temp = (0, 0)
    res = []
    min_price = get_min_price(sp)
    for price in sp[min_price[0]:]:
        if price[1] - min_price[1] >= temp[1]:
           res.append(price)
           if sp[price[0]:]:
               get_result(sp[price[0]:])
    return res

print(get_result(price_per_day))
