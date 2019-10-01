#!/usr/bin/env python3

# Created by Marwan Mashaly
# Created on September 2019
# This program lets user to guess a number and see if it's correct


import constants


def main():
    # this function lets user to guess a number and see if it's correct

    # input
    guess_number = int(input("Enter a number between 0 to 9: "))
    print("")
    # process1
    if guess_number == constants.CHOSEN_NUMBER:
        # output1 
        print("correct, good guess ")
    
    # process2
    if guess_number != constants.CHOSEN_NUMBER:
        # output2
        print("wrong, better luck next time ")


if __name__ == '__main__':
    main()
