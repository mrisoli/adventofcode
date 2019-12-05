from operator import eq

def find_solutions(l, u):
  return len(list(filter(lambda i: "".join(sorted(str(i))) == str(i) and any(map(eq, str(i), str(i)[1:])), range(l,u))))

def count_match(a):
  b=[""]+[a[x:x+2] for x in range(len(a)-1)]+[""]
  return any(b[x][0]==b[x][1] and b[x]!=b[x-1] and b[x]!=b[x+1] for x in range(1,len(b)-1))

def find_solutions_2(l, u):
  return len(list(filter(lambda i: "".join(sorted(str(i))) == str(i) and count_match(str(i)), range(l,u))))

print(find_solutions(347312, 805915))
print(find_solutions_2(347312, 805915))
