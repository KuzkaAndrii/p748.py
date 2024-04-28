from MyWord import cut
class SentenceError(Exception):
    def __init__(self, i, c):
        self._i=i
        self._c=c
    def __str__(self):
        if self._c==1:
            return f"The tipe is incorect in {self._i}"
        else:
            return f"There are problem with {self._i} operation"
class Sentence:
    def __init__(self, l):
        self._lis=[]
        if isinstance(l, list):
            self._lis=l
            for i in range(len(self._lis)):
                if type(self._lis[i]) != str:
                    raise SentenceError(i, 1)
        elif isinstance(l, str):
            self._lis=cut(l)
    def __len__(self):
        return len(self._lis)
    def __getitem__(self, item):
        return self._lis[item]
    def __setitem__(self, key, value):
        if type(value) != str:
            raise SentenceError(key, 1)
        self._lis[key]=value
    def __add__(self, other):
        if isinstance(other, str):
            nl=self._lis
            nl.append(other)
            res=Sentence(nl)
            return res
        elif isinstance(other, Sentence):
            res=Sentence(self._lis+other._lis)
            return res
        else:
            raise SentenceError('+', 0)
    def __sub__(self, other):
        if isinstance(other, str):
            res = Sentence(self._lis)
            for i in range(len(res._lis)):
                if res[i]==other:
                    del res._lis[i]
                    break
        elif isinstance(other, Sentence):
            nl=[]
            for i in range(len(other)):
                if other[i] not in self:
                    nl.append(other[i])
            return Sentence(nl)
        else:
            raise SentenceError('-', 0)
    def __contains__(self, item):
        if item in self._lis:
            return True
        else:
            return False
    def __str__(self):
        return self._lis.__str__()
if __name__=="__main__":
    c=Sentence("I actually love english on Mechmat")
    c[2]="hate"
    try:
        c[2]=1076
    except:
        try:
            c=c+12

        except:
            print("It's all")
    print(c)


