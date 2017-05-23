import sys
sys.path.append("../../")
from appJar import gui

app = gui()
app.setGeometry("400x400")

#app.setSticky("nsew")      #n, s, e, w
#app.setStretch()           #none, row, column, both

# add the widgets
app.addLabel("1", "1", 0, 0, 3) # span 3 cols
app.addLabel("2", "2", 1)
app.addLabel("3", "3", 1, 1, 0, 3) # span 3 rows
app.addLabel("4", "4", 1, 2)
app.addLabel("5", "5", 0, 3, 0, 2) # span 2 rows
app.addLabel("6", "6", 2)
app.addLabel("7", "7", 2, 2, 2) # span 3 cols

# set some colours
app.setLabelBg("1", "red")
app.setLabelBg("2", "blue")
app.setLabelBg("3", "green")
app.setLabelBg("4", "yellow")
app.setLabelBg("5", "pink")
app.setLabelBg("6", "purple")
app.setLabelBg("7", "orange")

app.go()
