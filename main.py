from graphics import Window, Point, Line


def main():
    win = Window(800, 600)

    p1 = Point(100,200)
    p2 = Point(100,400)
    p3 = Point(200,200)
    p4 = Point(200,400)

    l1 = Line(p1, p2)
    l2 = Line(p3, p4)
    l3 = Line(p1, p3)

    win.draw_line(l1, "black")
    win.draw_line(l2, "red")
    win.draw_line(l3, "blue")

    win.wait_for_close()

if __name__ == "__main__":
    main()
