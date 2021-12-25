from d19 import align_scanners
scanners = align_scanners()
align_scanners()
b = set()
for sc in scanners:
    for sig in sc.signals:
        b.add(sig.t)
print(len(b))
