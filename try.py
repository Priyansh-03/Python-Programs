def sms_encoding(data):

    word=data.split()
    print(word)
    vowels="aeiouAEIOU"
    st=""
    for i in word:
        if(len(i)==1):
            st=st+i
        else:
            for j in i:
                if j not in vowels:
                    st=st+j
        st=st+" "
    return st[0:-1]


data="I love Python"
print(sms_encoding(data))