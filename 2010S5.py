__author__ = 'Daniel'


class Node:
    def __init__(self, *args):
        if len(args) == 2:
            self.left = args[0]
            self.right = args[1]
            self.nutrients = [1]
        else:
            self.left = None
            self.right = None
            self.nutrients = [args[0]]

    def calc_nutrients(self, growth_agents):
        if self.left is None:
            stem_ga = 0
            stem_capacity = 1
            input_nutrients = self.nutrients[0]
            for ga in range(growth_agents):
                if input_nutrients >= stem_capacity:
                    stem_ga += 1
                    stem_capacity = (1 + stem_ga)**2
                else:
                    input_nutrients += 1
                self.nutrients.append(min(input_nutrients, stem_capacity))
            self.nutrients[0] = 1

        else:
            self.left.calc_nutrients(growth_agents)
            self.right.calc_nutrients(growth_agents)
            max_combos = [2]
            for ga in range(1, growth_agents+1):
                max_n = 2
                for rc in range(ga+1):
                    max_n = max(self.left.nutrients[ga-rc] + self.right.nutrients[rc], max_n)
                max_combos.append(max_n)
            for ga in range(1, growth_agents+1):
                max_n = 1
                for sa in range(ga+1):
                    stem_capacity = (1+sa)**2
                    input_nutrients = max_combos[ga-sa]
                    max_n = max(min(stem_capacity, input_nutrients), max_n)
                    if stem_capacity > input_nutrients:
                        break
                self.nutrients.append(max_n)

    def calc_root(self, growth_agents):
        if self.left is None:
            return self.nutrients[0] + growth_agents
        else:
            self.left.calc_nutrients(growth_agents)
            self.right.calc_nutrients(growth_agents)
            max_n = 2
            for rc in range(growth_agents+1):
                max_n = max(self.left.nutrients[growth_agents-rc] + self.right.nutrients[rc], max_n)
            return max_n


def read_node(string, index=0):
    node = None
    next_char = string[index]
    index += 1
    if next_char == '(':
        left, index = read_node(string, index)
        index += 1
        right, index = read_node(string, index)
        node = Node(left, right)
        index += 1
    else:
        number = next_char
        while string[index].isdigit():
            number += string[index]
            index += 1
        node = Node(int(number))
    return node, index

file = open('2010/S5/s5.8.in')
root = read_node(file.readline())[0]
print(root.calc_root(int(file.readline())))