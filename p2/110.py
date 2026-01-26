import sys
import string

SPACE = "    "
GAP = SPACE * 8
ALPHABET = list(string.ascii_lowercase)

def lsh(select: list):
    select.append(select.pop(0))

def swap(select, i, j):
    select[i], select[j] = select[j], select[i]

def print_if(d, select, i, j):
    dprint(d, "if", ALPHABET[select[i]], "<", ALPHABET[select[j]], "then")
            
def print_writeln(d, select):
    dprint(d, "writeln(" + ",".join([ALPHABET[s] for s in select]) + ")")

def dprint(d, *args):
    print(d * SPACE, *args)

def solve(n):
    select = list(range(n))
    lsh(select)
    
    def meta_sort(d):
        if d == n - 1:
            print_writeln(d, select)
        else:
            lsh(select)
            for i in range(0, d+1):  
                print_if(d, select, n - i - 2, n - i - 1)
                meta_sort(d + 1)
                
                swap(select, n - i - 2, n - i - 1)

                dprint(d, "else")

                if i == d:
                    meta_sort(d + 1)

    meta_sort(0)

def main():
    numbers = [int(line.strip()) 
        for line in sys.stdin.readlines() if line.strip() != ""]

    if len(numbers) <= 0:
        return

    m = numbers[0]

    for i in range(0,m):
        if i != 0:
            print()

        n = numbers[i+1]

        vars = ",".join(ALPHABET[:n])

        print("program sort(input,output);")
        print("var")
        print(vars + " : integer;")
        print("begin")
        print("readln(" + vars + ");")
        solve(n)
        print("end.")
        
if __name__ == "__main__":
    main()


