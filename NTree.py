# Program     : NTree.py
# Deskripsi   : Fungsi-fungsi untuk operasi list of list.
# NIM/Nama    : xxx/Daffa Maulana Alfianto
# Tanggal     : Rabu, 20 November 2024
# ================================================================================================================

from ListFunctions import * 

# DEFINISI DAN SPESIFIKASI KONSTURKTOR
def MakePN(A, PN):
    return [A, PN]  # A adalah akar, PN adalah list anak-anak

# DEFINISI DAN SPESIFIKASI SELEKTOR
def Akar(PN):
    return PN[0]

def Anak(PN):
    return PN[1]

# DEFINISI DAN SPESIFIKASI PREDIKAT

def IsTreeNEmpty(PN):
    return PN == []

def IsOneElmt(PN):
    return not IsTreeNEmpty(PN) and IsTreeNEmpty(Anak(PN))


def NbNElmt(PN):
    if IsTreeNEmpty(PN):
        return 0
    elif IsOneElmt(PN):
        return 1
    else:
        return NbNElmt(FirstElmt(Anak(PN))) + NbNElmt(MakePN(Akar(PN), Tail(Anak(PN))))

def NbNDaun(PN):
    if IsTreeNEmpty(PN):
        return 0
    elif IsOneElmt(PN):
        return 1
    else:
        return NbNDaunChild((Anak(PN)))

def NbNDaunChild(PN):
    if IsTreeNEmpty(PN):
        return 0
    else:
        return NbNDaun(FirstElmt(PN)) + NbNDaunChild(Tail(PN))

def IsMemberNTree(x, PN):
    if IsTreeNEmpty(PN) : 
        return False
    elif IsOneElmt(PN):
        if Akar(PN) == x: 
            return True
        else: 
            return False
    else:
        if IsMemberNTree(x, FirstElmt(Anak(PN))):
            return True
        else:
            return IsMemberNTree(x, MakePN(Akar(PN), Tail(Anak(PN))))
      
def Successor(PN):
    if IsOneElmt(PN):
        return Konso(Akar(PN))
    else:
        return Konso(Successor(FirstElmt(Anak(PN))), Successor( MakePN(Akar(PN), Tail(Anak(PN)))))

T = MakePN(2,[])
print(MakePN(2,[]))
print(IsTreeNEmpty(T))
print(IsOneElmt(T))
T2 = MakePN('A', [MakePN('B',[MakePN('D',[]), MakePN('E',[]), MakePN('F',[])]), MakePN('C',[MakePN('G',[]) , MakePN('H', [MakePN('I', [])])])])
print (T2)
print(NbNElmt(T2))
print (NbNDaun (T2))




