import tensorflow as tf


class MLPClassifier:

	def __init__(self, hidden_layer_sizes=(100,), alpha=1e-4, batch_size=256, learning_rate_init=1e-3):

		self.coeffs_ = {}
		self.intercepts_ = {}
		self.hidden_layer_sizes_ = hidden_layer_sizes
		self.alpha = alpha
		self.batch_size = batch_size
		self.learning_rate_init = learning_rate_init
		self._n_hidden_layers_ = len(self.learning_rate_init)
		self.n_layers_ = self._n_hidden_layers_+2


	def create_placeholders(self, n_x, n_y):
	    """
	    Creates the placeholders for the tensorflow session.
	    
	    Arguments:
	    n_x -- scalar, size of an image vector (num_px * num_px = 64 * 64 * 3 = 12288)
	    n_y -- scalar, number of classes (from 0 to 5, so -> 6)
	    
	    Returns:
	    X -- placeholder for the data input, of shape [n_x, None] and dtype "float"
	    Y -- placeholder for the input labels, of shape [n_y, None] and dtype "float"
	    
	    Tips:
	    - You will use None because it let's us be flexible on the number of examples you will for the placeholders.
	      In fact, the number of examples during test/train is different.
	    """

	    ### START CODE HERE ### (approx. 2 lines)
	    X = tf.placeholder(tf.float32, shape=(n_x, None), name='X')
	    Y = tf.placeholder(tf.float32, shape=(n_y, None), name='Y')
	    ### END CODE HERE ###
	    
	    return X, Y


	def initialize_parameters(self, n_x, n_y):
	    """
	    Initializes parameters to build a neural network with tensorflow. The shapes are:
	                        W1 : [25, 12288]
	                        b1 : [25, 1]
	                        W2 : [12, 25]
	                        b2 : [12, 1]
	                        W3 : [6, 12]
	                        b3 : [6, 1]
	    
	    Returns:
	    parameters -- a dictionary of tensors containing W1, b1, W2, b2, W3, b3
	    """
	    
	    tf.set_random_seed(1)                   # so that your "random" numbers match ours
	    l_size = 0
	    sizes = []
	    sizes.append(n_x)
	    sizes.append(list(self.hidden_layer_sizes_))
	    sizes.append(n_y)

	    for l in range(self.n_layers_):
	        
	    	l.size = self.hidden_layer_sizes_[l]

	    	self.coeffs_["W"+str(l+1)] = tf.get_variable("W"+str(l+1), [sizes[l+1], sizes[l]], 
	    		initializer = tf.contrib.layers.xavier_initializer(seed = 1))
	    	self.intercepts_["b"+str(l+1)] = tf.get_variable("b"+str(l+1), [sizes[l+1],1], initializer = tf.zeros_initializer())


	def fit(X, y):

		n_x = X.shape[0]
		n_y = y.shape[0]

		self.create_placeholders(n_x, n_y)
		self.initialize_parameters(n_x, n_y)




