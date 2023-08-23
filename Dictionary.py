#Dictionary


f2t=dict()
f2t['yek']='bir'
f2t['do']='ikki'

print(f2t)

#-------
ghad={}
type(ghad)
ghad={'jadi':180, 'ali':200, 'Zoreh':162}
print(ghad)
print(ghad['jadi'])

#-------
#key , value
print(ghad.keys())
list[ghad.keys()]
print(ghad.values())
list[ghad.values()]
#-------
#'jadi' in ghad -> True
#ghad.get('jadi', 500)
#-------

string='salam. Zohreh is here and testing python for fun'
tedad=dict()

for letter in string:
    if letter in tedad:
      tedad[letter]+=1
    else:
        tedad[letter]=1
print(letter, tedad)


#OR------------------------------
string='salam. Zohreh is here and testing python for fun'
tedad=dict()
for letter in string:
    if letter in tedad:
        tedad[letter]=tedad.get(letter,0)+1
print(letter, tedad)

