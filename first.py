import tensorflow as tf
import numpy as np

# node1 = tf.constant(3.0, tf.float32)
# node2 = tf.constant(4.0)
# print(node1, node2)

# sess = tf.Session()
# print(sess.run([node1, node2]))

# node3 = tf.add(node1, node2)
# print("node3: ",node3)
# print("sess.run(node3): ",sess.run(node3))

# a = tf.placeholder(tf.float32)
# b = tf.placeholder(tf.float32)
# adder_node = a + b

# print(sess.run(adder_node,{a:3, b:4.5}))
# print(sess.run(adder_node,{a:[1,3], b: [2, 4]}))

# add_and_triple = adder_node * 3
# print(sess.run(add_and_triple, {a:3, b:4.5}))

# W = tf.Variable([.3], tf.float32)
# b = tf.Variable([-.3], tf.float32)
# x = tf.placeholder(tf.float32)
# linear_model = W * x + b

# init = tf.global_variables_initializer()
# sess.run(init)

# print(sess.run(linear_model, {x:[1,2,3,4]}))

# y = tf.placeholder(tf.float32)
# squared_deltas = tf.square(linear_model - y)
# loss = tf.reduce_sum(squared_deltas)
# print(sess.run(loss,{x:[1,2,3,4], y: [0,-1,-2,-3]}))

# optimizer = tf.train.GradientDescentOptimizer(0.01)
# train = optimizer.minimize(loss)

# sess.run(init)
# for i in range(1000):
#     sess.run(train, {x:[1,2,3,4], y:[0,-1,-2,-3]})

# print(sess.run([W, b]))

# Model parameter
W = tf.Variable([.3], tf.float32)
b = tf.Variable([-.3], tf.float32)

# Model input and output
x = tf.placeholder(tf.float32)
linear_model = W * x + b
y = tf.placeholder(tf.float32)

# loss
loss = tf.reduce_sum(tf.square(linear_model-y))

# GradientDescentOptimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

# training data
train_x = [1,2,3,4]
train_y = [0, -1, -2, -3]

# training loop
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for i in range(1000):
    sess.run(train, {x:train_x, y:train_y})

# evaluate training accuracy
cur_W, cur_b, cur_loss = sess.run([W, b, loss], {x:train_x, y: train_y})

print("W: %s b: %s loss:%s" % (cur_W,cur_b,cur_loss))




