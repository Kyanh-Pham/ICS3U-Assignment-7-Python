#!/usr/bin/env python3
# Created by: Kyanh Pham
# Created on: Dec 2022
# This program concatenates two lists


def concatenates_lists(list1, list2):
    for item_in_list in list2:
        list1.append(item_in_list)
    concatenated_list = list1
    return concatenated_list


def main():
    # this function gets two lists

    first_list = []
    second_list = []
    combined_lists = []

    # input
    print("Please enter 5 items to place in the list: ")
    for counter in range(1, 6):
        item = input("Item {0}: ".format(counter))
        first_list.append(item)

    print("Please enter 5 items to place in the second list: ")
    for counter in range(1, 6):
        item = input("Item {0}: ".format(counter))
        second_list.append(item)

    # process and output
    # calls function
    combined_lists = concatenates_lists(first_list, second_list)
    print("")
    print("Here is your combined list: ")
    print("{0}".format(combined_lists))

    print("\nDone.")


if __name__ == "__main__":
    main()
