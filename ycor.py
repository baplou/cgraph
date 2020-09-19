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
        for i in range(self.x_length):
            self.space += self.placeholder

        self.return_value = ' ' + str(self.y_num) + self.medium_space + '|' + self.space + '|'

    def __repr__(self):
        return self.return_value
