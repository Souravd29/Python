user_input = input("Please enter a list of numbers separated by spaces: ")

try:
    user_list = [int(x) for x in user_input.split()]
    if not user_list:
        print("No numbers entered.")
    else:
        minimum = user_list[0]
        for num in user_list:
            if num < minimum:
                minimum = num
        print(minimum)
except ValueError:
    print("Please enter valid integers.")
