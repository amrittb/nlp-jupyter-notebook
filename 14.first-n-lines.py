import sys

def main():
    args = sys.argv[1:]
    
    if len(args) != 1:
        print("Incorrect arguments")
        raise SystemExit
       
    line = args[0]
    if (not line.isdigit()) or (int(line) < 1):
        print("Line must be a natural number")
        raise SystemExit

    line = int(line)
    
    with open("data/popular-names.txt", "r") as file:
        lines = file.readlines()
        
        line = min(line, len(lines))
        
        for i in range(line):
            print(lines[i].strip())
            
if __name__ == "__main__":
    main()
    
# Linux Command
# diff <(python 14.first-n-lines.py 10) <(head -10 popular-names.txt)