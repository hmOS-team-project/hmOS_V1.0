#coding=utf-8

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np
import matplotlib.pyplot as plt
num_steps = 10000
ExampleNum = 10000
InputDim = 1000
ResultSize = 100
filePath_X = 'MCPinputX_' + str(ExampleNum) + '_' + str(InputDim) + '_' + str(ResultSize) + '.txt'
filePath_Y = 'MCPlable_' + str(ExampleNum) + '_' + str(InputDim) + '_' + str(ResultSize) + '.txt'

# 导入 训练数据

text_dir="C://Users/10257/Desktop/Mobike2017/Mobike2017/DataGenerate/MCPinputX_100_10_3.txt"
train_dir="C://Users/10257/Desktop/Mobike2017/Mobike2017/DataGenerate/MCPinputX_10000_1000_100.txt"
f = open(text_dir, 'r')
f_train = open(train_dir,'r')
labeled_data_sets = []
inputx=[]
i=0
for line in f.readlines():
    coding = []
    coding=line.strip().split(' ') #strip()除去/n
    coding = list(map(int, coding)) #字符串数组转化成整数数组
    inputx.extend(coding)
   # labeled_dataset= inputx[i]
    #labeled_data_sets.append(labeled_dataset)
   # print(labeled_data_sets[i])
   # i+=1
f.close()
inputx_train=[]
for line in f_train.readlines():
    coding = []
    coding=line.strip().split(' ') #strip()除去/n
    coding = list(map(int, coding)) #字符串数组转化成整数数组
    inputx_train.extend(coding)
   # labeled_dataset= inputx[i]
    #labeled_data_sets.append(labeled_dataset)
   # print(labeled_data_sets[i])
   # i+=1
f_train.close()
print(len(inputx_train))
result = []
for y in range(0, 10000):
  for x in range(0, 1000):
       if x == 0:
         result.append([])
       result[y].append(inputx_train[x + y * 1000])
# 参数
learning_rate = 0.01    #学习速率
training_epochs = 20    #训练批次
batch_size = 256        #随机选择训练数据大小
display_step = 100        #展示步骤
#examples_to_show = 10   #显示示例图片数量

# 网络参数
#我这里采用了三层编码，实际针对mnist数据，隐层两层，分别为256，128效果最好
n_hidden_1 = 512  #第一隐层神经元数量
n_hidden_2 = 256  #第二
n_hidden_3 = 128  #第三
n_input = 1000     #输入

#tf Graph输入
X = tf.placeholder("float", [None,n_input])

#权重初始化
weights = {
    'encoder_h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
    'encoder_h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
    'encoder_h3': tf.Variable(tf.random_normal([n_hidden_2, n_hidden_3])),
    'decoder_h1': tf.Variable(tf.random_normal([n_hidden_3, n_hidden_2])),
    'decoder_h2': tf.Variable(tf.random_normal([n_hidden_2, n_hidden_1])),
    'decoder_h3': tf.Variable(tf.random_normal([n_hidden_1, n_input])),
}

#偏置值初始化
biases = {
    'encoder_b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'encoder_b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'encoder_b3': tf.Variable(tf.random_normal([n_hidden_3])),
    'decoder_b1': tf.Variable(tf.random_normal([n_hidden_2])),
    'decoder_b2': tf.Variable(tf.random_normal([n_hidden_1])),
    'decoder_b3': tf.Variable(tf.random_normal([n_input])),
}

# 开始编码
def encoder(x):
    #sigmoid激活函数，layer = x*weights['encoder_h1']+biases['encoder_b1']
    layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weights['encoder_h1']),
                                   biases['encoder_b1']))
    layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1, weights['encoder_h2']),
                                   biases['encoder_b2']))
    layer_3 = tf.nn.sigmoid(tf.add(tf.matmul(layer_2, weights['encoder_h3']),
                                   biases['encoder_b3']))
    return layer_3

# 开始解码
def decoder(x):
    #sigmoid激活函数,layer = x*weights['decoder_h1']+biases['decoder_b1']
    layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weights['decoder_h1']),
                                   biases['decoder_b1']))
    layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1, weights['decoder_h2']),
                                   biases['decoder_b2']))
    layer_3 = tf.nn.sigmoid(tf.add(tf.matmul(layer_2, weights['decoder_h3']),
                                   biases['decoder_b3']))
    return layer_3

# 构造模型
encoder_op = encoder(X)
encoder_result = encoder_op
decoder_op = decoder(encoder_op)

#预测
y_pred = decoder_op
#实际输入数据当作标签
y_true = X

# 定义代价函数和优化器，最小化平方误差,这里可以根据实际修改误差模型
cost = tf.reduce_mean(tf.pow(y_true-y_pred, 2))
optimizer = tf.train.RMSPropOptimizer(learning_rate).minimize(cost)

# 初始化变量
init = tf.initialize_all_variables();

# 运行Graph
with tf.Session() as sess:
    sess.run(init)
    #总的batch
  #  total_batch = int(mnist.train.num_examples/batch_size)
    # 开始训练
  #  for epoch in range(training_epochs):
   #     for i in range(total_batch):
    for i in range(1, num_steps + 1):
            batch_xs = np.array(result[i])
            batch_ys,c = sess.run([optimizer, cost], feed_dict={X: batch_xs})
            if i % display_step == 0 or i == 1:
                print('Step %i: Minibatch Loss: %f' % (i, c))
    # 展示每次训练结果
      #  if epoch % display_step == 0:
          #  print("Epoch:", '%04d' % (epoch+1),
           #       "cost=", "{:.9f}".format(c))
    print("Optimization Finished!")
    # Applying encode and decode over test set
    #显示编码结果和解码后结果

    encodes = sess.run(
        encoder_result, feed_dict={X: inputx})
    encode_decode = sess.run(
        y_pred, feed_dict={X: inputx})

    cnt = 0
    for i in range(len(g[0])):
        if y_pred[0][i] >= 0.5:
            y_pred[0][i] = 1
        else:
            y_pred[0][i] = 0
        if y_pred[0][i] == inputx[i]:
            cnt = cnt + 1
    precision = cnt / 1000.0
    print('准确度是 %f' % (precision))


    # 对比原始图片重建图片
    # f, a = plt.subplots(2, 10, figsize=(10, 2))
    # for i in range(examples_to_show):
    #     a[0][i].imshow(np.reshape(mnist.test.images[i], (28, 28)))
    #     a[1][i].imshow(np.reshape(encode_decode[i], (28, 28)))
    # f.show()
    # plt.draw()
    # plt.savefig()
    # plt.waitforbuttonpress()

