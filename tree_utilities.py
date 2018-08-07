purines = ['A', 'G']
pyrimidines = ['C', 'T']
nucleotides = purines + pyrimidines

def tree_to_newick(tree):
    """
    Produce a string representation of the tree in Newick format.
    """
    return "({});".format(newick_traverse(tree, 'root'))

def newick_traverse(tree, node_name):
    """
    Traverse the tree recursively starting from the specified node,
    producing a string representation of the tree in Newick format.
    The nucleotide costs are stored inside the Newick "node name",
    separated by a | character.
    """
    if node_name is None:
        return ""
    costs_string = "|".join(["{}={}".format(nt,tree[node_name][nt]) for nt in nucleotides])
    node_string = "{}|{}".format(node_name,costs_string)
    left_child = tree[node_name]['left']
    right_child = tree[node_name]['right']
    if left_child is None and right_child is None:
        return node_string
    else:
        left_string = newick_traverse(tree, left_child)
        right_string = newick_traverse(tree, right_child)
        return "({},{}){}".format(left_string, right_string, node_string)