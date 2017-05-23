from appJar import gui

def getEm(btn=None):
    if btn=="DELETE":
        app.deleteProperty("The props", app.getOptionBox("Prop"))
        # TODO: remove from OptionBox
        app.deleteOptionBox("Prop", app.getOptionBox("Prop"))

    else:
        print(app.getProperties("The props"))
        print(app.getProperty("The props", app.getOptionBox("Prop")))

def change(btn=None):
    app.setProperty("The props", app.getOptionBox("Prop"), app.getCheckBox("Value"))

def state(btn):
    if btn=="ENAB":
        app.setPropertiesState("The props", "normal")
    else:
        app.setPropertiesState("The props", "disabled")

props = {
            "Name":True, "Age":False,
            "Name1":True, "Age1":False,
            "Name2":True, "Age2":False,
            "Name3":True, "Age3":False
        }

app=gui()

app.setBg("lightBlue")
app.setFont(20)

#app.startToggleFrame("t")
#app.setSticky("nsew")
app.addProperties("The props", props)
#app.setPropertiesBg("The props", "yellow")
#app.stopToggleFrame()
app.addButtons(["GET EM", "DELETE"], getEm)
app.addLabelOptionBox("Prop", ["Name", "Age", "Name1", "Age1", "Name2", "Age2", "Name3", "Age3"])
app.addCheckBox("Value")
app.setCheckBoxFunction("Value", change)
app.setProperty("The props", "Super Prop")
app.addButtons(["ENAB", "DISAB"], state)
app.setProperties("The props", {"fred":True, "Apples":False, "Age":True})

app.setBg("red")
app.go()
