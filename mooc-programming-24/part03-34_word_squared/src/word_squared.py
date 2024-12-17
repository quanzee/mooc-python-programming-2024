# Write your solution here
def squared(sentence, size):
    y = 0
    i = 0
    while y < size: 
        string = ""
        while len(string) < size: 
            string += sentence[i]
            i += 1 
            if i == len(sentence): 
                i = 0
        print(string)
        y += 1

        

# Testing the function
if __name__ == "__main__":
    squared("aybabtu", 5)
        