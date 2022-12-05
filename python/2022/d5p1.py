from d5 import cmds_and_stacks, answer

cmds, stacks = cmds_and_stacks()
for amount, fr, to in cmds:
    for i in range(amount):
        stacks[to].append(stacks[fr].pop())

answer(stacks)
