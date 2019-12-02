def calculateFuel(mass):
  return (int(mass) // 3) - 2

print(sum(list(map(calculateFuel, open("day1input.txt")))))
