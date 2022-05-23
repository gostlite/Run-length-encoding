
def run_len(array):
    lent = [[array.count(array[c]), array[c]] for c in range(0, len(array))if not array[c] == array[c-1] ]
    print(lent)
    
    

name = "aaaaaaaaaaaaaabbbbb"
run_len(name)