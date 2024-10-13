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
        self.pushButton.clicked.connect(self.main)

    def main(self):
        # 变量初始化
        map_id = ""
        num = 0
        switch_about = [True, False, True]
        # 检测输入情况(第一次)
        self.plainTextEdit.appendPlainText("On examination...")
        if self.lineEdit_6.text() == "":
            self.plainTextEdit_2.appendPlainText("请先输入地图画的编号!")
            self.plainTextEdit.appendPlainText("Error found!")
        try:
            map_id = int(self.lineEdit_6.text())
        except ValueError:
            self.plainTextEdit_2.appendPlainText("请输入正确的地图画编号!")
            self.plainTextEdit.appendPlainText("Error found!")
            self.lineEdit_6.clear()
            switch_about[0] = False
            switch_about[2] = False

        if switch_about[2]:
            if self.lineEdit.text() == "":
                if self.lineEdit_2.text() == "" and self.lineEdit_3.text() == "":
                    if self.lineEdit_4.text() == "" and self.lineEdit_5.text() == "":
                        self.plainTextEdit_2.appendPlainText("请输入信息!")
                        self.plainTextEdit.appendPlainText("Error found!")
                    try:
                        num = (
                            int(self.lineEdit_5.text())
                            - int(self.lineEdit_4.text())
                            + 1
                        )
                    except ValueError:
                        self.plainTextEdit_2.appendPlainText("请输入正确的地图画编号!")
                        self.plainTextEdit.appendPlainText("Error found!")
                        self.lineEdit_4.clear()
                        self.lineEdit_5.clear()
                        switch_about[0] = False
                else:
                    try:
                        num = int(self.lineEdit_2.text()) * int(self.lineEdit_3.text())
                    except ValueError:
                        self.plainTextEdit_2.appendPlainText("请输入正确的长宽!")
                        self.plainTextEdit.appendPlainText("Error found!")
                        self.lineEdit_2.clear()
                        self.lineEdit_3.clear()
                        switch_about[0] = False
            else:
                try:
                    num = int(self.lineEdit.text())
                except ValueError:
                    self.plainTextEdit_2.appendPlainText("请输入正确的地图画编号!")
                    self.plainTextEdit.appendPlainText("Error found!")
                    self.lineEdit.clear()
                    switch_about[0] = False
        # 检测输入情况(第二次)
        if switch_about[0]:
            if num > 729:
                self.plainTextEdit_2.appendPlainText(
                    "你生成地图画数量太多了，试试分段生成吧!"
                )
                self.plainTextEdit.appendPlainText("Error:Number of map drawings > 729")
                self.lineEdit_2.clear()
                self.lineEdit_3.clear()
                self.lineEdit.clear()
                self.lineEdit_4.clear()
                self.lineEdit_5.clear()
            elif num < 0:
                self.plainTextEdit_2.appendPlainText("请不要输入负数!")
                self.plainTextEdit.appendPlainText("Error:Number of map drawings < 0")
                self.lineEdit_2.clear()
                self.lineEdit_3.clear()
                self.lineEdit.clear()
                self.lineEdit_4.clear()
                self.lineEdit_5.clear()
            elif map_id < 0:
                self.plainTextEdit_2.appendPlainText("请不要输入负的地图画编号!")
                self.plainTextEdit.appendPlainText(
                    "Error:Map drawing number is negative"
                )
                self.lineEdit_6.clear()
            else:
                switch_about[1] = True

        self.plainTextEdit_2.appendPlainText("检查完成!")

        # 主程序

        # 变量初始化
        # 声明变量-1
        self.plainTextEdit.appendPlainText("Variable Initialization -1")
        map_1 = "{Count:1b,Slot:"  # 后面跟上在潜影盒里面的位置
        map_2 = 'b,id:"minecraft:filled_map",tag:{map:'  # 后面跟上地图画编号
        map_3 = "}}"  # 结尾

        shulker_noinbox_1 = '{Count:1b,id:"minecraft:white_shulker_box",tag:{BlockEntityTag:{Items:['  # 后面跟上地图画
        shulker_noinbox_2 = '],id:"minecraft:shulker_box"},display:{Name:\'{"italic":false,"extra":[{"text":""},{"bold":true,"color":"white","text":"'  # 后面跟上范围
        shulker_noinbox_3 = '"}],"text":""}\'}}}'  # 结尾

        shulker_inbox_1 = "{Count:1b,Slot:"  # 后面跟上在箱子里面的位置
        shulker_inbox_2 = 'b,id:"minecraft:white_shulker_box",tag:{BlockEntityTag:{Items:['  # 后面跟上地图画
        shulker_inbox_3 = '],id:"minecraft:shulker_box"},display:{Name:\'{"italic":false,"extra":[{"text":""},{"bold":true,"color":"white","text":"'  # 后面跟上范围
        shulker_inbox_4 = '"}],"text":""}\'}}}'  # 结尾

        box_1 = '{Count:1b,id:"minecraft:chest",tag:{BlockEntityTag:{Items:['  # 后面跟上潜影盒
        box_2 = '],id:"minecraft:chest"},display:{Name:\'{"italic":false,"extra":[{"text":""},{"bold":true,"color":"white","text":"'  # 后面跟上范围
        box_3 = '"}],"text":""}\'}}}'  # 结尾

        # 声明变量-2
        self.plainTextEdit.appendPlainText("Variable Initialization -2")
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
            self.plainTextEdit.appendPlainText("Variable Initialization -1")
            # 使用一个潜影盒能装下的
            self.plainTextEdit_2.appendPlainText("生成ing...")
            self.plainTextEdit.appendPlainText("Generating in progress...")
            if switch[0]:
                text_start += shulker_noinbox_1
                # 遍历地图画
                for i in range(num):
                    if i + 1 != num:
                        text_middle += f"{map_1}{i}{map_2}{map_id+i}{map_3},"
                    else:
                        text_middle += f"{map_1}{i}{map_2}{map_id+i}{map_3}"
                text += f"{text_start}{text_middle}{shulker_noinbox_2}{map_id}~{map_id+num-1}{shulker_noinbox_3}"
                self.plainTextEdit_2.appendPlainText(
                    f"生成完成!已复制到你的剪切板!\n累计生成{len(text)}字符\n总地图画数量:{num}\n总像素:{num*128*128}\n范围:{map_id}~{map_id+num-1}"
                )
                self.plainTextEdit.appendPlainText(
                    f"Generation completed!\nTotal number of map drawings:{num}\nTotal pixels:{num*128*128}\nRange:{map_id}~{map_id+num-1}"
                )
                pyperclip.copy(text)
                self.lineEdit_6.clear()
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
                        text_start += f"{shulker_inbox_1}{i}{shulker_inbox_2}"
                        # 如果循环到末尾
                        if i == shulker_num:
                            for j in range(num_remainder):
                                if j + 1 == num_remainder:
                                    text_middle += f"{map_1}{j}{map_2}{map_id+j}{map_3}"
                                else:
                                    text_middle += (
                                        f"{map_1}{j}{map_2}{map_id+j}{map_3},"
                                    )
                                map_num += 1
                            map_id += num_remainder
                        else:
                            for l in range(27):
                                if l + 1 == 27:
                                    text_middle += f"{map_1}{l}{map_2}{map_id+l}{map_3}"
                                else:
                                    text_middle += (
                                        f"{map_1}{l}{map_2}{map_id+l}{map_3},"
                                    )
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
                        text_start += f"{shulker_inbox_1}{i}{shulker_inbox_2}"
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
                self.plainTextEdit_2.appendPlainText(
                    f"生成完成!已复制到你的剪切板!\n累计生成{len(text)}字符\n总地图画数量:{num}\n总像素:{num*128*128}\n范围:{map_id}~{map_id+num-1}"
                )
                self.plainTextEdit.appendPlainText(
                    f"Generation completed!\nTotal number of map drawings:{num}\nTotal pixels:{num*128*128}\nRange:{map_id}~{map_id+num-1}"
                )
                pyperclip.copy(text)
                self.lineEdit_6.clear()

        self.plainTextEdit_2.appendPlainText("-----------------------------")
        self.plainTextEdit.appendPlainText("-----------------------------")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
