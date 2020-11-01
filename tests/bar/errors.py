from cgraph.bar import BarGraph

# incorrect type errors (0.1 - 0.8)
try:
  print("------------------------------------------------------------------------")
  print("Initializing Test 1 (BarGraph Incorrect Argument Type Handling)")
  print("------------------------------------------------------------------------")
  print("Test 1 Status: Generating Errors ...")
  print("------------------------------------------------------------------------")

  b = BarGraph(1.5, "this should be int", "this should be a list", "this should also be a list", "this should be a int")

  print("------------------------------------------------------------------------")

  b = BarGraph(1, 7, ["this should be int", 2, 3, 5], [4832094, "Science", "Humanities", "English"], 20, "this should be boolean")

  print("------------------------------------------------------------------------")

  b = BarGraph(3, 7, [1, 3, 5, 23], ["Science", "Math", "English", "Humanities", "PE"], 30)

  print("------------------------------------------------------------------------")

  b = BarGraph(7, 3, [1, 1], ["Science", "Math"], 2)

  print("------------------------------------------------------------------------")
  print("Test 1 Status: " + "\x1b[1;32;40m" + "Passed!" + "\x1b[0m")
except Exception as e:
  print("\n------------------------------------------------------------------------")
  print("Uncaught cgraph error in tests/bar/errors.py")
  print(f"Error: {e}")
  print("------------------------------------------------------------------------")
  print("Test 1 Status: " + "\x1b[1;31;40m" + "Failed!" + "\x1b[0m")
