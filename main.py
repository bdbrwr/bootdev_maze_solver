from graphics import Window, Point, Line, Cell


def main():
    win = Window(800, 600)

    c1 = Cell(200,200,400,400)
    c1.has_bottom_wall = False
    c2 = Cell(100,100,150,150)
    c3 = Cell(500,500,600,700)
    c3.has_top_wall = False

    win.draw_cell(c1)
    win.draw_cell(c2)
    win.draw_cell(c3)

    win.wait_for_close()

if __name__ == "__main__":
    main()
