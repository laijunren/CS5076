def without_vowels(s):
    vowel = "a,e,i,o,u,A,E,I,O,U"

    st = ""
    for i in s:
        if i in vowel:
            st+=""
        else:
            st+=i
    return st


str = 'I do not like vowels!'

print(without_vowels(str))