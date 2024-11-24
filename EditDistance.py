class EditDistance:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self.m = len(str1)
        self.n = len(str2)

    def compute(self):
        # Memory optimization approach using two rows
        prev = [j for j in range(self.n + 1)]  # Previous row initialization
        curr = [0 for _ in range(self.n + 1)]   # Current row initialization

        # Iterate through each character in str1
        for i in range(1, self.m + 1):
            # Reinitialize the current row for each iteration
            curr = [0 for _ in range(self.n + 1)]
            curr[0] = i  # Base case: edit distance for empty str2

            # Iterate through each character in str2
            for j in range(1, self.n + 1):
                if self.str1[i - 1] == self.str2[j - 1]:
                    curr[j] = prev[j - 1]  # No operation needed if characters match
                else:
                    # Calculate the minimum of insert, delete, and replace operations
                    insert = 1 + curr[j - 1]   # Insertion cost
                    delete = 1 + prev[j]       # Deletion cost
                    replace = 1 + prev[j - 1]  # Replacement cost
                    curr[j] = min(insert, min(delete, replace))

            # Move to the next row
            prev = curr

        # The answer will be stored in the last element of the last row
        return curr[self.n]


def main():
    # Take input from the user for two strings
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    # Create an EditDistance object
    ed = EditDistance(str1, str2)

    # Compute the minimum edit distance
    result = ed.compute()

    # Output the result
    print(f"The minimum edit distance between '{str1}' and '{str2}' is: {result}")


if __name__ == "__main__":
    main()
