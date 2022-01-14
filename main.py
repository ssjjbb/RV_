#Main program loop for Raspberry Pi 4
import PySimpleGUI as sg
import time

#Set up nicer theme for the GUI
sg.theme('DarkAmber')

#DataList updater function for GUI list element
#t1,2 = Temperature reading 1 and 2
#w1,2 = Water tank level reading 1 and 2
#switch = reed switch states, this might change later depending how multiple
#switches are implemented. In testing using boolean value to determine whether
#the state is open or closed. temp and water readings are FLOAT
def updateValue(t1, t2, w1, w2, switch):
    dataList = [t1, t2, w1, w2, switch]
    first_column = [
        [sg.Text("RV Current sensor data")],
        [sg.Table(values=[[dataList[0],
                           dataList[1],
                           dataList[2],
                           dataList[3],
                           dataList[4]]],
                  headings=('Temperature 1',
                            'Temperature 2',
                            'Water Level 1',
                            'Water Level 2',
                            'Switch states'),
                  max_col_width=50,
                  #background_color='light blue',
                  auto_size_columns=False,
                  justification='center',
                  num_rows=20,
                  row_height=20,
                  key='-DATALIST-',
                  hide_vertical_scroll=True
                  )],
        [sg.Button('Refresh', key='-REFRESH-')],
    ]
    updatedLayout = [[sg.Column(first_column)]]
    return updatedLayout



def main():
    screenHeight = 900
    screenWidth = 900
    tempRead1 = 0
    tempRead2 = 0
    waterRead1 = 0
    waterRead2 = 0
    switchRead = 'OK'



    while True:
        layout = updateValue(tempRead1, tempRead2, waterRead1, waterRead2, switchRead)
        window = sg.Window('GUI test window', layout, size = (screenWidth, screenHeight)).finalize()

        window.read()
        #Test part to update values on the layout. Abit tricky with pysimplegui since layout
        #creation is permanent. Might need to do 2 layouts and hide other and alternate between
        #2 layouts, updating the hidden one with new values

        tempRead1 = tempRead1 + 1
        tempRead2 = tempRead2 + 2
        waterRead1 = waterRead1 + 3
        waterRead2 = waterRead2 + 4
        event, values = window.read()

        if window == sg.WIN_CLOSED:
            window.close()
            break
        window.close()


if __name__ == '__main__':
    main()