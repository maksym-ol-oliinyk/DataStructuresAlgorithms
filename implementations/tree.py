class TreeNode:
	def __init__(self, data):
		self.data = data
		self.children = []
		self.parent = None

	def addChild(self, child):
		child.parent = self
		self.children.append(child)

	def printNode(self, level = " "):
		print(f"|{level}{self.data}")
		level += "   "
		for child in self.children:
			child.printNode(level)

def buildProductTree():
	root = TreeNode("Electronics")

	laptop = TreeNode("Laptop")
	laptop.addChild(TreeNode("Mac"))
	laptop.addChild(TreeNode("Surface"))
	laptop.addChild(TreeNode("Thinkpad"))

	cellphone = TreeNode("Cell Phone")
	cellphone.addChild(TreeNode("iPhone"))
	cellphone.addChild(TreeNode("Google Pixel"))
	cellphone.addChild(TreeNode("Vivo"))

	tv = TreeNode("TV")
	tv.addChild(TreeNode("Samsung"))
	tv.addChild(TreeNode("LG"))

	root.addChild(laptop)
	root.addChild(cellphone)
	root.addChild(tv)

	return root


if __name__ == '__main__':
	root = buildProductTree() 
	root.printNode()


