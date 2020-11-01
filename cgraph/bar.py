class BarGraph:
  def __init__(self, lowest_num, highest_num, nums, labels, max_spaces, color=True):
    self.lowest_num = lowest_num
    self.highest_num = highest_num
    self.nums = nums
    self.max_spaces = max_spaces
    self.color = color
    self.lines = labels

    self.colors = {
      "aqua":"\x1b[7;36;46m",
      "pink":"\x1b[7;35;45m",
      "blue":"\x1b[7;34;44m",
      "yellow":"\x1b[7;33;43m",
      "green":"\x1b[7;32;42m",
      "red":"\x1b[7;31;41m",
      "reset":"\x1b[0m"
    }

    self.error_check()
    self.setup()

  def error_check(self):
    # incorrect type checking
    if type(self.lowest_num) is not int:
      print(f"cgraph error: value '{self.lowest_num}' must be type int.")
      quit()

    if type(self.highest_num) is not int:
      print(f"cgraph error: value '{self.highest_num}' must be type int.")
      quit()

    if type(self.nums) is not list:
      print(f"cgraph error: value '{self.nums}' must be type list.")
      quit()

    for num in self.nums:
      if type(num) is not int:
        print(f"cgraph error: value '{num}' must be type int.")
        quit()

    if type(self.lines) is not list:
      print(f"cgraph error: value '{self.lines}' must be type list.")
      quit()

    for label in self.lines:
      if type(label) is not str:
        print(f"cgraph error: value '{label}' must be type str.")
        quit()

    if type(self.max_spaces) is not int:
      print("cgraph error: value '{self.max_spaces}' must be type int.")
      quit()

    if type(self.color) is not bool:
      print("cgraph error: value '{self.color}' must be type bool.")
      quit()

    # more specific error checking
    if len(self.nums) != len(self.lines):
      print("cgraph error: labels list and numbers list must must be the same length.")
      quit()
    
    for num in self.nums:
      if num > self.highest_num:
        print("cgraph error: number must be equal to or less than the highest number argument.")
        quit()

      elif num < self.lowest_num:
        print("cgraph error: number must be equal to or more than the lowest number argument.")
        quit()

    if self.lowest_num > self.highest_num:
      print("cgraph error: lowest number argument cannot be larger than highest number argument.")
      quit()

    if self.max_spaces < self.highest_num:
      print("cgraph error: the maximum amount of spaces cannot be smaller than the highest number possible.")

  def setup(self):
    label_max_length = self.longest_label(self.lines)
    scpn = self.str_char_per_num(self.max_spaces, self.highest_num, self.lowest_num)

    # spaces in every line are equal
    for i in range(len(self.lines)):
      if len(self.lines[i]) < label_max_length:
        for x in range(label_max_length - len(self.lines[i])):
          self.lines[i] += " "

      if self.color:
        if self.odd(i):
          self.lines[i] += f" {self.colors['aqua']}"
        else:
          self.lines[i] += f" {self.colors['red']}"
      else:
        self.lines[i] += " "

      # how many characters to fill each line with
      # scpn is defined above
      for x in range(int(self.nums[i])):
        self.lines[i] += scpn

      # adding the final number for each line
      if self.color:
        self.lines[i] += f"{self.colors['reset']} {float(self.nums[i])}"
      else:
        self.lines[i] += f" {float(self.nums[i])}"

  def show(self):
    for line in self.lines:
      print(line)
      
  @staticmethod
  def str_char_per_num(max_spaces, highest_num, lowest_num):
    number = int(max_spaces/(highest_num - lowest_num))
    return_value = ""

    for i in range(number):
      return_value += "x"

    return return_value

  @staticmethod
  def longest_label(labels):
    slt = []
    for label in labels:
      slt.append(len(label))

    return max(slt)

  @staticmethod
  def odd(number):
    if number % 2 == 0:
      return False
    else:
      return True

if __name__ == "__main__":
    b = BarGraph(1, 7, [1, 2, 5, 7], ["Math", "English", "Spanish", "Humanities"], 50)
    b.show()
