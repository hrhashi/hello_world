
import multiprocessing as mp
import tensorflow as tf

core_num = mp.cpu_count()
config = tf.ConfigProto(
    inter_op_parallelism_threads=core_num,
    intra_op_parallelism_threads=core_num )
sess = tf.Session(config=config)

hello = tf.constant('Hello, tensorflow')

print(sess.run(hello))

a = tf.constant(1)
b = tf.constant(32)
print(sess.run(a+b))

y = tf.placeholder(tf.float32, [1])
x = tf.Variable(tf.zeros([1]))
y = tf.pow(x,2) - 2*x + 10
find_min = tf.train.GradientDescentOptimizer(0.5).minimize(y)

sess = tf.InteractiveSession()
tf.global_variables_initializer().run()

for _ in range(10):
    sess.run(find_min)
    print(sess.run(y))

#train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
#    
#    sess = tf.InteractiveSession()
#    tf.global_variables_initializer().run()
#    # Train
#    for _ in range(1000):
#        batch_xs, batch_ys = mnist.train.next_batch(100)
#        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})