from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor, QPixmap
from Ui_main import Ui_Form
import pyperclip


class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind()

    def bind(self):
        self.lineEdit.setDisabled(True)
        self.lineEdit_2.setDisabled(True)
        self.lineEdit_3.setDisabled(True)
        self.lineEdit_4.setDisabled(True)
        self.lineEdit_5.setDisabled(True)
        self.pushButton.setDisabled(True)
        self.radioButton.toggled.connect(self.check)
        self.radioButton_2.toggled.connect(self.check_2)
        self.radioButton_3.toggled.connect(self.check_3)
        self.pushButton.clicked.connect(self.main)

    def main(self):
        # 变量初始化
        map_id = ""
        num = 0
        switch_about = [False, False, False]

        # 检测第一个遍历的地图画
        self.plainTextEdit.appendPlainText("检查中...")
        if self.inputEdit.text() == "":
            self.plainTextEdit.appendPlainText("请先输入地图画的编号!")
            switch_about[1] == False
        else:
            try:
                map_id = int(self.inputEdit.text())
                if map_id < 0:
                    self.plainTextEdit.appendPlainText(
                        "地图画编号不得为负!"
                    )
                    self.inputEdit.clear()
                    switch_about[1] == False
                else:
                    switch_about[1] = True
            except ValueError:
                self.plainTextEdit.appendPlainText(
                    "请输入正确的地图画编号!"
                )
                self.inputEdit.clear()
                switch_about[1] == False

        # 检测输入是否为空 & 是否为正整数
        if switch_about[1]:
            if self.radioButton.isChecked():
                if self.lineEdit.text() == "":
                    self.plainTextEdit.appendPlainText(
                        "请输入地图画遍历的数量!"
                    )
                    switch_about[0] == False
                else:
                    try:
                        num = int(self.lineEdit.text())
                        if num < 0:
                            self.plainTextEdit.appendPlainText(
                                "地图画数量不得为负!"
                            )
                            self.lineEdit.clear()
                            switch_about[0] = False
                        elif num > 729:
                            self.plainTextEdit.appendPlainText(
                                "遍历地图画数量太多了，试试分段输入吧!"
                            )
                            self.lineEdit.clear()
                            switch_about[0] = False
                        else:
                            switch_about[0] = True
                    except ValueError:
                        self.plainTextEdit.appendPlainText(
                            "请输入正确的地图画数量!"
                        )
                        self.lineEdit.clear()
                        switch_about[0] = False
            elif self.radioButton_2.isChecked():
                if (
                    self.lineEdit_2.text() == ""
                    and self.lineEdit_3.text() == ""
                ):
                    self.plainTextEdit.appendPlainText(
                        "请输入地图画的长宽!"
                    )
                    switch_about[0] == False
                elif self.lineEdit_2.text() == "":
                    self.plainTextEdit.appendPlainText(
                        "请输入地图画的宽度!"
                    )
                    switch_about[0] == False
                elif self.lineEdit_3.text() == "":
                    self.plainTextEdit.appendPlainText(
                        "请输入地图画的高度!"
                    )
                    switch_about[0] == False
                else:
                    try:
                        num = int(self.lineEdit_2.text()) * int(
                            self.lineEdit_3.text()
                        )
                        if num < 0:
                            self.plainTextEdit.appendPlainText(
                                "地图画的面积不得为负!"
                            )
                            self.lineEdit_2.clear()
                            self.lineEdit_3.clear()
                            switch_about[0] == False
                        elif num > 729:
                            self.plainTextEdit.appendPlainText(
                                "地图画的面积太大了，试试分段输入吧!"
                            )
                            self.lineEdit_2.clear()
                            self.lineEdit_3.clear()
                            switch_about[0] == False
                        else:
                            switch_about[0] = True
                    except ValueError:
                        self.plainTextEdit.appendPlainText(
                            "请输入正确的地图画的长宽!"
                        )
                        self.lineEdit_2.clear()
                        self.lineEdit_3.clear()
                        switch_about[0] == False
            elif self.radioButton_3.isChecked():
                if (
                    self.lineEdit_4.text() == ""
                    and self.lineEdit_5.text() == ""
                ):
                    self.plainTextEdit.appendPlainText(
                        "请输入两幅地图画的编号!"
                    )
                    switch_about[0] == False
                elif self.lineEdit_4.text() == "":
                    self.plainTextEdit.appendPlainText(
                        "请输入第一幅地图画的编号!"
                    )
                    switch_about[0] == False
                elif self.lineEdit_5.text() == "":
                    self.plainTextEdit.appendPlainText(
                        "请输入第二幅地图画的编号!"
                    )
                    switch_about[0] == False
                else:
                    try:
                        num = int(self.lineEdit_5.text()) - int(
                            self.lineEdit_4.text()
                        )
                        if num < 0:
                            self.plainTextEdit.appendPlainText(
                                "请检查一下地图画的先后顺序，看看是不是反了"
                            )
                            self.lineEdit_4.clear()
                            self.lineEdit_5.clear()
                            switch_about[0] == False
                        elif num > 729:
                            self.plainTextEdit.appendPlainText(
                                "地图画之间的差太大了，换一种方法吧!"
                            )
                            self.lineEdit_4.clear()
                            self.lineEdit_5.clear()
                            switch_about[0] == False
                        else:
                            switch_about[0] = True
                    except ValueError:
                        self.plainTextEdit.appendPlainText(
                            "请输入正确的地图画编号!"
                        )
                        self.lineEdit_4.clear()
                        self.lineEdit_5.clear()
                        switch_about[0] == False

        # 主程序

        # 判断
        if switch_about[0]:
            self.plainTextEdit.appendPlainText("检查完成!")
            self.plainTextEdit.appendPlainText("生成中...")
            # 变量初始化
            # 声明变量-1
            map_1 = "{Count:1b,Slot:"  # 后面跟上在潜影盒里面的位置
            map_2 = 'b,id:"minecraft:filled_map",tag:{map:'  # 后面跟上地图画编号
            map_3 = "}}"  # 结尾

            shulker_noinbox_1 = '{Count:1b,id:"minecraft:white_shulker_box",tag:{BlockEntityTag:{Items:['  # 后面跟上地图画
            shulker_noinbox_2 = '],id:"minecraft:shulker_box"},display:{Name:\'{"italic":false,"extra":[{"text":""},{"bold":true,"color":"white","text":"'  # 后面跟上范围
            shulker_noinbox_3 = '"}],"text":""}\'}}}'  # 结尾

            shulker_inbox_1 = (
                "{Count:1b,Slot:"  # 后面跟上在箱子里面的位置
            )
            shulker_inbox_2 = 'b,id:"minecraft:white_shulker_box",tag:{BlockEntityTag:{Items:['  # 后面跟上地图画
            shulker_inbox_3 = '],id:"minecraft:shulker_box"},display:{Name:\'{"italic":false,"extra":[{"text":""},{"bold":true,"color":"white","text":"'  # 后面跟上范围
            shulker_inbox_4 = '"}],"text":""}\'}}}'  # 结尾

            box_1 = '{Count:1b,id:"minecraft:chest",tag:{BlockEntityTag:{Items:['  # 后面跟上潜影盒
            box_2 = '],id:"minecraft:chest"},display:{Name:\'{"italic":false,"extra":[{"text":""},{"bold":true,"color":"white","text":"'  # 后面跟上范围
            box_3 = '"}],"text":""}\'}}}'  # 结尾

            # 声明变量-2
            switch = [False, False, False]
            # switch = [是否能用一个潜影盒装下,是否需要用到箱子,是否需要用到多个箱子]
            num_remainder = 0
            shulker_remainder = 0

            shulker_num = 1
            box_num = 1

            text_start = " "
            text_middle = " "
            text = " "

            # 判断数量
            if switch_about[1]:
                if num <= 27:
                    switch[0] = True
                elif num > 27 and num <= 729:
                    switch[1] = True
                    # 检测num/27是否为整数或有余数
                    if num % 27 == 0:
                        shulker_num = num // 27
                    else:
                        shulker_num = num // 27
                        num_remainder = num % 27
                else:
                    switch[2] = True
                    # 检测num/27是否为整数或有余数
                    if int(num % 27) == 0:
                        shulker_num = num // 27
                    else:
                        shulker_num = num // 27
                        num_remainder = num % 27

                    # 检测需要多少个箱子和潜影盒
                    if int(shulker_num % 27) == 0:
                        box_num = shulker_num // 27
                    else:
                        box_num = shulker_num // 27
                        shulker_remainder = shulker_num % 27
            if switch[0]:
                text_start += shulker_noinbox_1
                # 遍历地图画
                for i in range(num):
                    if i + 1 != num:
                        text_middle += (
                            f"{map_1}{i}{map_2}{map_id+i}{map_3},"
                        )
                    else:
                        text_middle += (
                            f"{map_1}{i}{map_2}{map_id+i}{map_3}"
                        )
                text += f"{text_start}{text_middle}{shulker_noinbox_2}{map_id}~{map_id+num-1}{shulker_noinbox_3}"
            elif switch[1]:
                # 箱子开头
                text_start += box_1
                # 循环潜影盒
                # 判断是否有余数
                map_id_1 = map_id
                map_id_2 = map_id
                map_num = 0
                map_num_copy = 0
                if num_remainder != 0:
                    for i in range(shulker_num + 1):
                        map_id_1 += map_num
                        map_id_1 -= map_num_copy
                        map_num_copy = map_num
                        # 潜影盒开头
                        text_start += (
                            f"{shulker_inbox_1}{i}{shulker_inbox_2}"
                        )
                        # 如果循环到末尾
                        if i == shulker_num:
                            for j in range(num_remainder):
                                if j + 1 == num_remainder:
                                    text_middle += f"{map_1}{j}{map_2}{map_id+j}{map_3}"
                                else:
                                    text_middle += f"{map_1}{j}{map_2}{map_id+j}{map_3},"
                                map_num += 1
                            map_id += num_remainder
                        else:
                            for l in range(27):
                                if l + 1 == 27:
                                    text_middle += f"{map_1}{l}{map_2}{map_id+l}{map_3}"
                                else:
                                    text_middle += f"{map_1}{l}{map_2}{map_id+l}{map_3},"
                                map_num += 1
                            map_id += 27

                        if i != shulker_num:
                            text_start += f"{text_middle}{shulker_inbox_3}{map_id_1}~{map_id_1+map_num-map_num_copy-1}{shulker_inbox_4},"
                        else:
                            text_start += f"{text_middle}{shulker_inbox_3}{map_id_1}~{map_id_1+map_num-map_num_copy-1}{shulker_inbox_4}"
                        text_middle = ""
                else:
                    for i in range(shulker_num):
                        map_id_1 += map_num
                        map_id_1 -= map_num_copy
                        map_num_copy = map_num
                        # 潜影盒开头
                        text_start += (
                            f"{shulker_inbox_1}{i}{shulker_inbox_2}"
                        )
                        # 循环地图画
                        for j in range(27):
                            if j + 1 == 27:
                                text_middle += f"{map_1}{j}{map_2}{map_id+j}{map_3}"
                            else:
                                text_middle += f"{map_1}{j}{map_2}{map_id+j}{map_3},"
                            map_num += 1
                        map_id += 27
                        if i != shulker_num:
                            text_start += f"{text_middle}{shulker_inbox_3}{map_id_1}~{map_id_1+map_num-map_num_copy-1}{shulker_inbox_4},"
                        else:
                            text_start += f"{text_middle}{shulker_inbox_3}{map_id_1}~{map_id_1+map_num-map_num_copy-1}{shulker_inbox_4}"
                        text_middle = ""
                text += f"{text_start}{box_2}{map_id_2}~{map_id_2+num-1}{box_3}"

            # 输出
            self.plainTextEdit.appendPlainText(
                f"生成完成!已复制到你的剪切板!\n累计生成{len(text)}字符\n总地图画数量:{num}\n总像素:{num*128*128}\n范围:{map_id}~{map_id+num-1}"
            )
            pyperclip.copy(text)
            self.inputEdit.clear()

        self.plainTextEdit.appendPlainText(
            "-----------------------------"
        )

    def check(self):
        if self.radioButton.isChecked():
            self.lineEdit.setDisabled(False)
            self.pushButton.setDisabled(False)
        else:
            self.lineEdit.setDisabled(True)

    def check_2(self):
        if self.radioButton_2.isChecked():
            self.lineEdit_2.setDisabled(False)
            self.lineEdit_3.setDisabled(False)
            self.pushButton.setDisabled(False)
        else:
            self.lineEdit_2.setDisabled(True)
            self.lineEdit_3.setDisabled(True)

    def check_3(self):
        if self.radioButton_3.isChecked():
            self.lineEdit_4.setDisabled(False)
            self.lineEdit_5.setDisabled(False)
            self.pushButton.setDisabled(False)
        else:
            self.lineEdit_4.setDisabled(True)
            self.lineEdit_5.setDisabled(True)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
