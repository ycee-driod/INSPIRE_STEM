# This is a program that multiplies numbers within a table
# Date:22/02/2024
# Name:ian


def main():
    n = 10
    # Print the table
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f"{i*j:4}", end=" ")
        print()
    pass

if __name__ == "__main__"