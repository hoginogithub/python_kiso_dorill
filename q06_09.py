import argparse

parser = argparse.ArgumentParser(description='Calculate X to the power of Y')
parser.add_argument('x', type=int, help='the base')
parser.add_argument('y', type=int, help='the exponent')
args = parser.parse_args()

answer = args.x ** args.y

print(f'{args.x} ^ {args.y} = {answer}')

