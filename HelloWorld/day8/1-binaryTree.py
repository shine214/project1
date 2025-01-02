class Node:
    def __init__(self, elem, left=None, right=None):
        self.elem = elem
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None
        self.queue = []
    def add(self,node:Node):
        self.queue.append(node)
        if self.root == None:
            self.root = node
        else:
            if self.queue[0].left == None:
                self.queue[0].left = node
            else:
                self.queue[0].right = node
                self.queue.pop(0)
    def pre_order(self,root:Node):
        if root == None:
            return
        print(root.elem,end = ' ')
        self.pre_order(root.left)
        self.pre_order(root.right)

    def mid_order(self,root:Node):
        if root == None:
            return
        self.mid_order(root.left)
        print(root.elem,end = ' ')
        self.mid_order(root.right)
    def post_order(self,root:Node):
        if root == None:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.elem, end=' ')
    def level_order(self,root:Node):
        if root == None:
            return
        q = []
        q.append(root)
        while q:
            n = q.pop(0)
            print(n.elem, end = ' ')
            if n.left != None:
                q.append(n.left)
            if n.right != None:
                q.append(n.right)
    def count_level(self,root:Node):
        max = 0
        if root == None:
            return max
        q = [root]
        cur = 1
        next = 0
        while q:
            for i in range(cur):
                n = q.pop(0)
                if n.left != None:
                    q.append(n.left)
                    next += 1
                if n.right != None:
                    q.append(n.right)
                    next += 1
            if next > max:
                max = next
            cur = next
            next = 0
        return max



elems = list(range(10))
tree = Tree()
for i in elems:
    new_node = Node(i)
    tree.add(new_node)
tree.pre_order(tree.root)
print()
tree.mid_order(tree.root)
print()
tree.post_order(tree.root)
print()
tree.level_order(tree.root)
print()
print(f'最大深度{tree.count_level(tree.root)}')