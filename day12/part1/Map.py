
class Node:
    def __init__(self, name):
        self.name = name
        self.nodes = 0
        self.connections = []

    def get_name(self):
        return self.name

    def add_connection(self, node):
        found = False
        for n in self.connections:
            if n.get_name() == node.get_name():
                found = True
        if found == False:
            self.connections.append(node)
            return True
        return False

    def get_connections(self):
        return self.connections


class Map:
    def __init__(self, connections):
        self.map = []
        self.nodes = 0
        self.connections = 0
        self.start = None

        # Create nodes
        s = set()
        for c in connections:
            [start, end] = c.split('-')
            if start not in s:
                s.add(start)
                n = Node(start)
                self.map.append(n)
                self.nodes += 1
                if start == 'start':
                    self.start = n
            if end not in s:
                s.add(end)
                n = Node(end)
                self.map.append(n)
                self.nodes += 1
                if end == 'start':
                    self.start = n

        # Create connections
        for c in connections:
            [start, end] = c.split('-')
            start_node = None
            end_node = None
            for n in self.map:
                if n.get_name() == start:
                    start_node = n
                elif n.get_name() == end:
                    end_node = n
            start_node.add_connection(end_node)
            self.connections += 1
            end_node.add_connection(start_node)
            self.connections += 1

    def get_nodes(self):
        return self.nodes

    def get_connections(self):
        return self.connections

    def find_paths(self, node=None, path='start', visited=['start']):
        n = node if node != None else self.start
        paths = []
        for c in n.get_connections():
            if c.get_name().islower() and c.get_name() in visited:
                pass
            elif c.get_name() == 'end':
                paths.append(path + ',' + c.get_name())
            else:
                new_visited = visited + [c.get_name()]
                paths = paths + \
                    self.find_paths(c, path + ',' + c.get_name(), new_visited)
        return paths

    def __str__(self):
        s = ''
        for n in self.map:
            for c in n.get_connections():
                s += n.get_name() + '-' + c.get_name() + '\n'
        return s
