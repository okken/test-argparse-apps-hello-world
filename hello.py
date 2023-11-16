import argparse


def parse_args(arg_list: list[str] | None):
    parser = argparse.ArgumentParser()

    parser.add_argument('name', type=str, default='World',
                        nargs='?', help='any name')

    parser.add_argument('-g', '--goodbye', action='store_true',
                        help='say goodbye instead')

    parser.add_argument('-d', '--debug', action='store_true',
                        help=argparse.SUPPRESS)


    args = parser.parse_args(arg_list)

    if args.debug:  # pragma: no cover
        print('--- debug output ---')
        print(f'  {args=}')
        print(f'  {args.goodbye=}, {args.name=}')
        print('')
    return args


def main(arg_list: list[str] | None = None):
    args = parse_args(arg_list)

    if args.goodbye:
        print(f'Goodbye, {args.name}!')
    else:
        print(f'Hello, {args.name}!')


if __name__ == '__main__':
    main()