import graphviz

def get_leaf_values(node):
    ''' 
    Given a node of a suffix trie, recursively perform depth-first search and return a list
    of all values found at leaves in this subtrie.
    '''
    values = []
    if '$' in node:
        values.append(node['$'])
    nonleaf_children = [c for c in node.keys() if c != '$']
    for char in nonleaf_children:
        values += get_leaf_values(node[char])
    return values

# Based on Ben Langmead's .to_dot() method

def _to_dot_helper(node, parid, lines):
    childid = parid
    for c, child in node.items():
        lines.append('  %d -> %d [ label=" %s" ];' % (parid, childid+1, c))
        if c=='$':
            # This child is a leaf, and we don't want to recurse over it
            # Instead draw the value in the node
            lines.append('  %d [ label="%s" ];' % (childid+1, child))
            childid += 1
        else:
            # This child is another internal node, recurse
            childid = _to_dot_helper(child, childid+1, lines)
    return childid
    
def trie_to_dot(trie):
    ''' Return a dot represntation of a suffix trie '''
    lines = []
    lines.append('digraph "Suffix trie" {')
    lines.append('  node [shape=circle label=""];')
    _to_dot_helper(trie, 0, lines)
    lines.append('}')
    return '\n'.join(lines) + '\n'

def draw_trie(trie):
    ''' Return a graphviz object representing the suffix trie '''
    return graphviz.Source(trie_to_dot(trie), engine='dot', format='png')