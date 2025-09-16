class PrintMode:
	NAME = "name"
	DESIGNATION = "designation"
	BOTH = "both"

class TreeNode:
	def __init__(self, name, designation = ""):
		self.name = name
		self.designation = designation
		self.children = []
		self.parent = None

	def addChild(self, child):
		child.parent = self
		self.children.append(child)

	def getDataToPrint(self, printMode):
		if printMode == "both":
			return f"{self.name}  ({self.designation})"
		if printMode == "designation":
			return self.designation
		else:
			return self.name

	def printNodeExc1(self, printMode = "name", level = 0):
		print(f"{"   " * level}{"|__" if level > 0 else ""}{self.getDataToPrint(printMode)}")
		level += 1
		for child in self.children:
			child.printNodeExc1(printMode, level)

	def printNodeExc2(self, showLevels = 0, printMode = "name", level = 0):
		if showLevels == 0 or showLevels >= level:
			print(f"{"   " * level}{"|__" if level > 0 else ""}{self.getDataToPrint(printMode)}")
		level += 1
		for child in self.children:
			child.printNodeExc2(showLevels, printMode, level)

def buildTreeExc1():
	root = TreeNode("Nilupul", "CEO")

	chinmay = TreeNode("Chinmay", "CTO")
	yishwa = TreeNode("Yishwa", "Infrastructure Head")
	aamir = TreeNode("Aamir", "Application Head")
	yishwa.addChild(TreeNode("Dhaval", "Cloud Manager"))
	yishwa.addChild(TreeNode("Adhijit", "App Manager"))
	chinmay.addChild(yishwa)
	chinmay.addChild(aamir)

	gels = TreeNode("Gels", "HR Head")
	gels.addChild(TreeNode("Peter", "Recruitment Manager"))
	gels.addChild(TreeNode("Waqas", "Policy Manager"))

	root.addChild(chinmay)
	root.addChild(gels)

	return root

def buildTreeExc2():
	root = TreeNode("Global")

	india = TreeNode("India")
	gujarat = TreeNode("Gujarat")
	gujarat.addChild(TreeNode("Ahmedabad"))
	gujarat.addChild(TreeNode("Baroda"))
	karnataka = TreeNode("Karnataka")
	karnataka.addChild(TreeNode("Bangluru"))
	karnataka.addChild(TreeNode("Mysore"))
	india.addChild(gujarat)
	india.addChild(karnataka)

	usa = TreeNode("USA")
	newJersey = TreeNode("New Jersey")
	newJersey.addChild(TreeNode("Princeton"))
	newJersey.addChild(TreeNode("Trenton"))
	california = TreeNode("California")
	california.addChild(TreeNode("San Francisco"))
	california.addChild(TreeNode("Mountain View"))
	california.addChild(TreeNode("Palo Alto"))
	usa.addChild(newJersey)
	usa.addChild(california)

	root.addChild(india)
	root.addChild(usa)

	return root


if __name__ == '__main__':
	root = buildTreeExc1() 
	root.printNodeExc1("designation")
	root.printNodeExc1("name")
	root.printNodeExc1("both")

	print()

	root = buildTreeExc2()
	root.printNodeExc2(1)
	root.printNodeExc2(2)
	root.printNodeExc2(3)


