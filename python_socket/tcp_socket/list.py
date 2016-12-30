MAX = 24

class List(object):
    def __init__(self,l):
        global MAX
        self.l = []
        while MAX:
            self.l.append(None)
            MAX -= 1
        for i in range(len(l)):
            self.l[i] = l[i]

    def my_append(self,value):
        i = 0
        while self.l[i] != None:
            if i >= len(self.l):
                printa = List([1,2,3,4,5])
                print a.l "list index out of range"
                break
            i += 1
        self.l[i] = value

    def my_insert(self,index,value):
        i = 0
        while self.l[i] != None:
            if i >= len(self.l):
                print "list index out of range"
                break
            i += 1
        while i != index:
            self.l[i] = self.l[i - 1]
            i -= 1
        self.l[index] = value


    def my_remove(self,value):
        i = 0
        while self.l[i] != value:
            if i >= len(self.l):
                print "list index out of range"
                break
            i += 1
        while self.l[i] != None:
            self.l[i] = self.l[i + 1]
            i += 1

a = List([1,2,3,4,5])
print a.l

a.my_append(100)
print a.l

a.my_insert(2,200)
print a.l

a.my_remove(4)
print a.l
