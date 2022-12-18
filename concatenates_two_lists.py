#!/usr/bin/env python3
# Created by: Kyanh Pham
# Created on: Dec 2022
# This program concatenates two lists


def concatenates_lists(list1, list2):
    for x in list2: 
        list1.append(x)
    concatenated_list = list1
    return concatenated_list
1
def main():
    # this function gets two lists

    christmas_list1 = []
    christmas_list2 = []
    christmas_shopping_list = []

    # input
    print("Please enter 5 items kid 1 wants for Christmas: ")
    item1 = input("Item 1: ")
    christmas_list1.append(item1)
    item2 = input("Item 2: ")
    christmas_list1.append(item2)
    item3 = input("Item 3: ")
    christmas_list1.append(item3)
    item4 = input("Item 4: ")
    christmas_list1.append(item4)
    item5 = input("Item 5: ")
    christmas_list1.append(item5)

    print("Please enter 5 items kid 2 wants for Christmas: ")
    item1 = input("Item 1: ")
    christmas_list2.append(item1)
    item2 = input("Item 2: ")
    christmas_list2.append(item2)
    item3 = input("Item 3: ")
    christmas_list2.append(item3)
    item4 = input("Item 4: ")
    christmas_list2.append(item4)
    item5 = input("Item 5: ")
    christmas_list2.append(item5)

    # process and output
    # calls function
    christmas_shopping_list = concatenates_lists(christmas_list1, christmas_list2)
    print("")
    print("Here is your Christmas shopping list: ")
    print("{0}".format(christmas_shopping_list))

    print("\nDone.")


if __name__ == "__main__":
    main()
