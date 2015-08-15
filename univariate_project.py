import collections 
import matplotlib.pyplot as plt 
import numpy as np 
import scipy.stats as stats



#test data 
testlist = [1, 4, 5, 6, 9, 9, 9]

#thsi will print out a list of the test data 
c = collections.Counter(testlist)

print c 

#calculate the number of instances in the list 

count_sum = sum(c.values())

print "the total number of data points in the test list is %s." %(count_sum)

for k, v in c.iteritems():
	print "the frequency of number " + str(k) + " is "  + str(float(v) / count_sum) 


#create a boxplot from testlist 

plt.title('This is a boxplot')
plt.boxplot(testlist)
plt.savefig('boxplot.png')

#create a histogram from testlist 

plt.title('This is a histogram')
plt.hist(testlist, histtype='bar') 
plt.savefig('histogram.png')

#create a qq plot from testlist 

plt.figure()
plt.title('This is a qq plot with a normal distribution')
sample_data = testlist
sample_data = np.random.normal(size=count_sum)
graph1 = stats.probplot(sample_data, dist="norm", plot=plt)
plt.savefig('qq_plot.png')






