import os
from math import gcd, prod, trunc
from typing import List

class Monkey:
    def __init__(self, id, items, operation, test, true_goal, false_goal):
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test
        self.true_goal = true_goal
        self.false_goal = false_goal
        self.inspections = 0
    
    def get_test_val(self):
        return self.test
    
    def get_inspection_count(self):
        return self.inspections
    
    def get_items(self):
        return self.items
    
    def get_id(self):
        return self.id
    
    def throw_item(self):
        thrown_item = self.items[0]
        self.items = self.items[1:]
        return thrown_item
    
    def receive_item(self, item):
        self.items.append(item)
        
    def get_target(self):
        return self.true_goal if self.items[0] % self.test == 0 else self.false_goal
    
    def inspect_item(self, lower_worry=0):
        operation_split = self.operation.split(" ")
        action = operation_split[3]
        value = int(operation_split[4]) if (operation_split[4] != "old") else self.items[0]
        if (action == "+"):
            self.items[0] = self.items[0] + value
        if (action == "*"):
            self.items[0] = self.items[0] * value
        self.inspections += 1
        if (lower_worry == 0):
            self.items[0] = trunc(self.items[0] / 3)
        else:
            self.items[0] %= lower_worry

def read_input(filename):
    fileDir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(fileDir, filename)
    with open(filename) as f:
        input = f.read().splitlines()
        number_of_monkeys = len([line for line in input if line.startswith("Monkey")])
        monkeys = []
        for i in range(0, number_of_monkeys):
            monkey_id = int(input[i * 7].split(" ")[1].replace(":", ""))
            items = [int(e) for e in input[i * 7 + 1].replace("  Starting items: ", "").split(", ")]
            operation = input[i * 7 + 2].replace("  Operation: ", "")
            test = int(input[i * 7 + 3].replace("  Test: divisible by ", ""))
            true_goal = int(input[i * 7 + 4].replace("    If true: throw to monkey ", ""))
            false_goal = int(input[i * 7 + 5].replace("    If false: throw to monkey ", ""))
            monkeys.append(Monkey(monkey_id, items, operation, test, true_goal, false_goal))
    return monkeys

def part_one():
    monkeys: List[Monkey] = read_input('./input.txt')
    for _ in range(0, 20):
        for monkey in monkeys:
            while len(monkey.get_items()):
                monkey.inspect_item()
                target_id = monkey.get_target()
                item = monkey.throw_item()
                target_monkey = [monkey for monkey in monkeys if monkey.get_id() == target_id][0]
                target_monkey.receive_item(item)
    return prod(sorted([monkey.get_inspection_count() for monkey in monkeys], reverse=True)[0:2])

        
   
def part_two():
    monkeys: List[Monkey] = read_input('./input.txt')
    test_lcm = prod([m.get_test_val() for m in monkeys])
    for _ in range(0, 10000):
        for monkey in monkeys:
            while len(monkey.get_items()):
                monkey.inspect_item(lower_worry=test_lcm)
                target_id = monkey.get_target()
                item = monkey.throw_item()
                target_monkey = [monkey for monkey in monkeys if monkey.get_id() == target_id][0]
                target_monkey.receive_item(item)
    return prod(sorted([monkey.get_inspection_count() for monkey in monkeys], reverse=True)[0:2])

def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()
