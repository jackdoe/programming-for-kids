## [DAY-164] pointers

Write a program to prepare for the test tomorrow. Its a test of abbreviations, from abbreviation to meaning. Make a program to help you study, it should ask you for a abbreviation and then you should write its meaning.

```
t.z.t -> ten zijner tijd
v.l.n.r -> van links naar rechts
e.d -> en dergelijk
nr. -> nummer
zg. -> zogenaamd
Gebr. -> gebroeders
dr. -> doctor
s.v.p -> s'il vous plait
t.o.v -> ten opzichte van
nl. -> namelijk
N.B. -> Nota Bene
sr. -> senior
jr. -> junior
C -> Celsius
etc -> etcetra
t.a.v -> ter attentie van
P.S. -> postscriptum
B. en W. -> Burgemeesteren Wethouders
NL -> Nederland
v.a -> vanaf
drs -> doctorandes
```

The program will have 2 lists with the same amount of elements, you should pick a random index, ask the user to type the meaning for `abbreviations[i]` and compare it with `meaning[i]`

```
import random
def test(taal,toets):
    i = random.randint(0,len(taal)-1)
    f = input(taal[i]+ ': ')
    if f == toets[i]:
        print('corect')
    else:
        print("WRONG, one more try!")
        f = input(taal[i]+ ': ')
        if f == toets[i]:
            print('corect')
        else:
            print('better luck next time the correct answer was: '+toets[i])

short = ['t.z.t','v.l.n.r','e.d','nr.','zg.','Gebr.','dr.',
         's.v.p','t.o.v','nl.','N.B.','sr.','jr.','C',
         'etc','t.a.v','P.S.','B. en W.','NL','v.a','drs']

long = ['ten zijner tijd','van links naar rechts','en dergelijk',
        'nummer','zogenaamd','gebroeders','doctor',
        "s'il vous plait",'ten opzichte van','namelijk',
        'Nota Bene','senior','junior','Celsius',
        'etcetra','ter attentie van','postscriptum',
        'Burgemeesteren Wethouders','Nederland','vanaf','doctorandes']

for i in range(len(short)):
    print(short[i] + ' -> ' + long[i])

while True:
    test(short,long)
    test(long, short)
```

## [DAY-165] pointers

Watch "What Are Pointers? (C++)", by javidx9 on youtube. https://www.youtube.com/watch?v=iChalAKXffs

