import PySimpleGUI as sg                        # Part 1 - The import
import tools as tls

import os
# Define the window's contents

layout = [[sg.T('Input Path and Tag Filters:'), sg.In(key='-Input-'), sg.Button('Show')],
    [sg.Button('Tag Cloud'), sg.Button('Graph View')],
    [sg.Listbox(values=[], size=(80, 12), key='-LIST-')]
]

# Create the window
window = sg.Window('Tagtics File Organiser', layout)      # Part 3 - Window Defintion

path_prev = None
while True:  # Event Loop
    event, values = window.read()
        
    # parse input and strip whitespace
    parsed_input = values['-Input-'].split('#')
    path = parsed_input[0].strip()
    tags = [tag.strip() for tag in parsed_input[1:]]
        
    # we don't want to scrap the directory tree everytime we query
    if path_prev != path: 
        files = tls.FileMetaData(path)
       
    #print(files.Tags)
    FilteredFiles = files.filter(tags)

    # Update the "output"
    if event == 'Show': 
        window['-LIST-'].update(FilteredFiles)
    
    if event == 'Tag Cloud':
        files.PlotTagCloud()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    
    path_prev = path
window.close()