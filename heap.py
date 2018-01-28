class maxHeap(object):
    """docstring for maxHeap"""
    def __init__(self):
        super(maxHeap, self).__init__()
        #names of vertices
        self.H = [-1]
        #vertex values
        self.D = [-1]
        self.n = 0

    def Maximum(self):
        #return self.D[1]
        return self.H[1]

    
    def Insert(self, name, value):
        self.n = self.n+1
        self.H.append(name)
        self.D.append(value)
        self.HeapFy(self.n);
    def Update(self, name, value):
        print value
        print self.n
    def Delete(self, h):
        if(self.n == 1 or h == self.n ):
            ddd = self.D.pop()
            hhh = self.H.pop()
            self.n = self.n-1
        else:
            self.D[h]=self.D.pop()
            self.H[h]=self.H.pop()
            self.n = self.n-1
            self.HeapFy(h)
    
    def HeapFy(self, k):#D[1..n] is a max heap with a bug at k

        if(k>1 and self.D[k]>self.D[k/2]):
            #pushing up
            h=k;
            while(h>1 and self.D[h]>self.D[h/2]):
                self.swap(h,h/2);
                h=h/2;
        else:
            #pushing down
            if(k <= self.n/2 and ( ( (2*k+1) <= self.n and self.D[k] < max(self.D[2*k],self.D[(2*k)+1]) )
                or ( 2*k+1 > self.n and self.D[k] < self.D[2*k] ) ) ):
            
                h=k
                while( h <= (self.n)/2 and ( ( (2*h+1) <= self.n and self.D[h] < max( self.D[2*h], self.D[(2*h)+1]) )

                    or ( 2*h+1 > self.n and self.D[h] < self.D[2*h] )  ) ):
                    
                    d = 2*h

                    if((2*h+1) <= self.n and self.D[2*h]<self.D[(2*h)+1]):
                        d = 2*h +1
                    
                    self.swap(h,d);
                    h=d

    def swap(self, h,d):
        temp=self.D[h]
        self.D[h]=self.D[d]
        self.D[d]=temp

        temp=self.H[h]
        self.H[h]=self.H[d]
        self.H[d]=temp

    def HeapSort(self):#doubtful
        sorted_edges = []
        sorted_weights = []
        while(self.n >= 1):
            sorted_edges.append(self.H[1])
            sorted_weights.append(self.D[1])
            self.Delete(1)
        #print sorted_weights
        #print sorted_edges
        return [sorted_weights,sorted_edges]
'''
mh = maxHeap() 
mh.Insert(1,10)
print '\n', mh.H, mh.D
mh.Insert(2,30)
print '\n', mh.H, mh.D
mh.Insert(3,40)
print '\n', mh.H, mh.D
mh.Insert(4,15)
print '\n', mh.H, mh.D
mh.Insert(5,60)
print '\n', mh.H, mh.D
print mh.Maximum()
mh.Delete(1)
print '\n', mh.H, mh.D
print mh.Maximum()
'''
'''
mh = maxHeap() 
mh.Insert(3)
print mh.D
mh.Insert(2)
print mh.D
mh.Insert(1)
print mh.D
mh.Insert(15)
print mh.D
mh.Insert(5)
print mh.D
mh.Insert(4)
print mh.D
mh.Insert(45)
print mh.D
mh.Delete(1)
print mh.D
print mh.Maximum()
mh.Insert(677)
print mh.D
print mh.Maximum()
'''