#function for each day
def day01():
    print("day01")
    #read txt file
    file = open('day01-input.txt','r')
    #data = file.read()
    #print(data)

    left = []
    right = []

    split = [line.strip()for line in file]
    for line in split:
        left.append(line.split("   ")[0])
        right.append(line.split("   ")[1])
    
    sorted_left = sorted(left)
    sorted_right = sorted(right)
    for (l,r) in zip(sorted_left, sorted_right):
        print(l,r)


def main():
    day01() #change function for each day


if __name__ == "__main__":
    main()
