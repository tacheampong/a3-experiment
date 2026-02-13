import random

class UniqueRandomGenerator:
    def __init__(self, low, high):
        # Create a list of all numbers in the range (inclusive)
        self.pool = list(range(low, high + 1))
        # Shuffle the list once at the start
        random.shuffle(self.pool)

    def get_next(self):
        if not self.pool:
            return "No numbers left in the range!"
        # Remove and return the last number from the shuffled list
        return self.pool.pop()

# --- Usage ---
# Initialize with your specific range: 2 to 1658
# 2 is the first row with game data and 1658 being the last. Row 1 is the title row so I disregarded it.
rng = UniqueRandomGenerator(2, 1658)

# Get x unique numbers
for _ in range(21):
    print(rng.get_next())