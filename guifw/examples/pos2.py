from appJar import gui

app=gui()

app.setBg("blue")

app.setPadX(20)
app.setPadY(20)
app.setIPadX(40)
app.setIPadY(5)
app.setSticky("w")

app.addLabel("l1", "Label")
app.setLabelBg("l1", "yellow")



app.go()
