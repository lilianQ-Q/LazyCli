import sys
import argparse

#c'est bien de fou le args parser

parser = argparse.ArgumentParser()
parser.add_argument("-z", "--zebi", help="sku", required=True)
args = parser.parse_args()

input = ""
while(input != "exit"):
    input = raw_input("sub >>> ")