def calcFuel(m):
  return (m // 3) - 2

def calculateTotalFuel(m):
  t = a = calcFuel(int(m))
  while a >= 9:
    a = calcFuel(a)
    t += a
  return t

print(sum(list(map(calculateTotalFuel, open("day1input.txt")))))
