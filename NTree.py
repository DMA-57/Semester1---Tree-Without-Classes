from listFunctions import *

# Membuat pohon
def MakePN(A, PN):
    return [A, PN]  # A adalah akar, PN adalah list anak-anak

# Mengambil akar dari pohon
def Akar(P):
    return P[0]

# Mengambil anak-anak dari pohon
def Anak(P):
    return P[1]

# Mengecek apakah pohon kosong
def IsTreeEmpty(PN):
    return PN == [] or (not Akar(PN) and IsEmpty(Anak(PN)))

# Mengecek apakah pohon hanya memiliki satu elemen (akar tanpa anak)
def IsOneElemt(PN):
    return not IsTreeEmpty(PN) and IsEmpty(Anak(PN))


def IterateChild(x, L):
    if IsEmpty(L):
        return 
    else:
        if IsMemberNTree(x, FirstElmt(L)):
            return True
        else:
            return IterateChild(x, Tail(L))

# Mengecek apakah x adalah anggota dari pohon
def IsMemberNTree(x, PN):
    if IsTreeEmpty(PN) : 
        return False
    elif IsOneElemt(PN):
        if Akar(PN) == x: 
            return True
        else: 
            return False
    else:
        if IsMemberNTree(x, FirstElmt(Anak(PN))):
            return True
        else:
            return IsMemberNTree(x, MakePN(Akar(PN), Tail(Anak(PN))))
        
def Succecor(PN):
    if IsOneElemt(PN):
        return Akar(PN)
    else:
        



pohon = MakePN('D', [
    MakePN('A', [
        MakePN('M', [
            MakePN('N', []),
            MakePN('I', []),
            MakePN('T', [])
        ]),
        MakePN('U', [])  
    ]),
    MakePN('F', [
        MakePN('L', [
            MakePN('O', [])
        ])
])])

tree = MakePN('D', [
    MakePN('I', [
        MakePN('H', [
            MakePN('P', []),
            MakePN('R', []),
            MakePN('T', [])
        ]),
        MakePN('M', [
            MakePN('T', [])
        ])
    ]),
    MakePN('A', [
        MakePN('L', []),
        MakePN('U', []),
        MakePN('W', [])
    ])
])

print(IsMemberNTree("D",tree))


print(IsMemberNTree('G', pohon))  # Output: False
print(IsMemberNTree('X', pohon))  # Output: False
