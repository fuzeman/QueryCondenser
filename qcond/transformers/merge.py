from operator import itemgetter
from logr import Logr
from qcond.helpers import simplify, strip
from qcond.transformers.base import Transformer


class MergeTransformer(Transformer):
    def __init__(self):
        super(MergeTransformer, self).__init__()

    def run(self, titles):
        titles = set([simplify(title) for title in titles])

        Logr.debug("------------------------------------------------------------")

        root = []
        tails = []

        for title in titles:
            Logr.debug(title)

            cur = None
            words = title.split(' ')

            for wx in xrange(len(words)):
                word = strip(words[wx])

                if cur is None:
                    cur = find_node(root, word)

                    if cur is None:
                        cur = DNode(word, None)
                        root.append(cur)
                else:
                    parent = cur
                    parent.weight += 1

                    cur = find_node(parent.right, word)

                    if cur is None:
                        cur = DNode(word, parent)
                        parent.right.append(cur)
                    else:
                        cur.weight += 1

            tails.append(cur)

        Logr.debug("--------------------------PARSE-----------------------------")

        for node in root:
            print_tree(node)

        Logr.debug("--------------------------MERGE-----------------------------")

        self.merge(root)

        Logr.debug("--------------------------FINAL-----------------------------")

        for node in root:
            print_tree(node)

        Logr.debug("--------------------------RESULT-----------------------------")

        results = {}

        for tail in tails:
            score, value = tail.full_value()

            if score and value:
                if value not in results:
                    results[value] = score
                else:
                    results[value] += score

        sorted_results = sorted(results.items(), key=itemgetter(1), reverse = True)

        return [result[0] for result in sorted_results]

    def merge(self, root):
        for x in range(len(root)):
            root[x].right = self._merge(root[x].right)

        return root

    def get_nodes_right(self, value):
        if type(value) is not list:
            value = [value]

        nodes = []

        for node in value:
            nodes.append(node)

            for child in self.get_nodes_right(node.right):
                nodes.append(child)

        return nodes

    def destroy_nodes_right(self, value):
        nodes = self.get_nodes_right(value)

        for node in nodes:
            node.value = None
            node.dead = True

    def _merge(self, nodes, depth = 0):
        Logr.debug(str('\t' * depth) + str(nodes))

        top = nodes[0]

        # Merge into top
        for x in range(len(nodes)):
            # Merge extra results into top
            if x > 0:
                top.value = None
                top.weight += nodes[x].weight
                self.destroy_nodes_right(top.right)

                if len(nodes[x].right):
                    top.join_right(nodes[x].right)

                    Logr.debug("%s joined %s", nodes[x], top)

                nodes[x].dead = True

        nodes = [n for n in nodes if not n.dead]

        # Traverse further
        for node in nodes:
            if len(node.right):
                node.right = self._merge(node.right, depth + 1)

        return nodes


def print_tree(node, depth = 0):
    Logr.debug(str('\t' * depth) + str(node))

    if len(node.right):
        for child in node.right:
            print_tree(child, depth + 1)
    else:
        Logr.debug(node.full_value()[1])


def find_node(node_list, value):
    # Try find adjacent node match
    for node in node_list:
        if node.value == value:
            return node

    return None


class DNode(object):
    def __init__(self, value, parent, right = None, weight = 1):
        self.value = value

        self.parent = parent

        if right is None:
            right = []
        self.right = right

        self.weight = weight

        self.dead = False

    def join_right(self, nodes):
        for node in nodes:
            duplicate = filter(lambda x: x.value == node.value, self.right)

            if duplicate:
                duplicate[0].weight += node.weight
                duplicate[0].join_right(node.right)
            else:
                node.parent = self
                self.right.append(node)

    def full_value(self):
        words = []
        total_score = 0
        cur = self

        while cur is not None:
            if cur.value and not cur.dead:
                words.insert(0, cur.value)
                total_score += cur.weight

            cur = cur.parent

        return total_score / len(words), ' '.join(words)

    def __repr__(self):
        return '<%s value:"%s", weight: %s%s>' % (
            'DNode',
            self.value,
            self.weight,
            ' REMOVING' if self.dead else ''
        )
