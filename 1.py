import time
from itertools import product
from random import randint, shuffle

class NodeSphere:
    
    def __init__(self, a:int, b:int):
        self.a = a
        self.b = b
    
    def __lt__(self, other):
        return self.a < other.a or self.a <= other.a and self.b < other.b
    
    def __le__(self, other):
        return self.a <= other.a or self.a <= other.a and self.b <= other.b


    def __gt__(self, other):
        return other.__lt__(self)
    
    def __ge__(self, other):
        return other.__le__(self)
    
    def __eq__(self, other):
        return self.a == other.a and self.b == other.b
    
    def __str__(self):
        return f"({self.a}, {self.b})"
    
    __repr__ = __str__


class TriangleCircles:
	
    def __init__(self, data:list):
        self.data = data
    
    def shift(self):
        data = [0 for _ in range(len(self.data))]
        data[0] = self.data[-1]
        for i in range(1, len(self.data)):
            data[i] = self.data[i - 1]
        return TriangleCircles(data)

    def get_edgesTable(self):
        l = len(self.data)
        table = [[0 for _ in range(l)] if __ != 0 else self.data for __ in range(l + 1)]
        for i in range(1, l + 1):
            table[i][i - 1] = 1
            if i + 1 < l + 1:
                table[i][i] = 1
        table[l][0] = 1
        return table

    def __eq__(self, other):
        def check(first, second):
            return first.data == second.data
        if check(self, other):
            return True
        self_shifted = self.shift()
        while (not check(self, self_shifted)):
            if check(self_shifted, other):
                return True
            self_shifted = self_shifted.shift()
        return False
    
    def __str__(self):
        return str(self.data)
    
    __repr__ = __str__


def print_table(table):
    for line in table:
        print(line)


def join_tables(table1, table2):
    table = [table1[0] + table2[0]]
    for i in range(1, len(table1)):
        for j in range(1, len(table2)):
            table.append(table1[i] + table2[j])
    return table


def join_sixTables(table1, table2, table3, table4, table5, table6):
    table12 = join_tables(table1, table2)
    table123 = join_tables(table12, table3)
    table1234 = join_tables(table123, table4)
    table12345 = join_tables(table1234, table5)
    table = join_tables(table12345, table6)
    return table


def zip_table(table):
    new_table = []
    header = sorted(list(set([obj.a for obj in table[0]])), reverse=True)
    mapping = {}
    for i in range(len(header)):
        mapping[header[i]] = i

    for i in range(1, len(table)):
        line = table[i]
        new_line = [0 for _ in range(len(header))]
        for num in header:
            found = False
            for j in range(len(line)):
                bit = line[j]
                if table[0][j].a == num and bit == 1:
                    found = True
                    break
            if found:
                new_line[mapping[num]] = 1
        new_table.append(tuple(new_line))

    return set(new_table)


def get_standard():
    data = []
    with open("data.txt", 'r') as f:
        for line in f:
            new_line = tuple(map(int, tuple(line.strip())))
            data.append(new_line)
    return set(data)


def algo():
    ops = (1, 2, 3, 4, 5, 6)
    for op in product(ops, repeat=75):
        print(op)


def get_elements():
    data = []
    for i in range(1, 16):
        for j in range(1, 6):
            data.append(NodeSphere(i, j))
    return data


def full_random_main():
    data = get_elements()
    standard = get_standard()
    i = 0

    while i == 0 or not standard == ziped_table:
        start_time = time.time()
        v1 = randint(3, 60)
        v2 = randint(3, max(60 - v1, 3))
        v3 = randint(3, max(60 - v1 - v2, 3))
        v4 = randint(3, max(60 - v1 - v2 - v3, 3))
        v5 = randint(3, max(60 - v1 - v2 - v3 - v4, 3))

        heaps = [[] for _ in range(6)]
        s = data.copy()
        shuffle(s)
        for i in range(75):
            if i < v1:
                heaps[0].append(s[i])
            elif v1 <= i < v1 + v2:
                heaps[1].append(s[i])
            elif v1 + v2 <= i < v1 + v2 + v3:
                heaps[2].append(s[i])
            elif v1 + v2 + v3 <= i < v1 + v2 + v3 + v4:
                heaps[3].append(s[i])
            elif v1 + v2 + v3 + v4 <= i < v1 + v2 + v3 + v4 + v5:
                heaps[4].append(s[i])
            else:
                heaps[5].append(s[i])

        triangles = [TriangleCircles(obj) for obj in heaps]
        tables = [obj.get_edgesTable() for obj in triangles]
        table = join_sixTables(*tables)
        ziped_table = zip_table(table)
        success = standard == ziped_table
        end_time = time.time()
        i += 1

        print(success)
        print(f"This one {end_time - start_time} seconds")

        if success:
            print(table)
        if i % 10 == 0:
            print(f"{i} iters left")

def partial_random_main():
    data = get_elements()
    standard = get_standard()
    i = 0

    while i == 0 or not standard == ziped_table:
        start_time = time.time()
        v1 = randint(3, 22)
        v2 = 25 - v1
        v3 = randint(3, 22)
        v4 = 25 - v3
        v5 = randint(3, 22)

        heaps = [[] for _ in range(6)]
        s = data.copy()
        shuffle(s)
        for i in range(75):
            if i < v1:
                heaps[0].append(s[i])
            elif v1 <= i < v1 + v2:
                heaps[1].append(s[i])
            elif v1 + v2 <= i < v1 + v2 + v3:
                heaps[2].append(s[i])
            elif v1 + v2 + v3 <= i < v1 + v2 + v3 + v4:
                heaps[3].append(s[i])
            elif v1 + v2 + v3 + v4 <= i < v1 + v2 + v3 + v4 + v5:
                heaps[4].append(s[i])
            else:
                heaps[5].append(s[i])

        triangles = [TriangleCircles(obj) for obj in heaps]
        tables = [obj.get_edgesTable() for obj in triangles]
        table = join_sixTables(*tables)
        ziped_table = zip_table(table)
        start_success = time.time()
        success = standard == ziped_table
        end_success = time.time()
        end_time = time.time()
        i += 1

        print(success)
        print(f"This one {end_time - start_time} seconds, success time {end_success - start_success}")

        if success:
            print(table)
        if i % 10 == 0:
            print(f"{i} iters left")

if __name__ == '__main__':
    full_random_main()
