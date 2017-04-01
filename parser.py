import argparse


# return parsed arguments
def get_parsed_args(prog_name):
    parser = argparse.ArgumentParser(prog=prog_name)
    # input file :
    parser.add_argument(dest='input')
    # output file :
    parser.add_argument(dest='output')
    # vertical / horizontal scanning:
    parser.add_argument('--scan', dest='scan_mode', choices=['vertical', 'horizontal'], default='horizontal')
    # tempo:
    parser.add_argument('-t', dest='tempo', choices=range(20, 200, 1), default=120, type=int)
    # scan precision :
    parser.add_argument('-p', dest='precision', choices=range(1, 20, 1), default=5, type=int)
    result = parser.parse_args()
    if not str.endswith(result.input, '.png'):
        result.input += '.png'
    if not str.endswith(result.output, '.midi'):
        result.output += '.midi'
    return result
