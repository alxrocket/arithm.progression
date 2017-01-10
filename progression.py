#!/usr/bin/python

# -*- coding: utf-8 -*-
"""
This program checks whether the numerical sequence arithmetic or geometric progression.

Example:
        $ ./progression.py --num="1 2 3 4 5 6 7"
"""
import sys
import getopt

"""
Constants for show user results of running program
"""
MSG_HELP = 'This program checks whether the numerical sequence arithmetic or geometric progression.\n' \
+'Usage: progression.py --num="1 2.5 3.5 4 5 6 7 8 9"'
MSG_BAD_OPTIONS = 'Unhandled options. Try progression.py --help'
MSG_BAD_INPUT = 'Unhandled params of option --num. Please, try progression.py --help'
MSG_SMALL_PARAM_AMOUNT = 'To check if it progression or not you need at least 3 numbers'

MSG_PROGRESSION_SUCCESS = 'Yes, this is a progression'
MSG_PROGRESSION_FAILURE = 'No, it is not a progression'

def main(argv):
    """
    Main function. Like a C, bro
    Args:
        argv (list): command-line params, except program name.
    """
    try:
        opts, args = getopt.getopt(argv, "h", ["help", "num="])
    except getopt.GetoptError as error:
        print error
        sys.exit()
    if len(opts) == 0:
        print MSG_BAD_OPTIONS
        sys.exit()
    user_input = None
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print MSG_HELP
            sys.exit()
        elif opt == "--num":
            user_input = arg
        else:
            print MSG_BAD_OPTIONS
            sys.exit()

    nums = check_user_input(user_input)
    if nums is False:
        print MSG_BAD_INPUT
        sys.exit()
    else:
        res_len = len(nums)
        if res_len < 3:
            print MSG_SMALL_PARAM_AMOUNT
            sys.exit()
        else:
            result = is_progression(nums)
            if result:
                print MSG_PROGRESSION_SUCCESS
            else:
                print MSG_PROGRESSION_FAILURE
            sys.exit()

def check_user_input(user_input):
    """
    Checks if user data correct or not
    Args:
        user_input (string): user data from input
    Returns:
        mixed: False if user data is incorrect
                  List with floats if data is correct
    """
    is_correct_data = True
    params = user_input.split()
    prepared_params = []
    if len(params) > 0:
        for num in params:
            try:
                prepared_params.append(float(num))
            except ValueError:
                is_correct_data = False
                break
    else:
        is_correct_data = False

    if is_correct_data:
        return prepared_params
    else:
        return is_correct_data

def is_progression(numbers_list):
    """
    Checks if list of numbers is a ariphmetical/geometric progression
    Args:
        numbers_list (list): list of numbers
    Returns:
        bool: False if numbers is NOT a ariphmetical/geometric progression
              True if numbers is a progression
    """
    first_num = numbers_list[0]
    second_num = numbers_list[1]
    third_num = numbers_list[2]
    ariph_step = second_num - first_num
    geom_step = second_num / first_num
    is_ariph_prog = False
    is_geom_prog = False

    if third_num == (first_num + 2 * ariph_step):
        is_ariph_prog = True
    elif third_num == (first_num * pow(geom_step, 2)):
        is_geom_prog = True

    list_start_ind = 3
    for num in numbers_list[list_start_ind::]:
        if is_ariph_prog:
            if num != (first_num + list_start_ind * ariph_step):
                is_ariph_prog = False
                break
        elif is_geom_prog:
            if num != (first_num * pow(geom_step, list_start_ind)):
                is_geom_prog = False
                break
        list_start_ind += 1

    result = False
    if is_ariph_prog or is_geom_prog:
        result = True
    return result

if __name__ == "__main__":
    main(sys.argv[1:])
