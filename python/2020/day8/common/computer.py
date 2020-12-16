class Computer:

    def __init__(self, ins):
        self.acc = 0
        self.curr = 0
        self.called = set()
        self.ins = [self.parse_ins(i) for i in ins]

    def parse_ins(self, i):
        [a, b] = i.split(' ')
        return (a, int(b))

    def run(self, ins=None):
        if ins is None:
            ins = self.ins
        while self.curr not in self.called:
            self.called.add(self.curr)
            self.exec_ins(ins)
            if self.curr == len(ins):
                return True
        return False

    def e_acc(self, ins):
        self.acc += ins[self.curr][1]
        self.curr += 1

    def e_jmp(self, ins):
        self.curr += ins[self.curr][1]

    def e_nop(self, ins):
        self.curr += 1

    def exec_ins(self, ins):
        ins_set = {
            'acc' : self.e_acc,
            'jmp': self.e_jmp,
            'nop' : self.e_nop,
        }
        f = ins_set.get(ins[self.curr][0])
        f(ins)

    def update_until_fixed(self):
        for i in range(len(self.ins)):
            self.reset()
            ins = list.copy(self.ins)
            inst = ins[i][0]
            if inst in ['jmp', 'nop']:
                ins[i] = ('nop' if inst == 'jmp' else 'jmp', ins[i][1])
            else:
                next
            ran = self.run(ins)
            if ran:
                return self.acc

    def reset(self):
        self.acc = 0
        self.curr = 0
        self.called = set()

