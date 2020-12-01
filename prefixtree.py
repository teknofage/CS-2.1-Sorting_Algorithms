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
        # creating node variable and setting it equal to the root node
        node = self.root
        # traverse the characters in the string
        for char in string:
          # if the node has a child node that is the same as the character
          if node.has_child(char): 
            # make a child variable and set it to equal the character of the child node
            child = node.get_child(char)
            # increment the node down the tree by making it point to the child
            node = child
          else:
            # if it the node has no more children, return it as the terminal node
            return node.is_terminal()
          return node.is_terminal()

    def insert(self, string):
        """Insert the given string into this prefix tree."""
        current = self.root
        #"h e l l o"
        for i in range(len(string)):
          print(string[i])
          #if current does not have children:
          if not current.has_child(string[i]):
            #create a new node
            #insert new node with current #char in string
            new_node = PrefixTreeNode(string[i])
            #add it as a child of current node
            #if there is a child the child is the letter of the string
            current.add_child(string[i], new_node)
            print("Current", current)
          #current = that child
          current = current.get_child(string[i])
          print("Change to next")
        print("End", current)
        #when I'm at the end of the string I want to make the last character terminal
        current.terminal = True

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
        # create index_pointer starting variable
        index_pointer = 0
        # traverse the letters of the string (for as long as the nodes have children) 
        while index_pointer < len(string) and node.has_child(string[index_pointer]) is True:
          # increment the node pointer by setting it to the child of the index_pointer
          node = node.get_child(string[index_pointer])
          # increment the index_pointer
          index_pointer += 1
        # return the node and its location
        return node, index_pointer

    def complete(self, prefix):
        """Return a list of all strings stored in this prefix tree that start
        with the given prefix string."""
        # Create a list of completions in prefix tree
        completions = []
        # if the prefix is an empty string
        if prefix == ""
          # return the strings function on the tree
          return self.strings()
        # create node variable and set it equal to that location 
        node = self._find_node(prefix)
        # if the character at location 0 is not empty
        if node[0].character != "":
          # traverse the tree from node 0 to the prefix, and append it to completions
          self.traverse(node[0], prefix, completions.append()
        # return the list of completions
        return completions

    def strings(self):
        """Return a list of all strings stored in this prefix tree."""
        # Create a list of all strings in prefix tree
        all_strings = []
        # traverse the branches of the tree and store any strings in all_strings
        self._traverse(self.root, len(self)-1, all_strings.append())
        return all_strings

    def _traverse(self, node, prefix, visit):
        """Traverse this prefix tree with recursive depth-first traversal.
        Start at the given node with the given prefix representing its path in
        this prefix tree and visit each node with the given visit function."""
        # TODO


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