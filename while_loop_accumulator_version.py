#import while_loop_flag_version as wlfv
def get_starting_number():
    """
    Asks the user how many bottles of beer they would like to drink.
    :return: The number of bottles of beer the user wants to drink.
    """
    num_bottles = int(input("How many bottles of beer would you like to drink? "))
    return num_bottles

def sing(num_bottles):
    bottles_left = num_bottles
    while bottles_left > 0:
        if bottles_left == 1:
            print(f"{bottles_left} bottle of beer on the wall, {bottles_left} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
        else:
            print(f"{bottles_left} bottles of beer on the wall, {bottles_left} bottles of beer.")
            print(f"Take one down, pass it around, {bottles_left - 1} bottles of beer on the wall.")
        bottles_left -= 1
    print()
    

