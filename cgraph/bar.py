class BarGraph:
  def __init__(self, lowest_num, highest_num, nums, labels, max_spaces):
    self.lowest_num = lowest_num
    self.highest_num = highest_num
    self.nums = nums
    self.labels = labels
    self.max_spaces = max_spaces

    self.lines = []

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

    max_length = self.longest_label(self.labels)

    # space and label (spaces are uneven)
    for label in self.labels:
      self.lines.append(f" {label}")

    # the length of every item in self.lines is equal
    counter = 0
    for line in self.lines:
      counter += 1
      if len(line) - 1 < max_length:
        for i in range(max_length - (len(line) - 1)):
          line += " "

      line += "  "
      self.lines[counter - 1] = line

    # spaces/characters depending on the given values
    character_per_num = int(self.max_spaces/(self.highest_num - self.lowest_num))

    for i in range(len(self.nums)):
      for x in range(self.nums[i]):
        for c in range(character_per_num):
          self.lines[i] += "x"

    for line in self.lines:
      print(line)

  @staticmethod
  def longest_label(labels):
    slt = []
    for label in labels:
      slt.append(len(label))

    return max(slt)

if __name__ == "__main__":
  b = BarGraph(1, 7, [7, 4, 5, 6], ["Math", "Science", "English", "PE"], 50)
