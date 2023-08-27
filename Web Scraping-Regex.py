//again bekhunam

#https://regex101.com/

# REgular Expression

# . -> har chizi    \d-> digit     \w-> word    \s->whitesapce  
#  * ->harchand ta    + -> 1 ta binahayat
# [abc]   [^abc]
# ()  -> group
# {n,m} -> az n m ta
# {n}
#  ^ shoru khat
#  $  payan khat

#  .  +  *  { }  ?  \s  \w  \d   \t  \n   [abc]  [A-Z]  [^ab]  ()



#\s....\s  -> har chiz 4 harfi ke ghablesh space va badesham space
# .*$  -> har chi har chandta ta payan khat
# ^1  -> shoru khat 1 bashad


import re
str='salam zohreh, salam jadi'
re.search(r'salalm', str)
result=re.search(r'salam',str)
result.span()
result.start()


input='jadi@gmail.com'
print(re.search(r'.+\@.+\..{2,3}', input))
