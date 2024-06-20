def get_starting_number():
    while True:
        try:
            num_bottles = int(input("How many bottles of beer on the wall? "))
            if num_bottles > 0:
                return num_bottles
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def sing(num_bottles):
    for i in range(num_bottles, 0, -1):
        if i == 1:
            print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
        else:
            print(f"{i} bottles")
