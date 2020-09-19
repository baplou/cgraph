from ycor import Ycor

class Graph:
    def __init__(self):
        self.top_bar = ''
        self.bottom_numberline = ''

        self.y_range_list = []
        self.x_range_list = []

        self.medium_space = ''
        self.max_length = None

        self.x_space = '  '

    def setMedium(self, number):
        self.max_length = number
        for i in range(len(str(number))):
            self.medium_space += ' '

    def changeMedium(self, number):
        self.medium_space = ''
        counter = len(str(self.max_length)) - len(str(number)) + 1

        for i in range(counter):
            self.medium_space += ' '

    def setup(self, x_range, y_range):
        self.setMedium(y_range)

        for i in range(len(str(self.max_length)) + 3):
            self.x_range_list.append(' ')

        for i in range(x_range):
            self.x_range_list.append(self.x_space + str(i))

        for i in range(y_range + 1):
            self.changeMedium(i)
            y = Ycor(x_range, i, self.medium_space)
            self.y_range_list.append(y.return_value)
            self.setMedium(y_range)

        '''
        Loop through y_range_list and add a space
        based on the length of self.max_length
        '''

    def plot(self, x_pos, y_pos):
        list_item = self.y_range_list[y_pos]
        replace_line = ''
        plot_counter = x_pos * 3 + 6 - 1

        for i in range(plot_counter):
            replace_line += list_item[i]

        replace_line += 'X'

        while True:
            if plot_counter >= len(list_item) - 2:
                break
            else:
                plot_counter += 1
                replace_line += list_item[plot_counter]

        replace_line += '|'

        self.y_range_list[y_pos] = replace_line
    
    def show(self):
        print(self.top_bar)

        for item in reversed(self.y_range_list):
            print(item)

        for item in self.x_range_list:
            self.bottom_numberline += item

        print(self.bottom_numberline)
