import tensorflow as tf

x1 = tf.constant(5)
x2 = tf.constant(6)
x3 = tf.Variable(x1*2 + x2)
#print(result)

'''
sess = tf.Session()
print(sess.run(result))
sess.close()
'''


#the following method automatically closes session
with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())
	output = sess.run(x3)
	#is output a session variable or a python variable??
	print(output)

print(output)
#it turns out output is a python variable unrelated to the session itself

