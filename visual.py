from cmu_graphics import *
import test
import json

def onAppStart(app):
    app.user_input = ''
    app.file_button_x, app.file_button_y = 5, 5
    app.file_button_w, app.file_button_h = 150, 50
    app.raw_input_string = ''
    app.code_x, app.code_y = 10, 80
    app.indent = 15
    app.line_to_highlight = 1
    app.user_input_json = None
    app.line_number = 0
    app.line_index = 0
    app.lines = []
    app.current_line = None
    app.visual_dict = {
        "<class 'list'>" : drawList,
        "<class 'str'>" : drawVar,
        "<class 'int'>" : drawVar
    }

def redrawAll(app):
    drawLabel('Enter Code File', app.file_button_w // 2, app.file_button_h // 2, fill='black', size=18)
    drawRect(app.file_button_x, app.file_button_y, app.file_button_w, app.file_button_h, fill=None, border='black')
    drawCode(app)
    drawVisual(app)

def drawVisual(app):
    if app.current_line == None: return
    print(app.current_line)
    for data in app.current_line:
        data_value = app.current_line[data]
        if data != 'step_line':
            continue
        # TODO: try to visualize one thing first
        print(app.current_line[data])
    drawLabel(app.current_line, 200, 200)

def drawList(app):
    pass

def drawVar(app):
    pass

def drawCode(app):
    if app.raw_input_string == '': return
    i = 1
    for line in app.raw_input_string.splitlines():
        # print(repr(line))
        line_color = 'black'
        if i == app.line_to_highlight:
            line_color = 'green'
        drawLabel(line, app.code_x, app.code_y + (i-1) * app.indent, align='left', fill = line_color)
        i += 1

def onKeyPress(app, key):
    if key == 'right':
        lineUpdate(app, 1)
    elif key == 'left':
        lineUpdate(app, -1)
    if len(app.lines) > 0:
        app.line_to_highlight = app.lines[app.line_index]['line']

def lineUpdate(app, dir):
    if app.line_index + dir >= 0 and app.line_index + dir < len(app.lines):
        app.line_index += dir
        app.current_line = app.lines[app.line_index]

def onMousePress(app, mouseX, mouseY):
    if mouseX <= app.file_button_x + app.file_button_w and mouseX >= app.file_button_x and mouseY <= app.file_button_y + app.file_button_h and mouseY >= app.file_button_y:
        getUserInput(app)
        loadLines(app)

def getUserInput(app):
    raw_input = app.getTextInput('Code File')
    with open(raw_input, 'r') as file:
        app.raw_input_string = file.read()
    # print(app.raw_input_string)
    app.user_input = test.test_tracing(app.raw_input_string)

def loadLines(app):
    app.user_input_json = json.loads(app.user_input)
    # print(app.user_input_json)
    for line in app.user_input_json:
        app.lines.append(line)
    app.current_line = app.lines[0]

def main():
    runApp()

main()