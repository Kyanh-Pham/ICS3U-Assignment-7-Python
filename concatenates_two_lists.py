#!/usr/bin/env python3
# Created by: Kyanh Pham
# Created on: Dec 2022
# This program concatenates two lists


def concatenates_lists(list1, list2):
    for x in list2:
        list1.append(x)
    concatenated_list = list1
    return concatenated_list


def main():
    # this function gets two lists

    first_list = []
    second_list = []
    combined_lists = []

    # input
    print("Please enter 5 items to place in the list: ")
    item1 = input("Item 1: ")
    first_list.append(item1)
    item2 = input("Item 2: ")
    first_list.append(item2)
    item3 = input("Item 3: ")
    first_list.append(item3)
    item4 = input("Item 4: ")
    first_list.append(item4)
    item5 = input("Item 5: ")
    first_list.append(item5)

    print("Please enter 5 items to place in the second list: ")
    item1 = input("Item 1: ")
    second_list.append(item1)
    item2 = input("Item 2: ")
    second_list.append(item2)
    item3 = input("Item 3: ")
    second_list.append(item3)
    item4 = input("Item 4: ")
    second_list.append(item4)
    item5 = input("Item 5: ")
    second_list.append(item5)

    # process and output
    # calls function
    combined_lists = concatenates_lists(first_list, second_list)
    print("")
    print("Here is your combined list: ")
    print("{0}".format(combined_lists))

    print("\nDone.")


if __name__ == "__main__":
    main()
