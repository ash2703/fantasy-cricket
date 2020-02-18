from PySide import QtCore, QtGui

class List(QtGui.QDialog):

	def __init__(self):
		super(List, self).__init__()
		
		self._listWidget = QtGui.QListWidget()
		self._listWidget.addItems(['a', 'b', 'c'])

		self._red = QtGui.QBrush(QtCore.Qt.red)
		self._green = QtGui.QBrush(QtCore.Qt.green)

		layout = QtGui.QVBoxLayout(self)
		layout.addWidget(self._listWidget)

		self._listWidget.itemDoubleClicked.connect(self._handleDoubleClick)

	def _handleDoubleClick(self, item):
		color = item.background()
		item.setBackground(self._red if color == self._green else self._green)
		item.setSelected(False)


if __name__ == '__main__':
	app = QtGui.QApplication([])
	d = List()
	d.show()
	d.raise_()
	app.exec_()