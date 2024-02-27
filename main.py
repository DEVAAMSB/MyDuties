import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QListWidget, QMessageBox
from PyQt5.QtGui import QIcon
class MyDuties(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowIcon(QIcon('keyboard.png'))
        self.setWindowTitle('My Duties')
        self.setGeometry(100, 100, 300, 400)
        
        # Layout
        layout = QVBoxLayout()
        
        # List widget
        self.taskList = QListWidget()
        
        # Line edit for new tasks
        self.newTaskLineEdit = QLineEdit()
        self.newTaskLineEdit.setPlaceholderText('Enter a new task...')
        
        # Buttons
        self.addTaskButton = QPushButton('Add Task')
        self.markCompletedButton = QPushButton('Mark as Completed')
        self.removeCompletedButton = QPushButton('Remove Completed Tasks')
        
        # Connect buttons to functions
        self.addTaskButton.clicked.connect(self.addTask)
        self.markCompletedButton.clicked.connect(self.markCompleted)
        self.removeCompletedButton.clicked.connect(self.removeCompletedTasks)
        
        # Add widgets to layout
        layout.addWidget(self.newTaskLineEdit)
        layout.addWidget(self.addTaskButton)
        layout.addWidget(self.markCompletedButton)
        layout.addWidget(self.removeCompletedButton)
        layout.addWidget(self.taskList)
        
        # Set the layout to the window
        self.setLayout(layout)
        
    def addTask(self):
        task = self.newTaskLineEdit.text().strip()
        if task:
            self.taskList.addItem(task)
            self.newTaskLineEdit.clear()
        else:
            QMessageBox.information(self, 'Empty Task', 'The task cannot be empty.', QMessageBox.Ok)
    
    def markCompleted(self):
        selectedItems = self.taskList.selectedItems()
        if not selectedItems:
            QMessageBox.information(self, 'No Task Selected', 'Please select a task to mark as completed.', QMessageBox.Ok)
            return
        for item in selectedItems:
            item.setCheckState(2)  # Qt.Checked
    
    def removeCompletedTasks(self):
        for i in range(self.taskList.count())[::-1]:
            if self.taskList.item(i).checkState() == 2:  # Qt.Checked
                self.taskList.takeItem(i)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyDuties = MyDuties()
    MyDuties.show()
    sys.exit(app.exec_())
