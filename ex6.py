def greedy_algorithm(dict_items, budget):
    """
    Greedy algorithm to maximize caloric value within a budget.
    Items are chosen based on the best caloric value to cost ratio.
    """

    if budget < 0:
        raise ValueError("Budget cannot be negative.")

    # Sort items by calories/cost ratio in descending order
    sorted_items = sorted(
        dict_items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

    total_caloric_value = 0
    bought_items = []  # List to store names of bought items
    spending = 0

    for key, item in sorted_items:
        # Check if the item can be bought within the budget
        if budget >= item["cost"]:
            budget -= item["cost"]
            total_caloric_value += item['calories']
            bought_items.append(key)
            spending += item["cost"]
        else:
            break  # Stop the loop when the budget is exhausted

    return total_caloric_value, bought_items, spending


def dynamic_programming(items, budget):
    """
    Dynamic programming approach to maximize caloric value within a budget.
    Considers all possible combinations to find the optimal solution.
    """

    if budget < 0:
        raise ValueError("Budget cannot be negative.")

    num_items = len(items)

    # Initialize a table to store optimal values for subproblems
    dp_table = [[0] * (budget + 1) for _ in range(num_items + 1)]

    for i in range(1, num_items + 1):
        for j in range(budget + 1):
            current_item = items[list(items.keys())[i - 1]]
            if current_item["cost"] <= j:
                dp_table[i][j] = max(dp_table[i - 1][j],
                                     dp_table[i - 1][j - current_item["cost"]] + current_item["calories"])
            else:
                dp_table[i][j] = dp_table[i - 1][j]

    total_caloric_value = dp_table[num_items][budget]
    selected_items = []  # List to store names of selected items
    spending = 0

    i, j = num_items, budget
    while i > 0 and j > 0:
        current_item = items[list(items.keys())[i - 1]]
        if dp_table[i][j] != dp_table[i - 1][j]:
            selected_items.append(list(items.keys())[i - 1])
            j -= current_item["cost"]
            spending += current_item["cost"]
        i -= 1

    return total_caloric_value, selected_items, spending


if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    budget = 130

    # Greedy algorithm
    total_caloric_value_greedy, bought_items_greedy, spending_greedy = greedy_algorithm(
        items, budget)
    print(f'Greedy algorithm:')
    print(
        f"Total caloric value: {total_caloric_value_greedy}, bought items: {bought_items_greedy}, spent: {spending_greedy}")
    print("\n-----------------------\n")

    # Dynamic programming
    total_caloric_value_dyn, bought_items_dyn, spending_dyn = dynamic_programming(
        items, budget)
    print(f'Dynamic programming:')
    print(
        f"Total caloric value: {total_caloric_value_dyn}, bought items: {bought_items_dyn}, spent: {spending_dyn}")
