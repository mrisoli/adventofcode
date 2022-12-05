from d5 import cmds_and_stacks, answer

cmds, stacks = cmds_and_stacks()
for amount, fr, to in cmds:
    stacks[to].extend(stacks[fr][-amount:])
    del stacks[fr][-amount:]

answer(stacks)
