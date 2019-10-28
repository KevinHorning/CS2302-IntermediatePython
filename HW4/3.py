#10.23

def recursive(indent, num):
    if num > 0:
        recursive(indent, num//2);               
        print(" " * indent + "*" * num);     
        recursive(indent + num // 2, num//2); 
