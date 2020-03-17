class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def makeRelationships(family):
    tree = {}

    for people in family:
        if people[1] in tree:
            tree[people[1]].append(people[0])
        else:
            tree[people[1]] = [people[0]]

    return tree


def earliest_ancestor(ancestors, starting_node):
    relationships = makeRelationships(ancestors)
    stack = Stack()
    oldest = {"length": 1, "node": starting_node}
    stack.push(oldest)

    if starting_node not in relationships:
        return -1

    while stack.size() > 0:
        node = stack.pop()
        if node["length"] >= oldest["length"]:
            if node["length"] == oldest["length"]:
                if node["node"] < oldest["node"]:
                    oldest = node
            else:
                oldest = node

        if node["node"] not in relationships:
            continue
        for parent in relationships[node["node"]]:
            new_node = {"length": node["length"] + 1, "node": parent}
            stack.push(new_node)

    return oldest["node"]

