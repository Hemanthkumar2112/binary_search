def binary_search_re(a:list,target:int)->str :
    if len(a)==0:return "NOT FOUND"
    a.sort()
    mid = len(a)//2
    if a[mid]== target:return "FOUND"
    else:
        if a[mid] < target:return binary_search_re(a[mid+1:],target)
        if a[mid] > target:return binary_search_re(a[:mid],target)
    
x = binary_search_re(a,7)
print(x)
