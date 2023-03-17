import pyautogui
import time


def mouse_pos(sec):
    # sec停留时间
    # 鼠标指定截图区域，返回point(x,y)
    pyautogui.alert(text=f'点击ok后，在{sec}秒内鼠标移动到下一周按钮上，将记录位置', title='开始', button='ok')
    time.sleep(sec)
    pos = pyautogui.position()
    print(pos[0], pos[1])
    pyautogui.alert(text=f'位置获取已结束\n位置是{pos[0]} {pos[1]}', title='结束', button='ok')
    return pos


# def mouse_color():
#     pyautogui.confirm('请将鼠标动到日程背景颜色上')
#     time.sleep(2)
#     pos1 = pyautogui.position()
#     color = pyautogui.pixel(pos1[0], pos1[1])
#     print(color)
#     return color


def delete_blue():
    # pyautogui.alert(text='点击ok后，在5秒内切换到日历', title='删除blue', button='ok')
    time.sleep(6)
    condition = True
    # 获取背景颜色
    # bg_color = mouse_color()
    # 删除一周
    while condition:
        try:
            x, y = pyautogui.locateCenterOnScreen('blue3.png')
        except TypeError:
            print(1)
            print('no find blue')
            condition = False
            break

        # if pyautogui.pixelMatchesColor(x, y, bg_color):
        # print('确认颜色')
        print('blue 的坐标%d %d', (x, y))
        pyautogui.moveTo(x, y, duration=0.15)
        pyautogui.click(button='right')
        try:
            delete_x, delete_y = pyautogui.locateCenterOnScreen('delete.png')
        except TypeError:
            print('no find delete')
        print('删除的坐标%d, %d', (delete_x, delete_y))
        pyautogui.moveTo(delete_x, delete_y, duration=0.15)
        pyautogui.click(button='left')

        # else:
        #     continue


def delete_week():
    pyautogui.alert(text='打开日历', title='开始', button='OK')
    next_pos = mouse_pos(3)    # 获取下一周按钮位置
    try:
        num = int(pyautogui.prompt(text='输入要删除的周数', title='输入', default='1'))
    except TypeError:
        print('未输入')
    for i in range(num):
        delete_blue()
        print("第%d次循环", i)
        pyautogui.moveTo(next_pos[0], next_pos[1], duration=0.15)
        pyautogui.click(button='left')
    pyautogui.alert(text='已完成', title='完成', button='关闭提示')


delete_week()
