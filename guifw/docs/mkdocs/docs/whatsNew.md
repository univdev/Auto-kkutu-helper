#Change-Log
---

## Version (0.061)  
* Issues Resolved:  
    * [#154](https://github.com/jarvisteach/appJar/issues/154) - Fixed bug with AutoEntry not showing drop-down in right position, when placed in a container

## Version (0.06)  
* New widgets: [MicroBit](/pythonDevWidgets/#microbit-emulator), [Validation Entries](/pythonWidgets/#entry)  
* Widget enhancements: Can now set some rules for [entries](/pythonWidgets/#set-entries)  
* New documentation: [packaging](/packaging), [special characters](/specialCharacters), [events](/pythonEvents), [drag'n drop](/pythonDnD)  
* Work on events: [stopping event propagation](/pythonEvents/#breakdown), [drag/over events](/pythonEvents/#make-stuff-happen), [drag'n drop](/pythonDnD)  
* Issues Resolved:  
    * [#143](https://github.com/jarvisteach/appJar/issues/143) - Fixed bug with setting defaults on AutoEntries  
    * [#142](https://github.com/jarvisteach/appJar/issues/142) - Finished documentation for [popups](/pythonDialogs/#file=boxes)
    * [#130](https://github.com/jarvisteach/appJar/issues/130) - Documented how to use [special characters](/specialCharacters)  
    * [#123](https://github.com/jarvisteach/appJar/issues/123) - New features for [setting entries](/pythonWidgets/#set-entries) - max length, auto uppercase/lowercase, validation  
    * [#119](https://github.com/jarvisteach/appJar/issues/119) - [MicroBit](/pythonDevWidgets/#microbit-emulator) widget added
    * [#118](https://github.com/jarvisteach/appJar/issues/118) - dynamic library imports
    * [#117](https://github.com/jarvisteach/appJar/issues/117) - introduced documentation on [packaging](/packaging/)
    * [#116](https://github.com/jarvisteach/appJar/issues/116) - configurable trough [increments](/pythonWidgets/#set-scales) for a scale
    * [#115](https://github.com/jarvisteach/appJar/issues/115) - fixed transparency in python 2.7
    * [#114](https://github.com/jarvisteach/appJar/issues/114) - ability to stop events being propagated
    * [#112](https://github.com/jarvisteach/appJar/issues/112) - now possible to start with a subWindow (specified in go()) as well as hide() & show() main window
    * [#110](https://github.com/jarvisteach/appJar/issues/110) - can now configure the number of rows to [show](/pythonWidgets/#set-entries) in an AutoEntry  
    * [#108](https://github.com/jarvisteach/appJar/issues/108) - Fixed issue with modal [SubWindows](/pythonWidgetGrouping/#startstop-sub-windows)
    * [#106](https://github.com/jarvisteach/appJar/issues/106) - Function to add an [image button](/pythonWidgets/#add-buttons)
    * [#102](https://github.com/jarvisteach/appJar/issues/102) - Updates to drag/over [events](/pythonEvents/#make-stuff-happen)
    * [#103](https://github.com/jarvisteach/appJar/issues/103) - Can now manage event calling when [widgets change](/pythonEvents/#make-stuff-happen)
    * [#101](https://github.com/jarvisteach/appJar/issues/101) - [Drag n'Drop](/pythonDnD.md) beta support for dnd between applications
    * [#92](https://github.com/jarvisteach/appJar/issues/92) - Function to [get all entries](/pythonWidgets/#get-entries)
    * [#75](https://github.com/jarvisteach/appJar/issues/75) - Fix to [destroySubWindow](/pythonWidgetGrouping/#showhide-sub-windows)
    * [#46](https://github.com/jarvisteach/appJar/issues/46) - Added version details to about box  
    * [#42](https://github.com/jarvisteach/appJar/issues/42) - Added functionality to [change TickOptionBoxes](/pythonWidgets/#set-optionboxes)
    * [#33](https://github.com/jarvisteach/appJar/issues/33) - Added convenience function to [setTreeColours](/pythonDevWidgets/#tree)  

## Version (0.052)  
* Issues Resolved:  
    * [#114](https://github.com/jarvisteach/appJar/issues/114) - ability to stop functions being called when a set method is activated

## Version (0.051)  
* Issues Resolved:  
    * [#109](https://github.com/jarvisteach/appJar/issues/109) - Labelled Auto Entry, contributed by [jacobthetechy](https://github.com/jacobthetechy)

## Version (0.05)  
* [Open Container](/pythonWidgetGrouping/#reopening-containers) - implemented issue [#83](https://github.com/jarvisteach/appJar/issues/83), can now reopen a container, perform operations on it, and close it.  
* Changed disable entry to readonly, allows entries to be copied ([#86](https://github.com/jarvisteach/appJar/issues/86))  
* Images now support [raw image data](/pythonImages/#add-images).  
* Setters now call any registered functions  
* Rewrite of [Meters](/pythonWidgets/#meter), proper inheritance, all use gradated fill, Dual/Split Meter swapped ([#65](https://github.com/jarvisteach/appJar/issues/65)).  
* Rewrite of [ScrollPane](/pythonWidgetGrouping/#scroll-pane), multi-platform scrolling...
* Added functions to [change the bg/fg](/pythonWidgets/#listbox) of ListBox items ([#97](https://github.com/jarvisteach/appJar/issues/97)).  
* Issues Resolved:  
    * [#101](https://github.com/jarvisteach/appJar/issues/101) & [#103](https://github.com/jarvisteach/appJar/issues/103) - updates to documentation
    * [#99](https://github.com/jarvisteach/appJar/issues/99) - ability to create empty containers  
    * [#97](https://github.com/jarvisteach/appJar/issues/97) - ability to set bg/fg colour of list items
    * [#94](https://github.com/jarvisteach/appJar/issues/94) - basic support for [MatPlotLib](/pythonDevWidgets/#matplotlib)  
    * [#90](https://github.com/jarvisteach/appJar/issues/90) - raw image data  
    * [#89](https://github.com/jarvisteach/appJar/issues/89) - minimum speed for animated image  
    * [#88](https://github.com/jarvisteach/appJar/issues/88) - preload mouse over images  
    * [#86](https://github.com/jarvisteach/appJar/issues/86) - disabled entry now readonly  
    * [#85](https://github.com/jarvisteach/appJar/issues/85) - setters now call function (if available)  
    * [#83](https://github.com/jarvisteach/appJar/issues/83) - can now reopen container  
    * [#65](https://github.com/jarvisteach/appJar/issues/65) - Meter rewrite  
    * [#34](https://github.com/jarvisteach/appJar/issues/34)/[#35](https://github.com/jarvisteach/appJar/issues/35) - ScrollPane rewrite

## Version 0.042  
* Issues Resolved:  
    * [#95](https://github.com/jarvisteach/appJar/issues/95) - fixed issue launching ShowCase under Python 2 (removed icons)  
    * [#93](https://github.com/jarvisteach/appJar/issues/93) - fixed issue with numDialog/textDialog under python 2  

## Version 0.041  
* Continuous Integration - added [landscape.io](https://landscape.io/github/jarvisteach/appJar/) to monitor code quality  
* [Reload Image](/pythonImages/#change-images) - function to force a reload of an image, bypassing the cache (issue [#87](https://github.com/jarvisteach/appJar/issues/87))  
* Minor fixes based off landscape report  
* Issues Resolved:  
    * [#87](https://github.com/jarvisteach/appJar/issues/87) - reloadImage()  
    * [#84](https://github.com/jarvisteach/appJar/issues/84) - Removed requirement for appJar icon in Windows  

## Version 0.04  
* [Internationalisation](/pythonInternationalisation) - it's now possible to support multiple languages, by adding simple config files.  
* [Splashscreen](/splash) - a simple splashscreen is now available.  
* [AutoCompletion EntryBox](/pythonWidgets/#entry) - added a new widget, giving autocompletion in EntryBoxes  
* [Function on change](/pythonEvents/#make-stuff-happen) in ListBox - now possible to call a function each time a ListBox changes  
* [Python 3.6 Support](https://docs.python.org/3.6/whatsnew/3.6.html#idlelib-and-idle) - now supports python3.6 - fixed issue with renamed idelib files  
* Continuous Integration - now uses [Travis-CI](https://travis-ci.org/jarvisteach/appJar) and [Coveralls](https://coveralls.io/github/jarvisteach/appJar) to check for errors on each commit  
* Updated documentation: Rearrangement of navigation bar, new pages for new features, minor modifications.  
* Issues Resolved:  
    * [#81](https://github.com/jarvisteach/appJar/issues/81) - now allows negative numbers/decimals to be entered correctly in NumericEntries  
    * [#80](https://github.com/jarvisteach/appJar/issues/80) - now support Python 3.6  
    * [#78](https://github.com/jarvisteach/appJar/issues/78) - fixed typo in documentation  
    * [#74](https://github.com/jarvisteach/appJar/issues/74) - SplashScreen  
    * [#72](https://github.com/jarvisteach/appJar/issues/72) - Unit testing  
    * [#71](https://github.com/jarvisteach/appJar/issues/71) - Internationalisation  
    * [#70](https://github.com/jarvisteach/appJar/issues/70) - AutoComplete EntryBox  
