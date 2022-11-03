import PySimpleGUI as sg 
import os, shutil

def gui():
    #设置布局
    layout = [
        [sg.Text('THE File you choose:', font=("Hack", 15)),
        sg.Text('',key="text1", size = (30, 1), font = ("Hack",15))],
        
        [sg.Output(size = (50, 15), font = ("Hack",13))],
        [sg.FolderBrowse('Open',key = 'folder', target = 'text1'),
        sg.Button('Rename'),sg.Button('Close')]
    ]

    window = sg.window('File-size Cal', layout, font=("Hack",15))

    while True:
        event, values = window.read()
        if event in (None, 'Close'):
            break
        if event == 'Rename':
            if values['folder']:
                print('{0}Start{0}'.format('='*12))
                cal_size(values['folder'])
                print('{0}Over {0}'.format('='*12))
            else:
                print("You need choose file first!!!")
    window.close()

def total_func(file_path):
    file_sum_size = 0
    for f in os.listdir(file_path):
        f = os.path.join(file_path, f)
        n = os.path.getsize('f')
        file_sum_size = n + file_sum_size
    return file_sum_size




def cal_size(dir_path):
    for f in os.listdir(dir_path):
        file_path = os.path.join(dir_path, f)
        #判断是否为文件夹
        if not os.path.isdir(file_path):
            flie_size = total_func(file_path)
            print('{0} size is {1} B'.format(file_path, file_size))

def main():
    gui()

if __name__ == '__main__':
    main()

