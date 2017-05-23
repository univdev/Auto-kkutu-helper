#Images
____
![ImageDemo](img/imageDemo.png)  

Default image support in appJar assumes no extra libraries. That means it should only support `.GIF` and `.PPM` images.  
However, code is included to allow the use of `.PNG` and `.JPG` files. appJar will convert these to `.GIF` files, before loading.  
Converting image files is **SLOW**, so it's best to stick to `.GIF` files!  

Getting the path for images right can be **TRICKY**  
It's therefore best to put images in the same folder as your Python code.  
Or, create an image folder and set it using the `.setImageLocation(location)` function.  

###Add Images

* `.addImage(title, file)`  
    Adding an image is exactly the same as adding any other widget.  
    Simply give the image a title, and pass the filename.  
    appJar will confirm the file is valid, and will also check the file contains the type specified.  
    If an animated `.GIF` is found, then it will be animated within the GUI.  

```python
app.startLabelFrame("Simple", 0, 0)
app.addImage("simple", "balloons.gif")
app.stopLabelFrame()
```

* `.addImageData(title, imgData)`  
    As above, but receives raw image data.  
    Currently only supports base64 encoded GIF images.  

* `.setImageLocation(location)`  
    Set a folder for image files.  
    This will be put before the names of any image files used.  

###Change Images

* `.setImage(title, image)` & `.setImageData(title, imgData)`  
    This will replace the existing image with the new one.  
    If the image has the same path, it will not be changed.  
    If imgData, will always be reloaded.  

* `.reloadImage(title, image)` & `.reloadImageData(title, imgData)`  
    This will replace the existing image with the new one.  
    It will force an image reload, even if the file name hasn't changed.  
    Useful if an outside agency modifies the image file.  

```python
def changePic(btn):
    if btn == "Reload":
        app.reloadImage("reload", "balloons.gif")

app.startLabelFrame("Reload", 1, 1)
app.setSticky("ew")
app.addImage("reload", "balloons.gif")
app.addButton("Reload", changePic)
app.stopLabelFrame()
```

* `.setImageSubmitFunction(title, function)`  
    This will set a function to call when the image is clicked.  

```python
clicked = False
def changePic(btn):
    if btn == "clickme":
        global clicked
        if clicked: app.setImage("clickme", "balloons.gif")
        else: app.setImage("clickme", "balloons2.png")
        clicked = not clicked

app.startLabelFrame("Click Me", 0, 2)
app.addImage("clickme", "balloons.gif")
app.setImageSubmitFunction("clickme", changePic)
app.stopLabelFrame()
```

* `.setImageMouseOver(title, image)`  
    Set an image to show, instead of the stored image, while the mouse is over this widget.  

```python
app.startLabelFrame("Mouse Over", 0, 1)
app.addImage("mo_1", "balloons.gif")
app.setImageMouseOver("mo_1", "balloons2.png")
app.stopLabelFrame()
```

* `.setImageSize(title, width, height)`  
    This will set the size of the container for the image, cropping anything that doesn't fit.  

* `.zoomImage(title, mod)`  
    This will attempt to change the size of the image.  
    It's very rudimentary, and usually doesn't look good - but is fun to play around with (try adding a slider under an image...)  
    Negative values will shrink the image, positive will enlarge the image.  

```python
def changePic(btn):
    if btn == "Zoom":
        app.zoomImage("Zoom", int(app.getSpinBox("Zoom")))
```


* `.shrinkImage(title, mod)` & `.growImage(title, mod)`  
    These are wrappers for the above function, simply causing the image to shrink or grow accordingly.

###Change Image Animation
If an image is animated, it's possible to control it.

* `.setAnimationSpeed(title, speed)`  
    This will change the speed an image is animated at.

* `.stopAnimation(title)` & `.startAnimation(title)`  
    These will start and stop the animation of an image.

```python
def changePic(btn):
    if btn == "Stop":
        global animated
        if animated:
            app.stopAnimation("animated")
            app.setButton("Stop", "Start")
        else:
            app.startAnimation("animated")
            app.setButton("Stop", "Stop")
        animated = not animated

app.startLabelFrame("Animated", 1, 2)
app.setSticky("ew")
app.addImage("animated", "animated_balloons.gif")
app.addButton("Stop", changePic)
app.stopLabelFrame()
```

###Set Background Images
It's also possible to add a background image to your GUI.  
If you have lots of grouped widgets, this can look quite **UGLY**, as all of the widgets are drawn on top.  

* `.setBgImage(image)`  
    Set the image for the background.

* `.removeBgImage(image)`  
    Remove the image form the background.

###Image Caching
appJar employs an image caching mechanism, to speed up image processing.  
Every time an image is loaded, it's added to the cache.  
The next time an image of the same filename is referenced, it will be loaded from the cache.  
This speeds up processes such as mouse-overs, or setting images back-and-forth.  

Animatd images also have their own internal cache, storing each version of the image.  

appJar attempts to preload mouse over images and animated images, to improve smoothness.  

If there's ever a need to clear the image cache (maybe reduce memory footprint), call: `.clearImageCache()`  
