#Events  
---
The whole point of GUIs is [events](https://en.wikipedia.org/wiki/Event-driven_programming)!   

We want events to be generated whenever the user does something, such as clicking a button, moving a scale, or pressing a key...

We also, sometimes, want events to happen repeatedly...

##Make stuff happen...
----
To make something happen you have to set a function for a widget.  
appJar currenly supports four basic use cases:  

* `.set XXX ChangeFunction(title, function)` call a function when the widget changes  
* `.set XXX SubmitFunction(title, function)` call a function when the widget is submitted    
* `.set XXX OverFunction(title, functions)` call function(s) when the mouse enters/leaves the widget  
* `.set XXX DragFunction(title, functions)` call function(s) when the mouse is dragged in/out of the widget  

###Breakdown  
---

* `.set XXX ChangeFunction(title, function)` & `.set XXX SubmitFunction(title, function)`  

    These do similar things, so probably shouldn't both exist, but have evolved from a single `.set XXX Function()` which is now deprecated.  

    They bind a function to the named widget.  

    For `ChangeFunction`:  

    * Scales, OptionBoxes, SpinBoxes, ListBoxes, RadioButtons & CheckBoxes, Entries & TextAreas, and Properties - the function will be called each time the widget is changed.  
    * Buttons, Labels & Images - it is not available.  
    * Other widgets - it will set the *command* property for the underlying tkinter widget; this may or may not do anything...  

    For `SubmitFunction`:  

    * Labels & Images - it binds a function to the ```<Left-Mouse-Button>```, making the widget clickable.  
    * Entries & Buttons - it binds a function to the ```<Return>``` key  
    * TextAreas - it's not available
    * Other widgets - it does the same as `ChangeFunction`  

**Be careful** it's possible to generate a RuntimeError. If you've got two widgets changing the same variable, say a Scale and a SpinBox, and you want a change in one widget to cause an update in the other, you might inadvertently end up stuck in a recursive loop, until the [stack overflows](https://en.wikipedia.org/wiki/Stack_overflow).  

In this case, make sure you set the optional parameter ```callFunction = False``` when you  call the ```set XXX Function()``` of a widget.  

```python
from appJar import gui

def songChanged(rb):
    print(app.getRadioButton(rb))

def reset(btn):
    # set back to the default, but don't call the change function
    app.setRadioButton("song", "Killer Queen", callFunction=False)

app=gui()
app.addRadioButton("song", "Killer Queen")
app.addRadioButton("song", "Paradise City")
app.setRadioButtonChangeFunction("song", songChanged)
app.addButton("Reset", reset)
app.go()
```

* `.set XXX OverFunction(name, [inFunction, outFunction])`  
    Set functions to call whenever the mouse enters (goes over) or leaves the specified widget.  
    **Only available on Labels**  
    The first function is called when the mouse first enters the widget.  
    The second function is called when the mouse leaves the widget.  
    If you only want a function to be called when the mouse leaves the widget, pass an array like: `[None, leave]`  

```python
    from appJar import gui

    def enter(wdgt): 
        print("IN", wdgt)
    def leave(wdgt):
        print("OUT", wdgt)

    app=gui()
    app.addLabel("l1", "Testing...")
    app.setLabelOverFunction("l1", [enter, leave])
    app.go()
```  

* `.setImageMouseOver(title, image)`  
    Additional function, specific to [images](/pythonImages/#change-images), to change the specified image, while the mouse is over it.

* `.set XXX DragFunction(name, [startDragFunction, stopDragFunction])`  
    Set functions to call whenever the mouse button is clicked and dragged.  
    **Only available on Labels**  
    The first function will be called when the mouse is initially clicked.  
    The second function will be called when the mouse is released.  
    The same rules for passing functions apply as above.  

### Registering Other Event Types  

It's possible to register any of the standard event types with appJar widgets  
```python
app.getEntryWidget("widget_name").bind("<FocusOut>", function_name, add="+")
```

##Binding Keys
As well as changing widgets, we sometimes want keys to trigger events.  
The classic example is the ```<Return>``` key, we often want to be able to hit the ```<Return>``` key to submit a form...

* `.enableEnter(function)`  
Link a function to the ```<Return>``` key

* `.disableEnter()`  
Unlink a function from the ```<Return>```  key

You may also want to bind other keys to events.  

* `.bindKey(key, function)`  
Link the specified key to the specified function.

* `.unbindKey(key)`  
Unlink the specified key from any functions bound to it.

##Repeating Events  
Sometimes, you want events to keep happening in the background.  
GUIs aren't so great at this - if you have a loop in your program, the GUI will *hang* (stop working until the loop finishes).  
Luckily, we have a solution,,,

* `.registerEvent(function)`  
This will cause the GUI to keep repeating the named function in the background.  
The function should repeat every second.  

* `.setPollTime(time)`  
If you want your events to be called more or less frequently, set the frequency here.

This is great for updating statuses, checking for messages, etc...
```python
#function to set the status bar
def getLocation():
    x,y,z = mc.player.getPos()
    app.setStatusbar("X: "+ str(round(x,3)), 0)
    app.setStatusbar("Y: "+ str(round(y,3)), 1)
    app.setStatusbar("Z: "+ str(round(z,3)), 2)

# call the getLocation function every second
app.registerEvent(getLocation)
```

##Stopping the GUI
Usually the user just presses the **close icon** to stop the GUI.  
However, you might want to let them do it in other ways - maybe by pressing a button...
To stop the GUI, simply call `app.stop()`  

If you want to add a feature to confirm the user really wants to exit, or to save some data, then you'll need a **stop function**.  

* `.setStopFunction(function)`  
    Set a function to call, before allowing the GUI to be stopped.  
    This function should return True/False to confirm if the GUI should stop.  

```python
def checkStop():
    return app.yesNoBox("Confirm Exit", "Are you sure you want to exit the application?")

app.setStopFunction(checkStop)
```
