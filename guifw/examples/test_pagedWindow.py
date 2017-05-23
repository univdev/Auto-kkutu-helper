from appJar import gui

def pos(btn):
    if btn=="top":
        app.setPagedWindowButtonsTop("PagedWindow", True)
    elif btn=="bottom":
        app.setPagedWindowButtonsTop("PagedWindow", False)
    elif btn=="hide":
        app.showPagedWindowPageNumber("PagedWindow", False)
    elif btn=="show":
        app.showPagedWindowPageNumber("PagedWindow", True)
    elif btn=="titleOn":
        app.showPagedWindowTitle("PagedWindow", True)
    elif btn=="titleOff":
        app.showPagedWindowTitle("PagedWindow", False)
    elif btn=="tbOn":
        app.showToolbar()
    elif btn=="tbOff":
        app.hideToolbar()

def pageChanged(pager):
    app.setStatus(pager + " - " + str(app.getPagedWindowPageNumber(pager)))

app=gui("Pages", "280x400")
app.setBg("old lace")
app.setFont(20)
app.addToolbar(["top", "hide", "show","bottom", "titleOn", "titleOff"], pos)
app.addStatus()

app.startPagedWindow("PagedWindow")
#app.setBg("blue")
app.setPagedWindowButtons("PagedWindow", ["<<", ">>"])
app.setPagedWindowTitle("PagedWindow", "Random Stuff")
app.setPagedWindowFunction("PagedWindow", pageChanged)

app.startPage("PagedWindow")
app.addLabel("l11", "Label 1")
app.addLabel("l12", "Label 1")
app.addLabel("l13", "Label 1")
app.addButtons(["tbOn", "tbOff"], pos)
app.stopPage()

app.startPage("PagedWindow")
app.addLabel("l21", "Label 2")
app.addLabel("l22", "Label 2")
app.addLabel("l23", "Label 2")
app.addLabel("l24", "Label 2")
app.setBg("orange")
app.stopPage()

app.startPage("PagedWindow")
app.setBg("green")
app.addLabel("l3", "Label 3")
app.stopPage()

app.startPage("PagedWindow")
app.addLabel("l4", "Label 4")
app.stopPage()

app.startPage("PagedWindow")
app.addLabel("l5", "Label 5")
app.stopPage()

app.startPage("PagedWindow")
app.addLabel("l6", "Label 6")
app.stopPage()
app.startPage("PagedWindow")
app.addLabel("l7", "Label 6")
app.stopPage()
app.startPage("PagedWindow")
app.addLabel("l8", "Label 6")
app.stopPage()
app.startPage("PagedWindow")
app.addLabel("l9", "Label 6")
app.stopPage()
app.startPage("PagedWindow")
app.addLabel("l100", "Label 6")
app.stopPage()
app.startPage("PagedWindow")
app.addLabel("l101", "Label 6")
app.stopPage()
app.startPage("PagedWindow")
app.addLabel("l102", "Label 6")
app.stopPage()
app.startPage("PagedWindow")
app.addLabel("l103", "Label 6")
app.stopPage()
app.startPage("PagedWindow")
app.addLabel("l104", "Label 6")
app.stopPage()

app.stopPagedWindow()
app.go()
