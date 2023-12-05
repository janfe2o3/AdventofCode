#!/usr/bin/python3
import argparse
import subprocess
import sys
import requests

# Usage: ./get_input.py > 1.in
# You must fill in SESSION following the instructions below.
# DO NOT run this in a loop, just once.

# You can find SESSION by using Chrome tools:
# 1) Go to https://adventofcode.com/2023/day/1/input
# 2) right-click -> inspect -> click "Network".
# 3) Refresh
# 4) Click click
# 5) Click cookies
# 6) Grab the value for session. Fill it in.
SESSION = '53616c7465645f5f30ca6350a20ce203948107de94d69c395b9a77a644daeda0c92ef401179cd58d8bd5b7a1604f02cd0e865aac2d30e3fbb2d98492b530bec6'

useragent = 'https://github.com/jonathanpaulson/AdventOfCode/blob/master/get_input.py by jonathanpaulson@gmail.com'
parser = argparse.ArgumentParser(description='Read input')
parser.add_argument('--year', type=int, default=2023)
parser.add_argument('--day', type=int, default=1)
args = parser.parse_args()
def get_input(day, year=2023):
    cmd = f'curl https://adventofcode.com/{year}/day/{day}/input --cookie "session={SESSION}" -A {useragent}'
    output = subprocess.check_output(cmd, shell=True)
    output = output.decode('utf-8')
    #print(output, end='')
    #print(
    return '\n'.join(output.split('\n')[:10])

