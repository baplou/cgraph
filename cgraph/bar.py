class BarGraph:
  def __init__(self, lowest_num, highest_num, nums, labels, max_spaces, color=True):
    self.lowest_num = lowest_num
    self.highest_num = highest_num
    self.nums = nums
    self.labels = labels
    self.max_spaces = max_spaces
    self.color = color

    self.lines = []
    self.colors = {
      "aqua":"\x1b[7;36;46m",
      "pink":"\x1b[7;35;45m",
      "blue":"\x1b[7;34;44m",
      "yellow":"\x1b[7;33;43m",
      "green":"\x1b[7;32;42m",
      "red":"\x1b[7;31;41m",
      "reset":"\x1b[0m"
    }

    self.setup()

  def setup(self):
    # error checking
    if len(self.nums) != len(self.labels):
      print("cgraph error: labels list and numbers list must contain the same number of items")
      quit()
    
    for num in self.nums:
      if num > self.highest_num:
        print("cgraph error: number has to be equal to or less than the highest number argument")
        quit()

      elif num < self.lowest_num:
        print("cgraph error: number has to be equal to or more than the lowest number argument")
        quit()

    label_max_length = self.longest_label(self.labels)

    # adding the label to every line in self.lines
    for label in self.labels:
      self.lines.append(f"{label}")

    # the length of every item in self.lines is equal
    for i in range(len(self.lines)):
      if len(self.lines[i]) < label_max_length:
        for x in range(label_max_length - (len(self.lines[i]))):
          self.lines[i] += " "

      if self.color:
        if self.odd(i):
          self.lines[i] += f" {self.colors['aqua']}"
        else:
          self.lines[i] += f" {self.colors['red']}"
      else:
        self.lines[i] += " "

    # how many characters to fill each line with
    # scpn = string x character per num
    scpn = self.str_char_per_num(self.max_spaces, self.highest_num, self.lowest_num)

    for i in range(len(self.lines)):
      for x in range(self.nums[i]):
        self.lines[i] += scpn

    # adding the final number for each line
    for i in range(len(self.lines)):
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
