import matplotlib.pyplot as plt
import random

from collections import defaultdict


# Number of dice rolls
num_of_rolls = 1_000_000
# Initialize a defaultdict to count occurrences of each dice sum
counts = defaultdict(int)

# Simulate dice rolls
for _ in range(num_of_rolls):
    # Generate a random number between 1 and 6 for each dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    combination = dice1 + dice2  # Calculate the sum of the two dice
    counts[combination] += 1  # Increment the count for this sum

# Calculate probabilities for each sum
probabilities = {k: count / num_of_rolls for k, count in counts.items()}
# Sort the probabilities by the sum of the dice
sorted_probabilities = {k: probabilities[k] for k in sorted(probabilities)}

print(f'| {"Sum": ^10} | {"Probability": ^11} |')
print(f'| {"-"*10} | {"-"*11} |')
# Print sorted probabilities
for key, value in sorted_probabilities.items():
    print(f"| {key: ^10} | {value*100:^11.2f} |")

# Plot the probability distribution
plt.bar(sorted_probabilities.keys(), sorted_probabilities.values())
plt.xlabel("Sum of two dice")
plt.ylabel("Probability")
plt.title("Probability distribution of the sum of two dice")

plt.show()
