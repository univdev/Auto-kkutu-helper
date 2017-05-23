import sys
sys.path.append("../")
from appJar import gui

clicked = False
animated = True


photo="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"

def changePic(btn):
    if btn == "clickme":
        global clicked
        if clicked: app.setImage("clickme", "balloons.gif")
        else: app.setImage("clickme", "balloons2.png")
        clicked = not clicked
    elif btn == "No reload":
        app.setImage("no_reload", "balloons.gif")
    elif btn == "Reload":
        app.reloadImage("reload", "balloons.gif")
    elif btn == "Stop":
        global animated
        if animated:
            app.stopAnimation("animated")
            app.setButton("Stop", "Start")
        else:
            app.startAnimation("animated")
            app.setButton("Stop", "Stop")
        animated = not animated
    elif btn == "Speed":
        app.setAnimationSpeed("animated", app.getScale("Speed"))
    elif btn == "Zoom":
        app.zoomImage("Zoom", int(app.getSpinBox("Zoom")))
    elif btn == "Open":
        imgPath = app.openBox(title="Open Image", dirName="images", fileTypes=[('images', '*.png'), ('images', '*.jpg'), ('images', '*.gif'), ('images', '*.jpeg'), ('all', '*')])
        if imgPath != "":
            try:
                app.setImage("Open", imgPath)
            except:
                app.errorBox("File error", "Unable to open image: " + str(imgPath))

app=gui("Image Test")
app.setImageLocation("images")

app.startLabelFrame("Image Data", 0, 0)
app.addImageData("imgdata", photo)
app.stopLabelFrame()


app.startLabelFrame("Simple", 0, 1)
app.addImage("simple", "balloons.gif")
app.stopLabelFrame()

app.startLabelFrame("Mouse Over", 0, 2)
app.addImage("mo_1", "balloons.gif")
app.setImageMouseOver("mo_1", "balloons2.png")
app.stopLabelFrame()

app.startLabelFrame("Click Me", 0, 3)
app.addImage("clickme", "balloons.gif")
app.setImageFunction("clickme", changePic)
app.stopLabelFrame()

app.startLabelFrame("Zoom", 0, 4)
app.setPadding([5,5])
app.setSticky("ew")
app.startScrollPane("sp")
app.addImage("Zoom", "balloons.gif")
w, h = app.getImageDimensions("simple")
app.stopScrollPane()
app.setScrollPaneWidth("sp", 150)
app.addLabelSpinBox("Zoom", [20,5, 4, 3, 2, 1, -2, -3, -4, -5, -6, -7, -8, -9])
app.setSpinBox("Zoom", 1)
app.setSpinBoxFunction("Zoom", changePic)
app.stopLabelFrame()

app.startLabelFrame("No reload", 1, 1)
app.setSticky("ew")
app.addImage("no_reload", "balloons.gif")
app.addButton("No reload", changePic)
app.stopLabelFrame()

app.startLabelFrame("Reload", 1, 2)
app.setSticky("ew")
app.addImage("reload", "balloons.gif")
app.addButton("Reload", changePic)
app.stopLabelFrame()

app.startLabelFrame("Animated", 1, 3)
app.setSticky("ew")
app.addImage("animated", "animated_balloons.gif")
app.addLabelScale("Speed")
app.showScaleValue("Speed")
app.showScaleIntervals("Speed", 50)
app.setScaleRange("Speed", 1, 200, 50)
app.setScaleFunction("Speed", changePic)
app.addButton("Stop", changePic)
app.stopLabelFrame()

app.startLabelFrame("Open", 1, 4)
app.setSticky("ew")
app.addImage("Open", "balloons3.jpg")
app.addButton("Open", changePic)
app.stopLabelFrame()

app.go()
