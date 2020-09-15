## A xy graph for command line tools in python

This is matplotlib for command line tools. It allows you to make a basic xy graph for a terminal interface instead of a GUI.

For defining the xy borders of the graph use `.setup(x,y)`.
For plotting a point in the graph use `.plot(x,y)`.
For printing the graph use `.show()`.

You **can** plot multiple points in the graph.

You must `.setup()` the graph beafore showing or plotting.

Right now this only works with integers and single digits.

**If you plot something thats out of reach of the graph borders the program will throw an error.**
