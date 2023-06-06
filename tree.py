class Tree :

    def __init__(self, value, parent_branch, childs = []) :
        self.value = value
        self.child_branchs = childs
        self.parent_branch = parent_branch
    
    def add_child(self, value) :
        """Add a child to the current tree"""
        new_child_branch = Tree(value, [])
        self.child_branchs.append(new_child_branch)

    def is_leaf(self) -> bool :
        """Whether the current tree has childs branchs or not"""
        return True if len(self.child_branchs) == 0 else False
    
    def find_leaf(self) :
        """Return the first lead founded"""
        if self.is_leaf() :
            return self.child_branchs[0]
        else :
            return self.child_branchs[0].find_depth()
    
    def find_depth(self) -> int :
        """Return the count of childs in the current tree"""
        return len(self.child_branchs)
    
    def browse_depth(self) -> list :
        """Return the childs with their values with the depth browse method"""
    

    def browse_width(self) -> list :
        """Return the childs with their values with the width browse method"""


root_tree = Tree(0, [])
root_tree.add_child(1, root_tree)
root_tree.add_child(2, root_tree)
count = 3
for branch in root_tree.child_branchs :
    for i in range(3) :
        branch.add_child(count, branch)
        count += 1

    for branch2 in root_tree.child_branchs :
        for elt in range(branch2.child_branchs) :
            elt.add_child(count, elt)
            count += 1
            elt.add_child(count, elt)
            count += 1


