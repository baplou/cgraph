## cgraph
This allows you to make graphs for your command line tools.

### X Y Graph
Makes it possible for you to make a basic xy graph for a terminal interface instead of a GUI.

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

### Bar Graph
The "BarGraph" object takes in 5 arguments; the lowest number possible in your data,
the highest number possible in your data, a list of all the numbers (your data), a
list of all your labels for each number, the number of spaces that are used for the 
maximum number/value in your data, and (this is a optional parameter) a boolean 
representing if you want colored output or not.

Source code for initializing the object:
```python
class BarGraph:
  def __init__(self, lowest_num, highest_num, nums, labels, max_spaces, color=True):
```

### Color

The colored output is done using [ASCII escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code).

An example using school grades (A = 6, B = 5, and so on). There are no + or - in the grades as to
not make this example too complicated.

#### With Color
```python
b = BarGraph(1, 6, [6, 4, 5, 6], ["Math", "Science", "English", "PE"], 50) # making the graph
b.show() # printing the graph
```

Output:
![](https://github.com/baplou/cgraph/blob/master/images/example-color.png?raw=true)


#### Without color
```python
b = BarGraph(1, 6, [6, 4, 5, 6], ["Math", "Science", "English", "PE"], 50, False) # making the graph
b.show() # printing the graph
```

Output:
![](https://github.com/baplou/cgraph/blob/master/images/example-nocolor.png?raw=true)

### TODO
* Write unit tests
* Add pip installation
* Support for decimal numbers
