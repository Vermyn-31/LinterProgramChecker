import argparse
from pathlib import Path

def linter_program(string, opening="", line_num=1, missing_line_num=""):
    # Corresponding openings and closings of the parenthesis, brackets and braces
    opening_dict = {"(": ")", "[": "]", "{": "}"}
    closing_dict = {")": "(", "]": "[", "}": "{"}

    
    # Base Case
    if not string:
        if opening:
            print(f"Line {missing_line_num.split(':')[1:][0]}: missing closing symbol '{opening_dict[opening[0]]}'")
            return linter_program("", opening[1:], line_num, ":".join(missing_line_num.split(':')[1:]))
        return
    
    # Missing Line Number Case
    if not missing_line_num and opening:
        missing_line_num = line_num
    if not opening:

        missing_line_num = ""

    # Opening Cases
    if string[0] in "([{":
        return linter_program(string[1:], opening+string[0], line_num, missing_line_num+":"+str(line_num))
    
    # Closing Cases
    elif string[0] in ")]}":
        if not opening:
            print(f"Line {line_num}: stray closing symbol '{string[0]}'")
            return linter_program(string[1:], opening, line_num, missing_line_num)
        elif opening[-1] == closing_dict[string[0]]:
            return linter_program(string[1:], opening[:-1], line_num, ":".join(missing_line_num.split(':')[:-1]))
        else:
            print(f"Line {line_num}: stray closing symbol '{string[0]}'")
            return linter_program(string[1:], opening, line_num, missing_line_num)
    
    # Counting the Line Number Case
    elif string[0] == "\n":
        return linter_program(string[1:], opening, line_num + 1, missing_line_num)
    else:
        return linter_program(string[1:], opening, line_num, missing_line_num)

def main():   
    #Parsing the filename to open using cmd
    parser = argparse.ArgumentParser(prog = 'cmdarg')
    parser.add_argument('filename')
    args = parser.parse_args()

    #Openng ithe file and use its content as an input for the linter program
    fpath = Path.cwd().joinpath(args.filename)  
    with open(fpath,'r') as file:
        string_fpath = file.read()

    print(string_fpath)  
    lst = string_fpath.split("\n")
    print(lst)
    linter_program(string_fpath)

if __name__ == '__main__':
    main()


