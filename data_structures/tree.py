class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        
    def get_level(self):
        level = 0
        p = self.parent
        #print('p = ', p)
        while p:
            level += 1
            p = p.parent
            #print('pp = ', p)

        #print('level = ', level)
        return level
        
    def print_tree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "!__" if self.parent else " "
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
        
def build_product_tree():
    root = TreeNode("Electronics")  # level 0
    
    laptop = TreeNode("Laptop") # level 1
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Hp"))
    laptop.add_child(TreeNode("Dell"))
    
    cellphone = TreeNode("Cell Phone")  # level 1
    cellphone.add_child(TreeNode("Samsung"))
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Android"))
    
    tv = TreeNode("TV") # level 1
    tv.add_child(TreeNode("Akira"))
    tv.add_child(TreeNode("HiSense"))
    
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root
    
root = build_product_tree()
root.print_tree()
