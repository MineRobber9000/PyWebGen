class Page:
	def __init__(self,title):
		self.contents = ""
		self.head_contents = "<title>" + title + "</title>"

	def addElement(self, elemName, attrString, content, isHeadElement):
		if not isHeadElement:
			self.contents = self.contents + "<" + elemName + " " + attrString + ">" + content + "</" + elemName + ">"
		else:
			self.head_contents = self.head_contents + "<" + elemName + " " + attrString + ">" + content + "</" + elemName + ">"

	def export(self):
		return "<html><head>" + self.head_contents + "</head><body>" + self.contents + "</body></html>"

