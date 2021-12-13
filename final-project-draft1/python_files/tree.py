class BST:
    """
    Implement the Binary Search Tree (BST) data structure.  The Node 
    class below is an inner class.  An inner class means that its real 
    name is related to the outer class.  To create a Node object, we will 
    need to specify BST.Node
    """

    class Node:
        """
        Each node of the BST will have data and links to the 
        left and right sub-tree. 
        """

        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None

    def insert(self, data):
        """
        Insert 'data' into the BST.  If the BST
        is empty, then set the root equal to the new 
        node.  Otherwise, use _insert to recursively
        find the location to insert.
        """
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    def _insert(self, data, node):
        """
        This function will look for a place to insert a node
        with 'data' inside of it.  The current sub-tree is
        represented by 'node'.  This function is intended to be
        called the first time by the insert function.
        """
        # Check if the data is less than the node.data 
        # and if it is not a duplicate
        if data < node.data and data != node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        # Do the same check but for values larger than data.node
        elif data > node.data and data != node.data:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)

    ###################
    # Start Problem 1 #
    ###################
    def __contains__(self, data):
        """ 
        This function will be called by the user which initiates
        a search to find a value in the BST. The value that will
        be passed is the value that the user is trying to find.
        If the BST is empty, return False. Otherwise, call the 
        _contains function and start at the root. This function
        supports the ability to use the 'in' keyword:

        if 5 in my_bst:
            ("5 is in the bst")
        """
        return self._contains(data, self.root)  # Start at the root

    def _contains(self, data, node):
        """
        This recursive function will be called until the value is
        found. If the function does not find the function, it will
        return False. The node parameter represents the subtree 
        that will be searched. If the value is found in the BST,
        recursion should stop (Hint: Base Case). For every recursive
        call, the subtree should get smaller (Hint: Smaller Problem).
        """
        # Base Case
        if data == node.data:
            return True

        else:
            # If data is less than the node data, search through the
            # left subtree 
            if data < node.data:
                if node.left is None:
                    # Since it has made it to the end of the tree, the value is not present
                    return False
                else:
                    return self._contains(data, node.left)
            
            # If data is greater than the node data, search through the
            # right subtree
            elif data > node.data:
                if node.right is None:
                    # Since it has made it to the end of the tree, the value is not present
                    return False
                else:
                    return self._contains(data, node.right)
    
    #################
    # End Problem 1 #
    #################