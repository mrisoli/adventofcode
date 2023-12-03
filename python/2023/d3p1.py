from d3 import generate

print(sum(n for _,n in generate(r'[^0-9.]')))
