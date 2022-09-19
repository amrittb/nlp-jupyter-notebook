import sys

def main():
    args = sys.argv[1:]
    
    if len(args) != 1:
        print("Incorrect arguments")
        raise SystemExit
       
    I = args[0]
    if (not I.isdigit()) or (int(I) < 1):
        print("Line must be a natural number")
        raise SystemExit

    I = int(I)
    
    with open("data/popular-names.txt", "r") as file:
        lines = file.readlines()
        L = len(lines)
        
        for i in range(max(L-I,0), L):
            print(lines[i].strip())
            
if __name__ == "__main__":
    main()
    
# Linux Command
# diff <(python 15.last-n-lines.py 10) <(tail -10 popular-names.txt)