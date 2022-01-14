#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Jan. 10, 2022
# This program allows a user to enter two integers in order
# to compute sine, cosine and tangent for a given number
# while the other number determines the
# number of repititons of the taylor series

import math
import time


def main():

    def sinx():
        # Function that calculates and displays sine
        sin_x = 0
        count_num = user_count_num_int
        for counter in range(count_num):
            fact_sin = math.factorial(2 * counter + 1)
            sin_x += (-1)**counter * user_num_int**(2 * counter + 1) / fact_sin

        print(" ")
        print("The sine of " +
              "{} is approximately {}.".format(user_num_int, sin_x))

    def cosx():
        # Function that calculates and displays cosine
        cos_x = 0
        count_num = user_count_num_int
        for counter in range(count_num):
            fact_cos = math.factorial(2 * counter)
            cos_x += (-1)**counter * user_num_int**(2 * counter) / fact_cos

        print(" ")
        print("The cosine of " +
              "{} is approximately {}.".format(user_num_int, cos_x))

    def tanx():
        # Function that calculates and displays tangent by calculating both
        # sine and cosine first
        cos_x = 0
        sin_x = 0
        tan_x = 0
        count_num = user_count_num_int
        for counter in range(count_num):
            fact_cos = math.factorial(2 * counter)
            cos_x += (-1)**counter * user_num_int**(2 * counter) / fact_cos
            fact_sin = math.factorial(2 * counter + 1)
            sin_x += (-1)**counter * user_num_int**(2 * counter + 1) / fact_sin
            tan_x = sin_x / cos_x

        print(" ")
        print("The tangent of " +
              "{} is approximately {}.".format(user_num_int, tan_x))

    def decision():
        # Loop that allows the user to decide which
        # calculation they want to perform
        while True:
            user_ans = input("Would you like to calculate sine, cosine " +
                             "or tangent? sine/cosine/tangent: ")

            if user_ans == "sine" or user_ans == "Sine":
                # Calls sine function and breaks loop
                sinx()
                break
            elif user_ans == "cosine" or user_ans == "Cosine":
                # Calls cosine function and breaks loop
                cosx()
                break
            elif user_ans == "tangent" or user_ans == "Tangent":
                # Calls tangent function and breaks loop
                tanx()
                break
            else:
                # Invalid input message
                print("Enter either 'sine', 'cosine' or 'tangent.")

    # Print introduction message to user
    print("Welcome! This program can calculate the approximate values " +
          "of the sine, cosine and tangent of a given number 25 or less.")
    time.sleep(1.5)

    # Loop that gets and checks user input
    while True:

        print(" ")
        user_num = input("Enter the number that you'd like " +
                         "to calculate with: ")

        try:
            # Make sure user input is an integer
            user_num_int = int(user_num)

            # Makes sure that user number is below 26 and above -26
            if user_num_int < 26 and user_num_int > -26:
                # Loop that asks the user for the number of times
                # that they want the series to loop
                while True:

                    print(" ")
                    print("It is recommended that you loop at least " +
                          "25 times to get accurate results.")
                    time.sleep(0.5)

                    # Make sure that user input is above 0 and an integer
                    user_count_num = input("Please enter the number of " +
                                           "times that you would like to" +
                                           " loop: ")
                    try:
                        user_count_num_int = int(user_count_num)

                        if user_count_num_int > 0:

                            # Call decision function and break loop
                            time.sleep(1)
                            print(" ")
                            decision()
                            break

                        else:
                            print("You must enter a number above 0.")

                    except Exception:
                        print("'{}' is not a number".format(user_count_num))
                break

            elif user_num_int < -25:
                print("{} is too small, please enter".format(user_num_int) +
                      " a number that is -25 or above.")
            else:
                print("{} is too big, please enter a".format(user_num_int) +
                      " number 25 or under.")

        except Exception:
            # Prevent crash by displaying error message if user
            # input is not an integer
            print("'{}' is not a number".format(user_num))


if __name__ == "__main__":
    main()
