#!python3

from prefixtreenode import PrefixTreeNode

class PrefixTree:
    """PrefixTree: A multi-way prefix tree that stores strings with efficient
    methods to insert a string into the tree, check if it contains a matching
    string, and retrieve all strings that start with a given prefix string.
    Time complexity of these methods depends only on the number of strings
    retrieved and their maximum length (size and height of subtree searched),
    but is independent of the number of strings stored in the prefix tree, as
    its height depends only on the length of the longest string stored in it.
    This makes a prefix tree effective for spell-checking and autocompletion.
    Each string is stored as a sequence of characters along a path from the
    tree's root node to a terminal node that marks the end of the string."""

    # Constant for the start character stored in the prefix tree's root node
    START_CHARACTER = ''

    def __init__(self, strings=None):
        """Initialize this prefix tree and insert the given strings, if any."""
        # Create a new root node with the start character
        self.root = PrefixTreeNode(PrefixTree.START_CHARACTER)
        # Count the number of strings inserted into the tree
        self.size = 0
        # Insert each string, if any were given
        if strings is not None:
            for string in strings:
                self.insert(string)

    def __repr__(self):
        """Return a string representation of this prefix tree."""
        return f'PrefixTree({self.strings()!r})'

    def is_empty(self):
        """Return True if this prefix tree is empty (contains no strings)."""
        return self.size == 0

    def contains(self, string):
        """Return True if this prefix tree contains the given string."""
        node = self.root
        # traverse through the string of each character
        for char in string: 
            # if node has the character in its children
            if node.has_child(char): 
                # this will be our "next"
                child = node.get_child(char) 
                # Reassign "head"
                node = child 
            # if the character is not in the string
            else: 
                # final node is terminal
                return node.is_terminal()
        # final node is terminal
        return node.is_terminal() 

    def insert(self, string):
        """Insert the given string into this prefix tree."""
        node = self.root
        # traverse the characters in the string
        for char in string:
             # Search for child, and character is found
            if node.has_child(char):
                # Node is there, move to the next node
                node = node.get_child(char) 
            else:
                # Create a new node
                new_node = PrefixTreeNode(char)
                # Append new node
                node.add_child(char, new_node) 
                # point "head" to new new node and continue
                node = new_node 
        # if node is not terminal, increase word count, then set terminal to equal True
        if not node.is_terminal():
            self.size += 1
            node.terminal = True

    def _find_node(self, string):
        """Return a pair containing the deepest node in this prefix tree that
        matches the longest prefix of the given string and the node's depth.
        The depth returned is equal to the number of prefix characters matched.
        Search is done iteratively with a loop starting from the root node."""
        # Match the empty string
        if len(string) == 0:
            return self.root, 0
        # Start with the root node
        node = self.root
        idx_pointer = 0 # Create starting pointer
        # Loop through each letter of string
        # while the runner is less than the length of the string and the if the node has the character
        while idx_pointer < len(string) and node.has_child(string[idx_pointer]) is True:
            # Traverse through each node, then point to the next value
            node = node.get_child(string[idx_pointer])
            idx_pointer += 1
        # return both node and location of the node
        return node,idx_pointer

    def complete(self, prefix):
        """Return a list of all strings stored in this prefix tree that start
        with the given prefix string."""
        # Create a list of completions in prefix tree
        # Create an empty array to hold all strings
        completions = []
        # If prefix is equal to nothing
        if prefix == '':
            # Return null
            return self.strings()
        # use the _find function to find the prefix within the string
        node = self._find_node(prefix)
        # if the value at the start is not equal to nothing
        if node[0].character != '':
            # start the recursive traverse function, start from the first value in the node, with the prefix used; and then on each visit, append to the completions array
            self._traverse(node[0], prefix, completions.append)
        # return the filled list of strings
        return completions

    def strings(self):
        """Return a list of all strings stored in this prefix tree."""
        # Create a list of all strings in prefix tree
        # Create an empty array
        all_strings = []
        # use the recursive traverse function, start from the self.root, start from an empty prefix, and on each node visited, append to the empty array
        self._traverse(self.root, '',all_strings.append)
        return all_strings

    def _traverse(self, node, prefix, visit):
        """Traverse this prefix tree with recursive depth-first traversal.
        Start at the given node with the given prefix representing its path in
        this prefix tree and visit each node with the given visit function."""
        # BASE CASE
        # If this node is the terminal/end node, return the entire prefix string
        if node.is_terminal():
            visit(prefix)
        # Traverse through the keys of the node's children
        for char in node.children.keys():
            # Assign the char to child
            child = node.get_child(char)
            # Recursively call the traversal function, but continue to add the new character to the prefix and start from the child node until we reach the end
            self._traverse(child, prefix + char, visit)


def create_prefix_tree(strings):
    print(f'strings: {strings}')

    tree = PrefixTree()
    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')
    print(f'strings: {tree.strings()}')

    print('\nInserting strings:')
    for string in strings:
        tree.insert(string)
        print(f'insert({string!r}), size: {tree.size}')

    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')

    print('\nSearching for strings in tree:')
    for string in sorted(set(strings)):
        result = tree.contains(string)
        print(f'contains({string!r}): {result}')

    print('\nSearching for strings not in tree:')
    prefixes = sorted(set(string[:len(string)//2] for string in strings))
    for prefix in prefixes:
        if len(prefix) == 0 or prefix in strings:
            continue
        result = tree.contains(prefix)
        print(f'contains({prefix!r}): {result}')

    print('\nCompleting prefixes in tree:')
    for prefix in prefixes:
        completions = tree.complete(prefix)
        print(f'complete({prefix!r}): {completions}')

    print('\nRetrieving all strings:')
    retrieved_strings = tree.strings()
    print(f'strings: {retrieved_strings}')
    matches = set(retrieved_strings) == set(strings)
    print(f'matches? {matches}')


def main():
    # Simpe test case of string with partial substring overlaps
    strings = ['ABC', 'ABD', 'A', 'XYZ']
    create_prefix_tree(strings)

    # Create a dictionary of tongue-twisters with similar words to test with
    tongue_twisters = {
        'Seashells': 'Shelly sells seashells by the sea shore'.split(),
        # 'Peppers': 'Peter Piper picked a peck of pickled peppers'.split(),
        # 'Woodchuck': ('How much wood would a wood chuck chuck'
        #                ' if a wood chuck could chuck wood').split()
    }
    # Create a prefix tree with the similar words in each tongue-twister
    for name, strings in tongue_twisters.items():
        print(f'{name} tongue-twister:')
        create_prefix_tree(strings)
        if len(tongue_twisters) > 1:
            print('\n' + '='*80 + '\n')


if __name__ == '__main__':
    main()