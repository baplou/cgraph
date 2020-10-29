class BarGraph:
  def __init__(self, lowest_num, highest_num, num, labels, max_spaces):
    self.lowest_num = lowest_num
    self.highest_num = highest_num
    self.num = num
    self.labels = labels
    self.max_spaces = max_spaces

    self.lines = []

    self.setup()

  def setup(self):
    if len(self.num) != len(self.labels):
      print("cgraph error: labels list and numbers list must contain the same number of items")
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

  @staticmethod
  def longest_label(labels):
    slt = []
    for label in labels:
      slt.append(len(label))

    return max(slt)

if __name__ == "__main__":
  b = BarGraph(1, 7, [3, 4, 5, 6], ["Math", "Science", "English", "PE"], 100)
