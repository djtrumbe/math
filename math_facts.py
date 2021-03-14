#!/usr/local/opt/python/libexec/bin/python

import argparse
import datetime
import importlib
import os
import random


def present_problem(problem_text, answer):
    guess = input(" " + problem_text)
    try:
        guess = int(guess)
    except:
        pass
    if guess == answer:
        print("     👍\n")
        return 1
    else:
        print("    the correct answer is: {}\n".format(answer))
        return 0


def addition(config):
    answer = random.randint(config.number_set_min, config.max_problem)
    addend1 = random.randint(config.number_set_min, min(config.number_set_max, answer))
    addend2 = answer - addend1
    return present_problem("{} + {} = ".format(addend1, addend2), answer)


def subtraction(config):
    minuend = random.randint(config.number_set_min, config.max_problem)
    max_subtrahend = min(config.number_set_max, minuend)
    subtrahend = random.randint(config.number_set_min, max_subtrahend)
    answer = minuend - subtrahend
    return present_problem("{} - {} = ".format(minuend, subtrahend), answer)


def multiplication(config):
    multiplicand = random.randint(config.number_set_min, config.number_set_max)
    multiplier = random.randint(config.number_set_min, config.number_set_max)
    product = multiplicand * multiplier
    return present_problem("{} * {} = ".format(multiplicand, multiplier), product)


def division(config):
    quotient = random.randint(config.number_set_min, config.number_set_max)
    divisor = random.randint(config.number_set_min, config.number_set_max)
    dividend = quotient * divisor
    return present_problem("{} / {} = ".format(dividend, divisor), quotient)


def __config_file(f):
    return os.path.splitext(f)[0]


def __validate_config(config):
    for op in config.operations:
        if op not in ['addition', 'subtraction', 'multiplication', 'division']:
            print('ERROR: configured operation {} not valid'.format(op))


def parse_arguments():
    parser = argparse.ArgumentParser(description='Practice math facts.')
    parser.add_argument('--config-file', dest='config_file', \
            type=__config_file, default='config.py', help='config file path')
    args = parser.parse_args()
    args.config = importlib.import_module(args.config_file)
    return args


if __name__ == '__main__':
    print("\n\n")
    args = parse_arguments()
    config = args.config
    start_time = datetime.datetime.now()
    total_correct = 0
    total = 0
    for i in range(config.number_of_problems):
        operation = random.choice(config.operations)
        if operation == 'addition':
            correct = addition(config)
        elif operation == 'subtraction':
            correct = subtraction(config)
        elif operation == 'multiplication':
            correct = multiplication(config)
        elif operation == 'division':
            correct = division(config)
        total_correct += correct
        total += 1

    percentage = round(float(total_correct) / float(total) * 100.0)
    print("{} correct out of {}  ({}%)".format(total_correct, total, percentage))

    seconds = int(round((datetime.datetime.now() - start_time).total_seconds()))
    minutes = round(float(seconds) / 60.0, 1)
    print("took {} minutes  ({} seconds)".format(minutes, seconds))
