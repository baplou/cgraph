class Ycor:
  def __init__(self, x_length, y_num, medium_space):
    self.x_length = x_length
    self.y_num = y_num
    self.medium_space = medium_space

    self.space = ''
    self.return_value = ''
    self.placeholder = ' '

    self.config()

  def config(self):
    if self.y_num == 0:
      self.placeholder = '_'

    self.x_length *= 3
    self.x_length += 1 

    for i in range(self.x_length):
      self.space += self.placeholder

    self.return_value = ' ' + str(self.y_num) + self.medium_space + '|' + self.space + '|'

class CoordinateGraph:
  def __init__(self, x, y):
    self.top_bar = ''
    self.bottom_numberline = ''
    self.y_range_list = []
    self.x_range_list = []

    self.medium_space = ''
    self.max_length = 0

    self.x_space = '  '
    self.top_bar_counter = 0
    self.setup(x, y)

  def set_medium(self, number):
    self.max_length = number

    for i in range(len(str(number))):
      self.medium_space += ' '

  def change_medium(self, number):
    self.medium_space = ''
    counter = len(str(self.max_length)) - len(str(number)) + 1

    for i in range(counter):
      self.medium_space += ' '

  def setup(self, x_range, y_range):
    self.set_medium(y_range)

    for i in range(len(str(self.max_length)) + 1):
      self.x_range_list.append(' ')

    for i in range(x_range + 1):
      self.x_range_list.append(self.x_space + str(i))

    for i in range(y_range + 1):
      self.change_medium(i)
      y = Ycor(x_range, i, self.medium_space)
      self.y_range_list.append(y.return_value)
      self.set_medium(y_range)

    for i in range(len(self.y_range_list)):
      line = self.y_range_list[i]
      replacement = ''
      for x in range(len(line) - 1):
        replacement += line[x]
      for y in range(x_range):
        for z in range(len(str(y)) - 1):
          if i == 0:
            replacement += '_'
          else:
            replacement += ' '

      replacement += line[-1]
      self.y_range_list[i] = replacement

    for i in range(len(str(self.max_length)) + 2):
      self.top_bar += ' '

    difference = len(str(self.max_length)) + 4
    for i in range(len(self.y_range_list[0]) - difference):
      self.top_bar_counter += 1

    for i in range(self.top_bar_counter + 2):
      self.top_bar += '_'

  def plot(self, x_pos, y_pos):
    line = self.y_range_list[y_pos]
    plot_counter = x_pos * 3
    replacement = ''

    for y in range(x_pos):
      for i in range(len(str(y)) - 1):
        plot_counter += 1

    plot_counter += 6 - 1
    for i in range(plot_counter):
      replacement += line[i]

    replacement += 'X'
    for i in range(len(line) - len(replacement) - 1):
      replacement += ' '

    replacement += '|'
    self.y_range_list[y_pos] = replacement
  
  def show(self):
    print(self.top_bar)

    for i in reversed(self.y_range_list):
      print(i)

    for i in self.x_range_list:
      self.bottom_numberline += i

    print(self.bottom_numberline)

if __name__ == "__main__":
  g = CoordinateGraph(13,13)
  g.plot(9,9)
  g.show()
