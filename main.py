import PySimpleGUI as sg                        # Part 1 - The import
import tools as tls

import os
# Define the window's contents

layout = [[sg.T('Input Path and Tag Filters:'), sg.In(key='-Input-'), sg.Button('Show')],
    [sg.Listbox(values=[], size=(80, 12), key='-LIST-')]
]

# Create the window
window = sg.Window('Tagtics File Organiser', layout)      # Part 3 - Window Defintion

path_prev = None
while True:  # Event Loop
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show': 
        
        # parse input 
        parsed_input = values['-Input-'].split('#')
        path = parsed_input[0].strip()
        tags = parsed_input[1:]

        if path_prev != path: # we don't want to scrap the directory tree everytime
            files = tls.FileMetaData(path)
       
        print(files.Tags)
        FilteredFiles = files.filter(tags)

        # Update the "output" 
        window['-LIST-'].update(FilteredFiles)
       

        '''
        for tag in tags:
            window['-OUTPUT-'].update
        '''
    path_prev = path
window.close()