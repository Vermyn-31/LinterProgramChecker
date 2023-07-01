import argparse
def parser_function():
    parser = argparse.ArgumentParser(
        prog = 'cmdarg',
        description= 'This is an example of a parser for arguments'
    )
    parser.add_argument('filename')
    args = parser.parse_args()

    return str(args.filename)

