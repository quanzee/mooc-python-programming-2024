# Copy here code of line function from previous exercise
def line(number, text):
    if text == "":
        print("*"*number)
    else:
        print(text[0] * number)

def triangle(size):
    height = 0
    width = 0a
    # You should call function line here with proper parameters
    line(4, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
