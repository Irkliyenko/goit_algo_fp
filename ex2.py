import argparse
import turtle


def parse_args():
    parser = argparse.ArgumentParser(
        description="Draw Pifagoras tree with specified order")
    parser.add_argument('-o', '--order', type=int, required=True,
                        help='Specify order for Pifagoras tree')
    parser.add_argument('-s', '--size', type=int,
                        default=100, help="Specify segment's size")
    return parser.parse_args()


def draw_pifagoras_tree(size, t, order):
    if order == 0:
        return
    else:
        # Draw main branch
        t.forward(size)

        # Draw right subtree
        t.right(45)
        draw_pifagoras_tree(0.6 * size, t, order - 1)

        # Return to main branch
        t.left(90)
        draw_pifagoras_tree(0.6 * size, t, order - 1)

        # Return to main branch and move back
        t.right(45)
        t.backward(size)


def main():
    args = parse_args()

    # Setup turtle
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(1)
    t.color("green")

    # Initial position
    t.left(90)
    t.up()
    t.backward(100)
    t.down()

    # Draw the Pifagoras tree
    draw_pifagoras_tree(args.size, t, args.order)

    # Close the turtle graphics window on click
    screen.exitonclick()


if __name__ == "__main__":
    main()
