import random


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"🌲({self.val}, {self.left}, {self.right})"


def randomTree():
    if random.randint(0, 2):
        # 2/3 chance of None. 1/3 chance of a node.
        # For a tree, this is especially important, to avoid exceeding the recursion limit.
        return None
    return TreeNode(random.randint(0, 10), randomTree(), randomTree())


class Codec:
    def serialize(self, root):
        return (
            "#"
            if not root
            else (
                str(root.val)
                + " "
                + self.serialize(root.left)
                + " "
                + self.serialize(root.right)
            )
        )

    def deserialize(self, data):
        def dsl_iter():
            v = next(vals)
            if v == "#":
                return None
            root = TreeNode(int(v))
            root.left = dsl_iter()
            root.right = dsl_iter()
            return root

        vals = iter(data.split())
        return dsl_iter()


if __name__ == "__main__":
    codec = Codec()
    root = randomTree()
    print(root)
    print("Serializing...")
    print(codec.serialize(root))
    print("... and deserializing.")
    print(codec.deserialize(codec.serialize(root)))
