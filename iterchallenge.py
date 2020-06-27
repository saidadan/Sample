shopping = ["ball", "milk", "rolls", "bag"]
my_iter = iter(shopping)
for i in range(0, len(shopping)):
    next_item = next(my_iter)
    print(next_item)
