
import multiprocessing as mp
import tensorflow as tf

#core_num = mp.cpu_count()
#config = tf.ConfigProto(
#    inter_op_parallelism_threads=core_num,
#    intra_op_parallelism_threads=core_num )
#sess = tf.Session(config=config)

#hello = tf.constant('Hello, tensorflow')

#print(sess.run(hello))

#a = tf.constant(1)
#b = tf.constant(32)
#print(sess.run(a+b))

y = tf.placeholder(tf.float32, [1])
x1 = tf.Variable(tf.zeros([1]))
x2 = tf.Variable(tf.zeros([1]))
y = tf.pow(x1,2) - 2 * x1 + tf.pow(x2,2) + 4 * x2
find_min = tf.train.GradientDescentOptimizer(0.5).minimize(y)

sess = tf.InteractiveSession()
tf.global_variables_initializer().run()

for _ in range(10):
    sess.run(find_min)
    print(sess.run(y))
