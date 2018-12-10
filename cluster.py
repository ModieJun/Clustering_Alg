from numpy import array,random,divide,zeros,alltrue,copy,sum
import math

class vector_quant():
    def __init__(self,inp,num_cluster):
        self.inp= inp
        self.num_cluster= num_cluster
        # WE NEED TO CREATE num_cluster MEANS
        self.prototype=zeros((num_cluster,2),dtype=float)
        # classifies the points to each prototype
        self.classify=[None]*len(self.inp)
        self.converge=False
        # print(self.inp))
        random.seed(6)
        for x in range(num_cluster):
            rand1= random.randint(0,len(self.inp))
            self.prototype[x]= self.inp[rand1]
        # print(self.prototype )
        
    def euclid_dist(self,pt1,pt2):
        # we have 2 pt with [x,y]
        dist= (pt1[0]-pt2[0])**2+(pt1[1]-pt2[1])**2
        return math.sqrt(dist)

    def find_closest_pt(self,point):
        for x in range(len(self.prototype)):
            dist = self.euclid_dist(point,self.prototype[x])
            # print(dist)
            if x== 0:
                distance =dist
                closest_prototype=0
            else:
                if dist <distance:
                    distance = dist
                    closest_prototype=x
        return closest_prototype 

    def fix_prototype(self):
        self.previous = copy(self.prototype)
        for x in range(len(self.prototype)):
            count =0
            temp =array([0,0],dtype=float)
            y=0
            while y<len(self.classify):
                if self.classify[y]==x:
                    temp+=self.inp[y]
                    count+=1
                y+=1
            self.prototype[x]=divide(temp,count)
            # print(self.prototype)
        # print("Changed prototype to" + str(self.prototype))
        # print("Previous Prototype: " + str(self.previous))
        
        # IF THE DIFFERENCE IS LESS THAN 0.2 THEN WE HAVE CONVERGED TO LOCAL MINUMUM
        # IDK if this is the correct convergence condition
        decision = abs(self.prototype-self.previous)<0.0000000000000000000000000000000000001

        # print(self.prototype-self.previous)
        # print(decision)
        if (alltrue(decision)):
            # print('true')
            self.converge=True
            
                   
    def run_alg(self):
        # STOP CONDITION OF THE CHANGE IN THE PROTOTYPE DISTANCE
        # IS VERY SMALL AND NEGLIGABLE 
        count =0
        # while not self.converge:
        while not self.converge:
            if count >100:
                break
            for x in range(len(self.inp)):
                self.classify[x]=self.find_closest_pt(self.inp[x])
            # print(self.classify)
            self.fix_prototype()
            count+=1
        print('Iteration:'  + str(count))
        print('Result: ' + str(self.prototype))
        result=sum(self.prototype)
        print(str(result))

def main():
    num_cluster = int(input())
    # read in all the input data
    inp=[]
    while True:
        read= input()
        if read=='':
            break
        read = read.split(',')
        inp.append(read)   
    inp = array(inp,dtype=float) 
    # print(inp[2])
    vq=vector_quant(inp,num_cluster) 
    vq.run_alg()  
    

if __name__ == "__main__":
    main()