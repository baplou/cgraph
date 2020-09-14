class Graph:
    def __init__(self):
        self.top_bar = ''
        self.y_range_list = []
        self.x_range_list = ['   ']

        self.bottom_number = ''

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
        for i in range(x_range + 1):
            self.x_range_list.append('  ' + str(i))

        for i in range(y_range + 1):
            self.y_range_list.append(str(i) + ' |' + self.getSpace() + '|')

        self.y_range_list[0] = '0 |' + self.getUnder(1) + '|'

        self.top_bar += '  ' + self.getUnder(0) + '_'

    def plot(self, x_pos, y_pos):
        '''
        This must change the self.y_range_list according to x_pos and y_pos
        This will make it possible to plot multiple points
        '''
        pass

    def show(self):
        print(self.top_bar)
        for item in reversed(self.y_range_list):
            print(item)
        for item in self.x_range_list:
            self.bottom_number += item
        print(self.bottom_number)

if __name__ == '__main__':
    g = Graph()
    g.setup(6,9)
    g.show()
