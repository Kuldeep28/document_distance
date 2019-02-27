import sys
import math

x=sys.argv[1]
y=sys.argv[2]

from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

# making tentaive answer vector  using dict

Tent_ans=x.upper()
Tent_ans=Tent_ans.replace(","," ")
Tent_ans=Tent_ans.replace("."," ")
Tent_ans=Tent_ans.replace("|"," ")
Tent_ans=Tent_ans.rsplit(" ")
#remove stop words
Tent_ans=[w for w in Tent_ans if not w in stop_words]

#stem
Tent_ans = [porter.stem(word) for word in Tent_ans]
tent_vector=dict()
for elem in Tent_ans:
    if elem in tent_vector :
        tent_vector[elem] = tent_vector[elem]+1
    else:
        tent_vector[elem]=1

# making original answer vector using dict

orig_ans=y.upper()#convert all to upper
orig_ans=orig_ans.replace(","," ")
orig_ans=orig_ans.replace("."," ")
orig_ans=orig_ans.replace("|"," ") 
orig_ans=orig_ans.rsplit(" ")# split on space to make coropus

#removing stop words
orig_ans=[w for w in orig_ans if not w in stop_words]

#stemming
orig_ans = [porter.stem(word) for word in orig_ans]

orig_vector=dict()
for elem in orig_ans:
    if elem in orig_vector:
        orig_vector[elem]=orig_vector[elem]+1
    else:
        orig_vector[elem]=1


#tentaive ans modulas
mod_tent=0
for key in tent_vector:
    mod_tent=mod_tent+((tent_vector[key])**2)
mod_tent=math.sqrt(mod_tent)

#real anwer modulas calc
mod_orig=0
for key in orig_vector:
    mod_orig=mod_orig+((orig_vector[key])**2)
mod_orig=math.sqrt(mod_orig)

numerator=0

# dot product find using vector dot

if len(orig_vector)>len(tent_vector):
    for key in orig_vector:
        if key in tent_vector:
            numerator=numerator+orig_vector[key]*tent_vector[key]
else:
    for key in tent_vector:
        if key in orig_vector:
            numerator=numerator+orig_vector[key]*tent_vector[key]

print((numerator/(mod_orig*mod_tent)))