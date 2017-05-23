#appJar
---
This is a Python library for creating **quick** and **easy** GUIs, designed primarily for use in the **classroom**.  

It has no dependencies, other than [Python](https://www.python.org/downloads/) (Python 3.x or 2.7) and relies on Python's built-in [tkinter](https://docs.python.org/3.5/library/tkinter.html) library.  

It's designed to be as easy to set-up as possible, specifically with schools in mind, so can just be downloaded and used.  
See the [installation guidelines](Install.md) for more information.

###Let's make a sandwich
---
Making a [GUI](https://en.wikipedia.org/wiki/Graphical_user_interface) (using appJar) is just like making a [sandwich](https://en.wikipedia.org/wiki/Sandwich)!  

You need a slice of bread on the top and bottom, and then a bunch of fillings in the middle ...

```python
# import the library
from appJar import gui

# top slice - CREATE the GUI
app = gui()

### fillings go here ###

# bottom slice - START the GUI
app.go()
```

If you forget a slice of bread - you haven't got a sandwich!  
Oh, and if you try to put fillings under the bottom-slice, then they won't be in the sandwich!

###Add some fillings...
---
When making a sandwich, you could just stuff it with fillings:  

* `addFilling('cheese', 'cheddar')`  
* `addFilling('ham', 'smoked')`  

But it's often nice to prepare the fillings too:  

* `setFilling('cheese', 'grated')` 
* `setFilling('ham', 'sliced')` 

```python
# import the library
from appJar import gui

# top slice - CREATE the GUI
app = gui()

### fillings go here ###
app.addLabel("title", "Welcome to appJar")
app.setLabelBg("title", "red")

# bottom slice - START the GUI
app.go()
```
![simpleApp](img/simpleApp.png)

And, that's it...  
The more [fillings](pythonWidgets.md) you put in your sandwich, and the more time you spend making them [look nice](pythonWidgetOptions.md), the better it will taste!

###Foot-long sub?
---
Of course, for most of us, a simple sandwich isn't enough...  
We want to make a meal out of it!  

In which case, you're going to want to arrange your fillings a bit more cleverly!

* 3 slices of cheese along the bottom  
* Alternating slices of tomato & cucumber on top  
* Then a mixture of onions and peppers  
* Finally, the sauce!  

By default, in an appJar GUI, the fillings are simply stacked on top of each other.  

However, filling a sub is very similar to filling a spreadsheet.  
Simply tell each filling what layer (row) it's on, and what column it's in.  
And, if you're not planning on chopping a filling, it might stretch (span) across more than one column.  

[See here](pythonWidgetLayout.md) for more.  

```python
from appJar import gui

# function called by pressing the buttons
def press(btn):
    if btn=="Cancel":
        app.stop()
    else:
        print("User:", app.getEntry('user'), "Pass:", app.getEntry('pass'))

app = gui()

app.addLabel("title", "Welcome to appJar", 0, 0, 2)  # Row 0,Column 0,Span 2
app.addLabel("user", "Username:", 1, 0)              # Row 1,Column 0
app.addEntry("user", 1, 1)                           # Row 1,Column 1
app.addLabel("pass", "Password:", 2, 0)              # Row 2,Column 0
app.addSecretEntry("pass", 2, 1)                     # Row 2,Column 1
app.addButtons(["Submit", "Cancel"], press, 3, 0, 2) # Row 3,Column 0,Span 2

app.setEntryFocus("user")

app.go()
```

![testLog](img/testLog.png)

###Any extras?  
---
It's possible to make changes to how the GUI looks  
For starters, you can specify a name and size for your GUI when you make it:  

* `app=gui("Login Window", "400x200")`  

And, you can choose what kind of bread, and whether it's toasted:   

* `app.setBg("Brown")`
* `app.setFont(20)`

[See here](pythonGuiOptions.md) for more.  

![testLog](img/testLog2.png)


###Make your own!
---
That's about it for now.  
Have a look around, discover all of the different [fillings](pythonWidgets.md) available.  
And, investigate how best to [present ](pythonWidgetGrouping.md) your sandwich!
