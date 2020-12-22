from queue import Queue


class Node(object):
    def __init__(self, value):
        self.value = value
        self.lchild = None
        self.rchild = None

class BinarySearchTree(object):
    def __init__(self, root=None):
        self.root = root

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, root, value):
        if not root:
            return Node(value)
        
        if value < root.value:
            root.lchild = self._insert(root.lchild, value)
        elif value > root.value:
            root.rchild = self._insert(root.rchild, value)
        else:
            print(f"The insert value exsists!")
        
        return root
    
    def traversal(self):
        self._preorder_traversal(self.root)
        print("preorder traversal")
        self._inorder_traversal(self.root)
        print("inorder traversal")
        self._postorder_traversal(self.root)
        print("postorder traversal")

    def _preorder_traversal(self, root):
        if not root:
            return

        print(root.value, end=' ')
        self._preorder_traversal(root.lchild)
        self._preorder_traversal(root.rchild)

    def _inorder_traversal(self, root):
        if not root:
            return

        self._inorder_traversal(root.lchild)
        print(root.value, end=' ')
        self._inorder_traversal(root.rchild)

    def _postorder_traversal(self, root):
        if not root:
            return

        self._postorder_traversal(root.lchild)
        self._postorder_traversal(root.rchild)
        print(root.value, end=' ')
        
    def bfs(self):
        queue = Queue()
        
        if not self.root:
            print("The root is None!")
        else:
            print("bfs: ", end='')
            queue.put(self.root)

            while not queue.empty():
                node = queue.get()
                print(node.value, end=' ')
                if node.lchild:
                    queue.put(node.lchild)
                if node.rchild:
                    queue.put(node.rchild)

    def find(self, value):
        return self._find(self.root, value)

    def _find(self, root, value):
        while root and root.value != value:
            if value < root.value:
                root = root.lchild
            else:
                root = root.rchild
        
        return root

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, root, value):
        if not root:
            return None
        
        # 理解_delete()函数的功能:
        # 删除以root为根结点的子树中值为value的结点并返回一棵重构后的搜索树
        if value < root.value:
            root.lchild = self._delete(root.lchild, value)
        elif value > root.value:
            root.rchild = self._delete(root.rchild, value)
        else:
            if root.lchild and root.rchild:
                # 找到待删除结点左子树中的最大值结点，并删除
                lchild_maxmum_node = root.lchild
                while lchild_maxmum_node.rchild:
                    lchild_maxmum_node = lchild_maxmum_node.rchild
                root.lchild = self._delete(root.lchild, lchild_maxmum_node.value)
                root.value = lchild_maxmum_node.value

                # 注意:用左子树中的最大值还是右子树中的最小值，重构的BST不一样 

                # # 找到待删除结点右子树中的最小值结点，并删除
                # rchild_minmum_node = root.rchild
                # while rchild_minmum_node.lchild:
                #     rchild_minmum_node = rchild_minmum_node.lchild
                # root.rchild = self._delete(root.rchild, rchild_minmum_node.value)
                # root.value = rchild_minmum_node.value
            else:
                # 把待删除结点度为0/1的情况一并考虑了
                root = root.lchild if root.lchild else root.rchild

        return root



if __name__ == "__main__":

    arr = [5, 3, 4, 0, 2, 1, 8, 6, 9, 7]
    bst = BinarySearchTree()

    # check insert()
    for i in arr:
        bst.insert(i)

    # check traversal()
    bst.traversal()

    # check bfs()
    bst.bfs()

    # check find()
    print(f"\nfind value: {bst.find(0)}")

    # check delete()
    bst.delete(3)
    bst.bfs()

    

