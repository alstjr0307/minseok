def d(number):
    total = number
    number = str(number)
    for i in number:
        total += int(i)
    return total

self_number_total = 0
self_number_set = set()

for i in range(1,5000):
    self_number_set.add(d(i))

for i in range(1,5000):
    if not i in self_number_set:
        self_number_total += i

print(self_number_total)
