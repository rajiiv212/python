from itertools import count


class sample:
    count = 0

    def increase(self):
        sample.count += 1

s1 = sample()
s1.increase()
s1.increase()
print(s1.count)

s2 = sample()
s2.increase()
print(s2.count)