from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closed...")

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def draw_cell(self, cell, fill_color="black"):
        cell.draw(self.__canvas, fill_color)


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line():
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, fill=fill_color, width =2)


class Cell():
    def __init__(self, x1, y1, x2, y2):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

    def draw(self, canvas, fill_color="black"):
        if self.has_left_wall:
            canvas.create_line(self.__x1, self.__y1, self.__x1, self.__y2, fill = fill_color, width = 1)
        if self.has_right_wall:
            canvas.create_line(self.__x2, self.__y1, self.__x2, self.__y2, fill = fill_color, width = 1)
        if self.has_top_wall:
            canvas.create_line(self.__x1, self.__y1, self.__x2, self.__y1, fill = fill_color, width = 1)
        if self.has_bottom_wall:
            canvas.create_line(self.__x1, self.__y2, self.__x2, self.__y2, fill = fill_color, width = 1)

