def solve(ls):
  min_l,min_s=[],150
  for i,l in enumerate(ls):
    c = list(map(int, l))
    s = sum(1 for i in c if i == 0)
    if s < min_s:
      min_s = s
      min_l = c

  ones = sum(1 for i in min_l if i == 1)
  twos = sum(1 for i in min_l if i == 2)
  return ones * twos

def render(ls):
  img = []
  for i in range(150):
    for l in ls:
      if l[i] != '2':
        img.append(l[i])
        break
  m = [ img [i:i + 25] for i in range(0, len(img), 25) ]
  for i in m:
    for j in i:
      if j == '1':
        print('█', end='')
      else:
        print(' ', end='')
    print('\n')


inp = open("day8input.txt").read()
layers = list(map(''.join, zip(*[iter(inp)]*150)))
print(solve(layers))
render(layers)
