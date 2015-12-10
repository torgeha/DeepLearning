import numpy as np
#from skdata.mnist.views import OfficialImageClassification
from matplotlib import pyplot as plt
from tsne import bh_sne
from load import mnist

# load up data
#data = OfficialImageClassification(x_dtype="float32")
trX, teX, trY, teY = mnist(onehot=True)
x_data = trX
y_data = trY

print(len(x_data))
print(len(y_data))

# convert image data to float64 matrix. float64 is need for bh_sne
x_data = np.asarray(x_data).astype('float64')
x_data = x_data.reshape((x_data.shape[0], -1))


# For speed of computation, only run on a subset
n = 20000
x_data = x_data[:n]
y_data = y_data[:n]

# perform t-SNE embedding
vis_data = bh_sne(x_data)

# plot the result
vis_x = vis_data[:, 0]
vis_y = vis_data[:, 1]

# convert labels
labels = []
for arr in y_data:
    labels.append(np.argmax(arr))

plt.scatter(vis_x, vis_y, c=labels, cmap=plt.cm.get_cmap("jet", 10))

#plt.scatter(vis_x, vis_y, 20, labels)
plt.colorbar(ticks=range(10))
plt.clim(-0.5, 9.5)
plt.savefig("tsnetest")