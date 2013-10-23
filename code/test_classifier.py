import PyML
import pickle
k = PyML.ker.Gaussian(gamma=3)
data = PyML.VectorDataSet('training-9k.txt', labelsColumn = -1)
test_data = PyML.VectorDataSet('test-1k.txt', labelsColumn = -1)
s = PyML.SVM(k)
s.train(data)
s.save('the_svm_ten')
#foo = s.test(test_data)

#print foo.getPredictedClass()

r = s.cv(data, 5)
print r