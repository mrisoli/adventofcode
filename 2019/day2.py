def execute(a, i):
  if a[i] == 99 :
    return (a,i)
  elif a[i] == 1:
    a[a[i + 3]] = a[a[i + 1]] + a[a[i + 2]]
  elif a[i] == 2:
    a[a[i + 3]] = a[a[i + 1]] * a[a[i + 2]]
  return (a,i + 4)

def solve(a):
  a[1],a[2],i = 12,2,0
  while a[i] != 99:
    a,i=(execute(a,i))

  return a[0]

print(solve(list(map(int,open("day2input.txt").read().split(",")))))
