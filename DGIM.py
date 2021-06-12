import math

class DGIM:
    def __init__(self,window=1000):
        self.window=window
        self.container={} #key: log2 of batch size, value: a list of timestamp
        self.maxkey=int(math.log2(self.window))+1
        self.current_max=-1 #Record current biggest bucket size
        self.current_timestamp=-1
        for i in range(self.maxkey):
            self.container[i]=[]

    def insert(self,bit,timestamp):
        timestamp=timestamp%self.window
        self.current_timestamp=timestamp
        if self.current_max >=0 and self.container[self.current_max][0]==timestamp: #Remove the out-dated bucket, check each time
            del self.container[self.current_max][0]
            if len(self.container[self.current_max])==0:
                self.current_max-=1
        if bit==1:
            self.container[0].append(timestamp)
            self.current_max=max(0,self.current_max)
            for i in range(self.maxkey):
                if len(self.container[i])<=2:
                    break
                else:
                        self.container[i+1].append(self.container[i][1])
                        self.container[i]=self.container[i][-1:]
                        self.current_max=max(i+1,self.current_max)

    def query(self, interval):
        assert self.current_timestamp>=0 and interval <= self.window and interval>=1
        sum=0
        for i in range(self.maxkey):
            for j in range(len(self.container[i])-1,-1,-1):
                time=self.container[i][j]
                if (self.current_timestamp-time+1)%self.window>interval:
                    print('There are {} ones estimated in the last {} bits'.format(sum, interval))
                    return sum
                else:
                    if (self.current_timestamp-time)%self.window+2**i<=interval:
                        sum+=2**i
                    else:
                        sum+=min(2**(i-1),interval-(self.current_timestamp-time)%self.window) # Slight modification
                        print('There are {} ones estimated in the last {} bits'.format(sum, interval))
                        return sum
        print('There are {} ones estimated in the last {} bits'.format(sum,interval))
        return sum
