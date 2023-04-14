# -*- coding: utf-8 -*-
from .person import Person
from .person.address import Address


def create_concatenated_string():
    ### Bad
    # # create a concatenated string from 0 to 19 (e.g. "012..1819")
    # nums = ""
    # for n in range(20):
    #     nums += str(n)   # slow and inefficient
    # return nums

    ### Better
    # # create a concatenated string from 0 to 19 (e.g. "012..1819")
    # nums = []
    # for n in range(20):
    #     nums.append(str(n))
    # return "".join(nums)  # much more efficient

    ### Best
    # create a concatenated string from 0 to 19 (e.g. "012..1819")
    nums = [str(n) for n in range(20)]
    return "".join(nums)


def main() -> None:
    person_1 = Person("John", 30, Address("street", "city", "zipcode"))
    print(person_1)


if __name__ == "__main__":
    main()
