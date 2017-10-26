def string_both_ends ():
    x=input ("learn python")
    if(len(x) <2):
        return ''
    return str[0:2] + str[-2:]
print(string_both_ends('w3resource'))
print(string_both_ends('w3'))
print(string_both_ends('w'))