import tensorflow as tf

x1 = tf.constant(5)
x2 = tf.constant(6)

result = tf.multiply(x1, x2)

print(result)

'''
sess = tf.Session()
print(sess.run(result))
sess.close()
'''
#the following method automatically closes session
with tf.Session() as sess:
	output = sess.run(result)
	#is output a session variable or a python variable??
	print(output)

print(output)
