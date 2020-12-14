import argparse

parser = argparse.ArgumentParser(prog='Prog')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--h', action='store_true')
group.add_argument('--f', action='store_true')
group.add_argument('--n', action='store_true')
args = parser.parse_args()

if args.n:
    print('input f')
elif args.h:
    print('input h')
else:
    print('input n')
