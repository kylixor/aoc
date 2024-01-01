from dataclasses import dataclass
from typing import Optional


file = open('day9/input.txt', 'r')
lines = file.read().splitlines()

@dataclass
class Sequence:
    nums: list[int]
    prev_seq: Optional['Sequence'] = None
    next_seq: Optional['Sequence'] = None

    def is_not_zeros(self):
        return True if any([x != 0 for x in self.nums]) else False
    
    def step_in(self):
        new_seq = [self.nums[x+1] - self.nums[x] for x in range(len(self.nums) - 1)]
        self.next_seq = Sequence(new_seq, self)
        if self.next_seq.is_not_zeros():
            self.next_seq.step_in()
        else:
            self.next_seq.step_out()

    def step_out(self):
        if self.next_seq:
            self.nums.insert(0, self.nums[0] - self.next_seq.nums[0])
        else:
            self.nums.insert(0, 0)
        if self.prev_seq:
            self.prev_seq.step_out()
        else:
            return self.nums[0]


extrapolated_values = 0
for line in lines:
    seq = Sequence([int(x) for x in line.split()])
    if seq.is_not_zeros():
        seq.step_in()
    extrapolated_values += seq.nums[0]
print(extrapolated_values)