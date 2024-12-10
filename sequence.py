# Read number of test cases
t = int(input())

# Initialize a list to store the results
results = []

# Loop through each test case
for _ in range(t):
    # Read the two integers for this test case
    A = int(input())
    B = int(input())
    # Compute the product and append to results
    results.append(A * B)

# Print each result on a new line
for result in results:
    print(result)
