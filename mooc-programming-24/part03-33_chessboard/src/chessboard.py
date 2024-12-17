# Write your solution here
def chessboard(number):
    y = 1
    one = "1"
    zero = "0"
    while y <= number:
        string = ""
        if y % 2 != 0:
            while len(string) < number:
                string += one
                if len(string) < number:
                    string += zero
            print(string)
        else:
            while len(string) < number:
                string += zero
                if len(string) < number:
                    string += one
            print(string)
        y += 1


# Testing the function
if __name__ == "__main__":
    chessboard(6)
