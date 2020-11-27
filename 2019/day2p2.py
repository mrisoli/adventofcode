def execute(a, i):
  if a[i] == 99:
    return (a,i)
  elif a[i] == 1:
    a[a[i + 3]] = a[a[i + 1]] + a[a[i + 2]]
  elif a[i] == 2:
    a[a[i + 3]] = a[a[i + 1]] * a[a[i + 2]]
  return (a,i + 4)

def solve(a):
  for noun in range(0,99):
    for verb in range(0,99):
      b = a[:]
      b[1],b[2],i = noun, verb, 0
      while b[i] != 99:
        b,i=(execute(b,i))
      if b[0] == 19690720:
        return 100 * noun + verb

  return 100 * a[i + 1] + a[i + 2]

print(solve(list(map(int,open("day2input.txt").read().split(",")))))
