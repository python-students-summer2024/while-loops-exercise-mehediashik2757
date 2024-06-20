def get_starting_number():
    while True:
        num_bottles = input("How many bottles of beer on the wall? ")
        if num_bottles.isdigit() and int(num_bottles) > 0:
            return int(num_bottles)
        else:
            print("Please enter a positive integer.")

def sing(num_bottles):
    bottles_remaining = num_bottles
    keep_singing = True

    while keep_singing:
        if bottles_remaining == 1:
            print(f"{bottles_remaining} bottle of beer on the wall, {bottles_remaining} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
            keep_singing = False
        else:
            print(f"{bottles_remaining} bottles of beer on the wall, {bottles_remaining} bottles of beer.")
            print(f"Take one down, pass it around, {bottles_remaining - 1} bottles of beer on the wall.")
            print()
            bottles_remaining -= 1
