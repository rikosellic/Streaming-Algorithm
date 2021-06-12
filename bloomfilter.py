import time
from mmh3 import hash
from bitarray import bitarray


class Bloom_Filter:
    def __init__(self,m=1000000,k=1):
        assert k<=20
        self.seed=[41,13,91,257,131,37,149,283,97,31,199,211,233,17,59,2,73,179,223,127]
        self.array=[]
        self.k=k
        self.m=m
        self.array=bitarray(m)
        self.array[:]=False

    def insert(self,s):
        for i in range(self.k):
            hash_value=hash(s,self.seed[i])%self.m
            self.array[hash_value]=True

    def query(self,s):
        for i in range(self.k):
            hash_value = hash(s, self.seed[i]) % self.m
            if not self.array[hash_value]:
                return False
        return  True
