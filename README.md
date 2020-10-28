## cGraph

This allows you to make graph for your command line tools.
It allows you to make a basic xy graph for a terminal interface instead of a GUI.

For making a coordinate graph use the object CoordinateGraph().
For plotting a point in the graph use `.plot(x,y)`.
For printing the graph use `.show()`.

Example:
```python
graph = CoordinateGraph(13, 10) # 13 width, 10 height
graph.plot(6,7) # plotting a point in (6,7)
graph.show() # printing the graph
```

### Things to keep in mind
* You **can** plot multiple points in the graph.
* You must `.setup()` the graph before showing or plotting.
* Right now this only works with integers.
* If you plot something thats out of reach of the graph borders the program will throw an error.

### TODO
* Clean up code
* Write unit tests
* add for pip installation
* Titles for graphs
* Bar graphs
* Support for decimal numbers
