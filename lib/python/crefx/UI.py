from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2 import QtCore

from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui


def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)

class BlockBuilder(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(BlockBuilder, self).__init__()

        self.setParent(maya_main_window())
        self.setWindowFlags(QtCore.Qt.Window)

        # Set the object name
        self.setObjectName('CreateBlockUI_UniqueId')
        self.setWindowTitle('Create Block')
        self.setGeometry(50, 50, 250, 250)

        # text and textbox for block_name
        self.textFieldBlockName = QtWidgets.QLineEdit(self, text="Arm")
        self.textFieldBlockName.setGeometry(80, 10, 150, 30)
        self.textPrefix = QtWidgets.QLabel(self, text="Block Name")
        self.textPrefix.setGeometry(10,10,70,30)

        # text and textbox for prefix
        self.textFieldPrefix = QtWidgets.QLineEdit(self, text="L")
        self.textFieldPrefix.setGeometry(80, 40, 150, 30)
        self.textPrefix = QtWidgets.QLabel(self, text="Block Prefix")
        self.textPrefix.setGeometry(10,40,70,30)

        # text and textbox for joint_one
        self.textFieldJointOne = QtWidgets.QLineEdit(self, text="Shoulder")
        self.textFieldJointOne.setGeometry(80, 70, 150, 30)
        self.textPrefix = QtWidgets.QLabel(self, text="Joint One")
        self.textPrefix.setGeometry(10,70,70,30)

        # text and textbox for joint_two
        self.textFieldJointTwo = QtWidgets.QLineEdit(self, text="Elbow")
        self.textFieldJointTwo.setGeometry(80, 100, 150, 30)
        self.textPrefix = QtWidgets.QLabel(self, text="Joint Two")
        self.textPrefix.setGeometry(10,100,70,30)

        # text and textbox for joint_three
        self.textFieldJointThree = QtWidgets.QLineEdit(self, text="Wrist")
        self.textFieldJointThree.setGeometry(80, 130, 150, 30)
        self.textPrefix = QtWidgets.QLabel(self, text="Joint Three")
        self.textPrefix.setGeometry(10,130,70,30)

        # button to call the buildBlock function
        self.button = QtWidgets.QPushButton(self, text="Build")
        self.button.setGeometry(50, 160, 150, 30)

        self.button.clicked.connect(self.buildBlock)

    def buildBlock(self):
        prefix = self.textFieldPrefix.text()
        joint_one = self.textFieldJointOne.text()
        joint_two = self.textFieldJointTwo.text()
        joint_three = self.textFieldJointThree.text()
        block_name = self.textFieldBlockName.text()

        import crefx.blockBuilder as bb
        reload(bb)

        block = bb.ThreeJointIK(prefix=prefix,
                                joint_one=joint_one,
                                joint_two=joint_two,
                                joint_three=joint_three,
                                block_name=block_name)
        block.build()

        print "build block", prefix + '_' + block_name

try:
    ui.deleteLater()
except NameError as e:
    pass

ui = BlockBuilder()
ui.show()
