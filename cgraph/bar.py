class BarGraph:
  def __init__(self, lowest_num, highest_num, nums, labels, max_spaces, color=True):
    self.lowest_num = lowest_num
    self.highest_num = highest_num
    self.nums = nums
    self.max_spaces = max_spaces
    self.color = color
    self.lines = labels

    self.errors = []

    for i in range(13):
      self.errors.append(False)
      
    self.error_counter = 0

    self.run = True
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
    if self.run:
        self.setup()

  def error_check(self):
    # incorrect argument type errors checking
    if type(self.lowest_num) is not int:
      print(f"cgraph error 0.1: value '{self.lowest_num}' must be type int.")
      self.errors[0] = True

    if type(self.highest_num) is not int:
      print(f"cgraph error 0.2: value '{self.highest_num}' must be type int.")
      self.errors[1] = True

    if type(self.nums) is not list:
      print(f"cgraph error 0.3: value '{self.nums}' must be type list.")
      self.errors[2] = True

    if type(self.lines) is not list:
      print(f"cgraph error 0.4: value '{self.lines}' must be type list.")
      self.errors[3] = True

    if type(self.max_spaces) is not int:
      print("cgraph error 0.5: value '{self.max_spaces}' must be type int.")
      self.errors[4] = True

    if type(self.color) is not bool:
      print("cgraph error 0.6: value '{self.color}' must be type bool.")
      self.errors[5] = True

    if self.errors[2] == False:
      for num in self.nums:
        if type(num) is not int:
          print(f"cgraph error 0.7: value '{num}' must be type int.")
          self.errors[6] = True

    if self.errors[3] == False:
      for label in self.lines:
        if type(label) is not str:
          print(f"cgraph error 0.8: value '{label}' must be type str.")
          self.errors[7] = True

    # more specific error checking
    if self.errors[2] == False and self.errors[3] == False:
      if len(self.nums) != len(self.lines):
        print("cgraph error 1.0: labels list and numbers list must must be the same length.")
        self.errors[8] = True
      
    if self.errors[2] == False and self.errors[6] == False:
      for num in self.nums:
        if self.errors[1] == False:
          if num > self.highest_num:
            print(f"cgraph error 1.1: number '{num}' must be equal to or less than the highest number argument.")
            self.errors[9] = True

        if self.errors[0] == False:
          if num < self.lowest_num:
            print(f"cgraph error 1.2: number '{num}' must be equal to or more than the lowest number argument.")
            self.errors[10] = True

    if self.errors[0] == False and self.errors[1] == False:
      if self.lowest_num > self.highest_num:
        print("cgraph error 1.3: lowest number argument cannot be larger than highest number argument.")
        self.errors[11] = True

    if self.errors[1] == False and self.errors[4] == False:
      if self.max_spaces < self.highest_num:
        print("cgraph error 1.4: the maximum amount of spaces cannot be smaller than the highest number possible.")
        self.errors[12] = True

    # counting all the errors into self.error_counter
    for boolean in self.errors:
      if boolean:
        self.error_counter += 1

    # printing the errors to the user
    if self.error_counter > 0:
      print("------------------------------------------------------------------------")
      print(f"{self.error_counter} errors generated")
      print("------------------------------------------------------------------------")
      self.run = False

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
      for x in range(self.nums[i]):
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
  nb = BarGraph(1, 7, ["this should be int", 2, 3, 5], [4832094, "Science", "Humanities", "English"], 20, "this should be boolean")
