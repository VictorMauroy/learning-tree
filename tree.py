class Tree :

    def __init__(self, value:any, childs = []) :
        self.value = value
        self.child_branchs:list[Tree] = childs
    
    def add_child(self, value:any) :
        """Add a child to the current tree"""
        new_child_branch = Tree(value, [])
        self.child_branchs.append(new_child_branch)

    def is_leaf(self) -> bool :
        """Whether the current tree has childs branchs or not"""
        return not self.child_branchs
    
    def tree_depth(self, depth_counter) -> int:
        """Return the first leaf founded"""
        if self.is_leaf() :
            return depth_counter
        else :
            depth_counter += 1
            return self.child_branchs[0].tree_depth(depth_counter)
    
    def get_depth(self) -> int :
        """Return the count of childs in the current tree"""
        
        if self.is_leaf() :
            return 1
        
        depth_list = [childBranch.get_depth() for childBranch in self.child_branchs]
        return max(depth_list) + 1
    
    def browse_depth(self, list_of_branchs:list = []) -> list :
        """Return the childs with their values by using the depth browse method"""
        #print(f"{self.value} is {'a leaf' if self.is_leaf() else 'not a leaf'}")
        
        if not self.is_leaf() :
            for branch in self.child_branchs :
                branch.browse_depth(list_of_branchs)
        
        list_of_branchs.append(self.value)

        return list_of_branchs

    def browse_width(self) -> list :
        """Return the childs with their values by using the width browse method"""
        list_of_branchs = []
        
        stack_branch = [self]
        while len(stack_branch) != 0 :
            current_branch = stack_branch.pop(0)
            list_of_branchs.append(current_branch.value)
            for branch in current_branch.child_branchs :
                stack_branch.append(branch)

        return list_of_branchs
        

root_tree = Tree(0, [])
root_tree.add_child(1)
root_tree.add_child(2)
count = 3

# Create 3 branchs in each branch of the root
for branch in root_tree.child_branchs :
    
    for i in range(3) :
        branch.add_child(count)
        count += 1

# Create 2 branch for each branch in each branch of the root
for branch in root_tree.child_branchs :
    
    for elt in branch.child_branchs :
        elt.add_child(count)
        count += 1
        elt.add_child(count)
        count += 1

print(f"Depth browse : {root_tree.browse_depth()}")
print(f"Width browse : {root_tree.browse_width()}")

print(f"Depth of tree is : {root_tree.get_depth()}")