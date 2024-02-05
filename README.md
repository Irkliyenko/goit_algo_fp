# Algorithms. Final Project

## Problem 2.

This task involves creating a Pythagoras tree using Python's turtle graphics library. The Pythagoras tree, a geometric fractal, is constructed recursively, resulting in an aesthetically pleasing visual pattern.

I utilized the turtle module for graphical rendering, employing command-line arguments to specify the order (recursion level) and segment size of the tree. The draw_pythagoras_tree function, which I implemented, employs recursive logic to draw the tree with branches at specific angles. The incorporation of the turtle graphics library streamlines the translation of recursive logic into a visually compelling representation. This task serves as an exemplar, showcasing recursion's sophistication and effectiveness in generating intricate patterns with concise code.

## Problem 6.

For this task, I employed two distinct algorithms: a greedy approach and a dynamic programming approach, to address the challenge of selecting food items with the maximum total caloric value within a constrained budget. I implemented two functions, greedy_algorithm and dynamic_programming, each designed to maximize the caloric value of a meal within a specified financial limit.

While executing these two functions, I observed discrepancies in the results. For example, when the budget is set to 100, the greedy algorithm spends only 80 and obtains 870 calories, while dynamic programming spends the entire 100 and achieves 970 calories. This result highlights the limitations of the greedy algorithm. The greedy algorithm selects a locally optimal result, but it does not always lead to the best global optimum. In contrast, dynamic programming calculates all possible outcomes and selects the one that provides the best global optimum.
