import sys
import math

def main():
    args = sys.argv[1:]
    
    if len(args) != 1:
        print("Incorrect arguments")
        raise SystemExit
       
    I = args[0]
    if (not I.isdigit()) or (int(I) < 1):
        print("Argument must be a natural number")
        raise SystemExit

    I = int(I)
    
    with open("data/popular-names.txt", "r") as file:
        lines = file.readlines()
        L = len(lines)
        
        if I > L:
            print("Number of files is greater than number of lines")
            raise SystemExit
            
            
        num_lines = math.floor(L / I)
        
        for i in range(I):
            with open("exports/popular-names-{}.txt".format(i), "w+") as f:
                start_index = i * num_lines
                last_index = L if i == I - 1 else start_index + num_lines
                
                f.writelines(lines[start_index :last_index])

if __name__ == "__main__":
    main()
    
# Linux Command