class Graph:
    def __init__(self):
        self.top_bar = ''
        self.y_range_list = []
        self.x_range_list = ['   ']
        self.bottom_numberline = ''

    def getUnder(self, modifier):
        get_under_counter = 0
        get_under_return = ''

        for i in self.x_range_list:
            get_under_counter += 1

        get_under_counter *= 3
        get_under_counter -= 1

        for i in range(get_under_counter - modifier):
            get_under_return += '_'

        return get_under_return

    def getSpace(self):
        get_space_counter = 0
        get_space_return = ''
        
        for i in self.x_range_list:
            get_space_counter += 1

        get_space_counter *= 3 
        get_space_counter -= 2

        for i in range(get_space_counter):
            get_space_return += ' '

        return get_space_return

    def setup(self, x_range, y_range):
        '''
        Have a function that returns how mnay spaces should be added
        depending on the len(x_range) and len(y_range)
        This should make it work with any integer
        '''
        for i in range(x_range + 1):
            self.x_range_list.append('  ' + str(i))

        for i in range(y_range + 1):
            self.y_range_list.append(str(i) + ' |' + self.getSpace() + '|')

        self.y_range_list[0] = '0 |' + self.getUnder(1) + '|'

        self.top_bar += '  ' + self.getUnder(0) + '_'

    def plot(self, x_pos, y_pos):
        '''
        Have a function that returns how mnay spaces should be added
        depending on the len(x_range) and len(y_range)
        This should make it work with any integer
        '''
        list_item = self.y_range_list[y_pos]
        replace_line = ''
        plot_counter = 0
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
