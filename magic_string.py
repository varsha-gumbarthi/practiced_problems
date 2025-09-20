def magic_string(str1):
    my_dict={}
    for i in str1:
        if i in my_dict:
            my_dict[i]+=1
        else:
            my_dict[i]=1
    maxx=max(my_dict.values())
    result=len(str1)-maxx
    return result
str1=input()
print(magic_string(str1))