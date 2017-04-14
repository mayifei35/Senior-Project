import numpy as np
np.random.seed(4)
import csv

'''
generate peremeter and weights
'''
#cutting down premeters
data=np.genfromtxt('recordws45.csv',delimiter=',',dtype=float)
data_size=45000
flap=data[:,0]
nflap=data[:,1]
result=data[:,2]
playerY=data[:,3]
#nextTopY=data[:,3]
nextBottomY=data[:,4]
#nextDistance=data[:,5]
#nnextTopY=data[:,6]
nnextBottomY=data[:,5]
#nnextDistance=data[:,8]

weightf =np.random.rand(1)
weightnf=np.random.rand(1)
weight2 =0
weight3 =np.random.rand(1)
weight4 =np.random.rand(1)
#weight4=0
weight5 =np.random.rand(1)
#weight6 =np.random.rand(1)
#weight7 =np.random.rand(1)
#weight7=0
#weight8 =np.random.rand(1)
#weight9 =np.random.rand(1)
bias = np.random.rand(1)
weights=np.matrix([weightf,weightnf,weight2,weight3,weight4,weight5])

learning_rate=0.38
epochs=5

def linearRegression ():

    global weights,learning_rate,bias,epochs
    trans_data=data.transpose()
    start_error=np.sum(np.dot(weights,trans_data))+bias*data_size-np.sum(result)
    init_cost = np.power(start_error, 2)
    print ' initial cost %s'% init_cost
    print ' initial error is %s'%start_error

    for e in range(0,epochs):
        global sum_error,weightf,weightnf,weight2,weight3,weight4,weight5
        
        for i in range(0,data_size-1):
            sum_error=0
            curr_error=np.sum(np.dot(weights,data[i]))+bias-result[i]          
            sum_error +=curr_error
            weightf = weightf - (learning_rate * curr_error * flap[i] )  
            weightnf= weightnf- (learning_rate*curr_error*nflap[i])
            #weights[1]=0 rewards
            weight3 = weight3 - (learning_rate * curr_error * playerY[i])
            # weights[3] = weights[3] - (learning_rate * curr_error * nextTopY[i])
            weight4 = weight4 - (learning_rate * curr_error * nextBottomY[i] )
            weight5 = weight5 - (learning_rate * curr_error * nnextBottomY[i])
            # weights[6] = weights[6] - (learning_rate * curr_error * nnextTopY[i])
            #weight6 = weight6 - (learning_rate * curr_error * nnextBottomY[i])
            #weight9 = weight9 - (learning_rate * curr_error * nnextDistance[i])
            bias = bias - (learning_rate * curr_error *2.0 )
            end_cost=np.power(sum_error,2)
	    #if -100<sum_error<100:
              #print sum_error,i 	    
        print  'end cost %s'%end_cost
    weightsNbias=np.matrix([weightf,weightnf,weight2,weight3,weight4,weight5,bias])
    np.savetxt('weights2v.csv',weightsNbias,delimiter=',')
linearRegression()




