from mmh3 import hash

class Count_Min:
    def __init__(self,w=100000,d=5):
        assert d <= 20
        self.seed = [41, 13, 91, 257, 131, 37, 149, 283, 97, 31, 199, 211, 233, 17, 59, 2, 73, 179, 223, 127]
        self.w=w
        self.d=d
        self.array=[]
        for i in range(d):
            self.array.append([0 for j in range(self.w) ])

    def insert(self,s):
        for i in range(self.d):
            hash_value=hash(s,self.seed[i])%self.w
            self.array[i][hash_value]+=1

    def query(self,s):
        result=999999999
        for i in range(self.d):
            hash_value=hash(s,self.seed[i])%self.w
            result=min(result,self.array[i][hash_value])
        return result
