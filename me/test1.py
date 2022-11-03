import PySimpleGUI as sg    

import os,shutil

def gui():
    layout = [
        [sg.Text('THE File you choose:', font=("Hack", 10)),
        sg.Text('',key="text1", size = (40, 1), font = ("Hack",10))],
        
        [sg.Output(size = (50, 15), font = ("Hack",13))],
        [sg.FolderBrowse('Open',key ='folder',target='text1'),
        sg.Button('cal'),sg.Button('Close')]
    ] 
    sg.theme('GreenMono')
    window = sg.Window('The File-size Cal', layout)  
  
    while True:
        event, values = window.read()
        if event in (None, 'Close'):   
            break
        if event == 'cal':
            if values['folder']:
                print('{0}Start{0}'.format('='*20))
                cal(values['folder'])
                print('{0}Over{0}'.format('='*20))
            else:
                print("You need choose file first!!!")
  
    window.close()


 
def total_func(file_path):
    file_sum_size = 0
   
    if os.path.isdir(file_path):
        
        for f in os.listdir(file_path):
            
            f = os.path.join(file_path, f)
            n = os.path.getsize(f)
            file_sum_size = n + file_sum_size
    return file_sum_size
  
def cal(dir_path): 
    #print(dir_path)
    for file in os.listdir(dir_path):
        #print(file)
        past = file
        file_path = dir_path + '/' + file
        #print(file_path)

        if os.path.isdir(file_path):
            
            flie_size = total_func(file_path)
            print("The file \"%s\" size is %4f kB" % (past, flie_size/1024))
            
                

def main():  
    gui()

if __name__ == '__main__':
    main()        