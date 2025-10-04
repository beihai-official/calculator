from tkinter import *
from tkinter.ttk import *
import sys
import os
import winsound  # 用于播放按键声音（Windows专用）

# ---------------- 资源路径 ----------------


def resource_path(relative_path):
    """获取资源文件的绝对路径（兼容打包后）"""
    if getattr(sys, 'frozen', False):  # 如果是打包后的exe
        base_path = sys._MEIPASS
    else:  # 普通脚本运行
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ---------------- 播放声音 ----------------


def play_sound():
    winsound.PlaySound(resource_path("press.wav"),
                       winsound.SND_FILENAME | winsound.SND_ASYNC)

# ---------------- 窗口UI ----------------


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        # 数字按钮
        self.tk_button_num7 = self.__tk_button_num7(self)
        self.tk_button_num8 = self.__tk_button_num8(self)
        self.tk_button_num9 = self.__tk_button_num9(self)
        self.tk_button_num6 = self.__tk_button_num6(self)
        self.tk_button_num5 = self.__tk_button_num5(self)
        self.tk_button_num4 = self.__tk_button_num4(self)
        self.tk_button_num1 = self.__tk_button_num1(self)
        self.tk_button_num2 = self.__tk_button_num2(self)
        self.tk_button_num0 = self.__tk_button_num0(self)
        self.tk_button_num3 = self.__tk_button_num3(self)

        # 运算按钮
        self.tk_button_times = self.__tk_button_times(self)
        self.tk_button_divide = self.__tk_button_divide(self)
        self.tk_button_sum = self.__tk_button_sum(self)
        self.tk_button_subtract = self.__tk_button_subtract(self)
        self.tk_button_equals = self.__tk_button_equals(self)
        self.tk_button_clean = self.__tk_button_clean(self)

        # 显示框
        self.tk_entry_display = self.__tk_text_entry(self)

    def __win(self):
        self.title("计算器 -- beihaimc")
        width, height = 402, 565
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2,
                                    (screenheight - height) / 2)
        self.iconbitmap(resource_path("icon.ico"))
        self.geometry(geometry)
        self.resizable(width=False, height=False)

    # ---------- 数字按钮 ----------
    def __tk_button_num7(self, parent): btn = Button(
        parent, text="7", takefocus=False); btn.place(x=0, y=318, width=100, height=60); return btn

    def __tk_button_num8(self, parent): btn = Button(
        parent, text="8", takefocus=False); btn.place(x=102, y=318, width=100, height=60); return btn

    def __tk_button_num9(self, parent): btn = Button(
        parent, text="9", takefocus=False); btn.place(x=204, y=318, width=100, height=60); return btn

    def __tk_button_num6(self, parent): btn = Button(
        parent, text="6", takefocus=False); btn.place(x=204, y=380, width=100, height=60); return btn

    def __tk_button_num5(self, parent): btn = Button(
        parent, text="5", takefocus=False); btn.place(x=102, y=380, width=100, height=60); return btn

    def __tk_button_num4(self, parent): btn = Button(
        parent, text="4", takefocus=False); btn.place(x=0, y=380, width=100, height=60); return btn

    def __tk_button_num1(self, parent): btn = Button(
        parent, text="1", takefocus=False); btn.place(x=0, y=442, width=100, height=60); return btn

    def __tk_button_num2(self, parent): btn = Button(
        parent, text="2", takefocus=False); btn.place(x=102, y=442, width=100, height=60); return btn

    def __tk_button_num0(self, parent): btn = Button(
        parent, text="0", takefocus=False); btn.place(x=0, y=504, width=100, height=60); return btn

    def __tk_button_num3(self, parent): btn = Button(
        parent, text="3", takefocus=False); btn.place(x=204, y=442, width=100, height=60); return btn

    # ---------- 运算按钮 ----------
    def __tk_button_times(self, parent): btn = Button(
        parent, text="×", takefocus=False); btn.place(x=306, y=318, width=95, height=60); return btn

    def __tk_button_divide(self, parent): btn = Button(
        parent, text="÷", takefocus=False); btn.place(x=306, y=380, width=95, height=60); return btn

    def __tk_button_sum(self, parent): btn = Button(
        parent, text="＋", takefocus=False); btn.place(x=306, y=442, width=95, height=60); return btn

    def __tk_button_subtract(self, parent): btn = Button(
        parent, text="-", takefocus=False); btn.place(x=306, y=504, width=95, height=60); return btn

    def __tk_button_equals(self, parent): btn = Button(
        parent, text="=", takefocus=False); btn.place(x=204, y=504, width=100, height=60); return btn

    def __tk_button_clean(self, parent): btn = Button(
        parent, text="AC", takefocus=False); btn.place(x=102, y=504, width=100, height=60); return btn

    # ---------- 显示框 ----------
    def __tk_text_entry(self, parent): entry = Entry(parent, font=(
        "Arial", 24), justify="right"); entry.place(x=0, y=5, width=402, height=312); return entry

# ---------------- 控制器 ----------------


class Controller:
    def init(self, view): self.view, self.expression = view, ""

    def append_number(self, num): self.expression += num; self.view.tk_entry_display.delete(
        0, "end"); self.view.tk_entry_display.insert("end", self.expression)

    def append_operator(self, op): self.expression += op; self.view.tk_entry_display.delete(
        0, "end"); self.view.tk_entry_display.insert("end", self.expression)

    def clear(self): self.expression = ""; self.view.tk_entry_display.delete(
        0, "end")

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.view.tk_entry_display.delete(0, "end")
            self.view.tk_entry_display.insert("end", result)
            self.expression = result
        except Exception:
            self.view.tk_entry_display.delete(0, "end")
            self.view.tk_entry_display.insert("end", "Error")
            self.expression = ""

# ---------------- 窗口绑定 ----------------


class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.ctl.init(self)
        self.__event_bind()
        self.__keyboard_bind()  # 绑定键盘输入

    def __event_bind(self):
        # 数字按钮绑定
        for i, btn in enumerate([
            self.tk_button_num0, self.tk_button_num1, self.tk_button_num2,
            self.tk_button_num3, self.tk_button_num4, self.tk_button_num5,
            self.tk_button_num6, self.tk_button_num7, self.tk_button_num8,
            self.tk_button_num9
        ]):
            btn.config(command=lambda x=str(i): [
                       self.ctl.append_number(x), play_sound()])

        # 运算符绑定
        self.tk_button_sum.config(
            command=lambda: [self.ctl.append_operator("+"), play_sound()])
        self.tk_button_subtract.config(
            command=lambda: [self.ctl.append_operator("-"), play_sound()])
        self.tk_button_times.config(
            command=lambda: [self.ctl.append_operator("*"), play_sound()])
        self.tk_button_divide.config(
            command=lambda: [self.ctl.append_operator("/"), play_sound()])

        # 功能键绑定
        self.tk_button_clean.config(
            command=lambda: [self.ctl.clear(), play_sound()])
        self.tk_button_equals.config(
            command=lambda: [self.ctl.calculate(), play_sound()])

    # ---------- 键盘绑定 ----------
    def __keyboard_bind(self):
        self.bind("<Key>", self.on_key_press)

    def on_key_press(self, event):
        key = event.char
        if key.isdigit():  # 数字键
            self.ctl.append_number(key)
            play_sound()
        elif key in "+-*/":  # 运算符
            self.ctl.append_operator(key)
            play_sound()
        elif key == "\r":  # 回车
            self.ctl.calculate()
            play_sound()
        elif key in "\x08\x1b":  # Backspace 或 Esc 清空
            self.ctl.clear()
            play_sound()


# ---------------- 主程序 ----------------
if __name__ == "__main__":
    ctl = Controller()
    win = Win(ctl)
    win.mainloop()
