class Tree :

    def __init__(self, name, value) :
        self.value = value
        self.childs_lane = []
        self.name = name
    
    def add_child(self, value) :
        """Add a child """
        child_name = self.name + "_" + (len(self.childs_lane) + 1)
        new_child_lane = Tree(value, child_name)
        self.childs_lane.append(new_child_lane)

    def is_leaf(self) -> bool :
        """Whether the current tree has childs lanes or not"""
        return True if len(self.childs_lane) == 0 else False
    
    def find_depth(self) -> int :
        """Return the number of childs"""
        return len(self.childs_lane)
    
    def browse_depth(self) -> list :
        """Return the childs with their values with the depth browse method"""

    def browse_width(self) :
        """Return the childs with their values with the width browse method"""

