# Alphaess API project

TUI project for my solar stuff

### Terminology
1. SN: The serial number of the inverter or the battery system.


## Project setup
1. Use command uv sync to install all dependencies
2. To run the program, use command `uv run textual run --dev <file_name>.py`


### Textual tutorial
Textual has many commands that can be used to create TUI applications. Here are some useful links to get started:
1. textual serve static_and_label_tcss.py -> this will run the textual app and serve it on a local web server
2. To enable hot reloading, it is possible to use watchfiles. A command like this might work:
    `uv run watchfiles "textual run --dev docker_widget.py" .`


## Styles tutorial

1. Width and height
    we can set the width and height but it restricts the number of
    columns and rows that can be used in the layout.
    Main disadvantage is if the terminal window is resized, the 
    layout will not adapt to the new size.
2. Auto dimensions
    In practice, we would like the size of the widget to adapt
    to its content. This is done by setting 'auto'.
3. units
    they allow you to specify dimensions relative to the screen or
    container. it keeps those percentage propportions even when
    the user resizes the terminal window.
4. FR units
   FR units are an improvement over percents as sometimes it gets hard to show 33.333% (usually when
   dividing a space into equal parts).

### Padding
Padding adds space around your content which helps with readability.

Setting padding like this `self.widget.styles.padding = (2, 4)` will set 2 rows to the top & bottom and 4 columns to the left and 
right of the widget. This can be set with 4 values as well.

### Border
The border style draws a border around your widget. 
There are many different border syles and they can be access by `uv run textual borders`.

