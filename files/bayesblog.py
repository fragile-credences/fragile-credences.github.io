import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy import integrate
from scipy import optimize
import sys
import time
import decimal

import mpld3
 
###############################
# small normalization constants
###############################
prior = stats.lognorm(s=.5,scale=math.exp(0.5))
likelihood = stats.norm(20,1)

def split_integral(f,splitpoint,integrate_to):
    a,b = -np.inf,np.inf
    if integrate_to < splitpoint:
        # just return the integral normally
        return integrate.quad(f,a,integrate_to)[0]
    else:
        integral_left = integrate.quad(f, a, splitpoint)[0]
        integral_right = integrate.quad(f, splitpoint, integrate_to)[0]
        return integral_left + integral_right

class Posterior_scipyrv(stats.rv_continuous):
	def __init__(self,d1,d2):
		super(Posterior_scipyrv, self).__init__()

		self.d1= d1
		self.d2= d2

		self.normalization_constant = integrate.quad(self.unnormalized_pdf,-np.inf,np.inf)[0]

	def unnormalized_pdf(self,x):
		return self.d1.pdf(x) * self.d2.pdf(x)

	def _pdf(self,x):
		return self.unnormalized_pdf(x)/self.normalization_constant

posterior = Posterior_scipyrv(prior,likelihood)

# print("small normalization constants")
# print('normalization constant:',posterior.normalization_constant)
# print("CDF values:")
# for i in range(30):
# 	print(i,posterior.cdf(i))

###############################
# large inputs into cdf
###############################
prior = stats.lognorm(s=.5,scale=math.exp(0.5))
likelihood = stats.norm(5,.5)

use_split_integral_in_cdf = False
class Posterior_scipyrv(stats.rv_continuous):
	def __init__(self,d1,d2):
		super(Posterior_scipyrv, self).__init__()

		self.d1= d1
		self.d2= d2

		self.splitpoint = (self.d1.expect()+self.d2.expect())/2
		self.normalization_constant = split_integral(self.unnormalized_pdf,self.splitpoint,np.inf)
	
	def unnormalized_pdf(self,x):
		return self.d1.pdf(x) * self.d2.pdf(x)

	def _pdf(self,x):
		return self.unnormalized_pdf(x)/self.normalization_constant

	def _cdf(self,x):
		if use_split_integral_in_cdf:
			return split_integral(self.pdf,self.splitpoint,x)
		else:
			return super(Posterior_scipyrv, self)._cdf(x)

posterior = Posterior_scipyrv(prior,likelihood)

print("large inputs into cdf")
for i in range(30):
	print(i,posterior.cdf(i))

###############################
# Defining support of posterior
##############################
prior = stats.beta(1,1)
likelihood = stats.norm(1,3)

def intersect_intervals(two_tuples):
	d1 , d2 = two_tuples

	d1_left,d1_right = d1[0],d1[1]
	d2_left,d2_right = d2[0],d2[1]

	if d1_right < d2_left or d2_right < d2_left:
		raise ValueError("the distributions have no overlap")
	
	intersect_left,intersect_right = max(d1_left,d2_left),min(d1_right,d2_right)

	return intersect_left,intersect_right

define_support = False
class Posterior_scipyrv(stats.rv_continuous):
	def __init__(self,d1,d2):
		super(Posterior_scipyrv, self).__init__()
		if define_support:
			a1, b1 = d1.support()
			a2,b2 = d2.support()
			self.a , self.b = intersect_intervals([(a1,b1),(a2,b2)])
		

		self.d1= d1
		self.d2= d2

		self.splitpoint = (self.d1.expect()+self.d2.expect())/2
		self.normalization_constant = split_integral(self.unnormalized_pdf,self.splitpoint,self.b)
	
	def unnormalized_pdf(self,x):
		return self.d1.pdf(x) * self.d2.pdf(x)

	def _pdf(self,x):
		return self.unnormalized_pdf(x)/self.normalization_constant

	def _cdf(self,x):
		return split_integral(self.pdf,self.splitpoint,x)
posterior = Posterior_scipyrv(prior,likelihood)

# print("defining support of posterior:")

# print("support:",posterior.support())
# s = time.time()
# print("result:",posterior.ppf(0.99))
# e = time.time()
# print(e-s,'seconds to evalute ppf')

###############################
# Defining support of posterior combined with large inputs to cdf
###############################
prior = stats.beta(1,1)
likelihood = stats.norm(1,3)

class Posterior_scipyrv(stats.rv_continuous):
	def __init__(self,d1,d2):
		super(Posterior_scipyrv, self).__init__()
		self.d1= d1
		self.d2= d2

		self.normalization_constant = integrate.quad(self.unnormalized_pdf,-np.inf,np.inf)[0]
	
	def unnormalized_pdf(self,x):
		return self.d1.pdf(x) * self.d2.pdf(x)

	def _pdf(self,x):
		return self.unnormalized_pdf(x)/self.normalization_constant

posterior = Posterior_scipyrv(prior,likelihood)

# print("support of posterior combined with large inputs to cdf")
# print("cdf values:")
# for i in range(20):
# 	print(i/5,posterior.cdf(i/5))
# print("try to compute ppf")
# print(posterior.ppf(0.5))

###############################
# cdf memoization
###############################
prior = stats.lognorm(s=.5,scale=math.exp(0.5))
likelihood = stats.norm(5,1)
memoization = True
class Posterior_scipyrv(stats.rv_continuous):
	def __init__(self,d1,d2):
		super(Posterior_scipyrv, self).__init__()
		
		self.cdf_lookup = {}

		a1, b1 = d1.support()
		a2,b2 = d2.support()
		self.a , self.b = intersect_intervals([(a1,b1),(a2,b2)])
		
		self.d1= d1
		self.d2= d2

		self.splitpoint = (self.d1.expect()+self.d2.expect())/2
		self.normalization_constant = split_integral(self.unnormalized_pdf,self.splitpoint,self.b)
	
	def unnormalized_pdf(self,x):
		return self.d1.pdf(x) * self.d2.pdf(x)

	def _pdf(self,x):
		return self.unnormalized_pdf(x)/self.normalization_constant

	def _cdf(self,x):
		if memoization:
			# Memeoization: exploit considering the cdf to be 1 forevermore once it reaches values close to 1
			for x_lookup in self.cdf_lookup:
				if x_lookup < x and np.around(self.cdf_lookup[x_lookup],5)==1.0:
					return 1

			# Memeoization for any input: check lookup table for largest integral already computed below x. only
			# integrate the remaining bit.
			# Same number of integrations, but the integrations are over a much smaller interval.
			sortedkeys = sorted(self.cdf_lookup ,reverse=True)
			for key in sortedkeys:
				#find the greatest key less than x
				if key<x:
					ret = self.cdf_lookup[key]+integrate.quad(self.pdf,key,x)[0]
					self.cdf_lookup[float(x)] = ret
					return ret
		
		# Initial run
		ret = split_integral(self.pdf,self.splitpoint,x)
		if memoization:
			self.cdf_lookup[float(x)] = ret
		return ret
posterior = Posterior_scipyrv(prior,likelihood)


percentiles_short = [0.1, 0.9, 0.25, 0.75, 0.5]

# print("Memeoization")
# print("memoization",memoization)
# s = time.time()
# print(posterior.ppf(percentiles_short))
# print("length of lookup table:",len(posterior.cdf_lookup))
# e = time.time()
# print(e-s,'seconds to evalute ppf')

###############################
# ppf with bounds
###############################
prior = stats.lognorm(s=.5,scale=math.exp(0.5))
likelihood = stats.norm(5,1)
bounds = True
class Posterior_scipyrv(stats.rv_continuous):
	def __init__(self,d1,d2):
		super(Posterior_scipyrv, self).__init__()

		a1, b1 = d1.support()
		a2,b2 = d2.support()
		self.a , self.b = intersect_intervals([(a1,b1),(a2,b2)])

		self.d1= d1
		self.d2= d2

		self.splitpoint = (self.d1.expect()+self.d2.expect())/2
		self.normalization_constant = split_integral(self.unnormalized_pdf,self.splitpoint,self.b)
	
	def unnormalized_pdf(self,x):
		return self.d1.pdf(x) * self.d2.pdf(x)

	def _pdf(self,x):
		return self.unnormalized_pdf(x)/self.normalization_constant

	def _cdf(self,x):
		return split_integral(self.pdf,self.splitpoint,x)

	def ppf_with_bounds(self, q, leftbound, rightbound):
		'''
		wraps scipy ppf function
		https://github.com/scipy/scipy/blob/4c0fd79391e3b2ec2738bf85bb5dab366dcd12e4/scipy/stats/_distn_infrastructure.py#L1681-L1699
		'''

		factor = 10.
		left, right = self._get_support()

		if np.isinf(left):
			left = min(-factor, right)
			while self._ppf_to_solve(left, q) > 0.:
				left, right = left * factor, left
		# left is now such that cdf(left) <= q
		# if right has changed, then cdf(right) > q

		if np.isinf(right):
			right = max(factor, left)
			while self._ppf_to_solve(right, q) < 0.:
				left, right = right, right * factor
		# right is now such that cdf(right) >= q

		if leftbound is not None:
			left = leftbound
		if rightbound is not None:
			right = rightbound

		root,rootinfo = optimize.brentq(self._ppf_to_solve,left, right, args=q, xtol=self.xtol, full_output=True)
		print("brentq looked between",np.around(left,2),np.around(right,2),"and took",rootinfo.iterations,"iterations")
		return root

	def compute_percentiles(self, percentiles_list):
		result = {}
		percentiles_list.sort()
		percentiles_reordered = sum(zip(percentiles_list,reversed(percentiles_list)), ())[:len(percentiles_list)] #https://stackoverflow.com/a/17436999/8010877

		def get_bounds(dict, p):
			keys = list(dict.keys())
			keys.append(p)
			keys.sort()
			i = keys.index(p)
			if i != 0:
				leftbound = dict[keys[i - 1]]
			else:
				leftbound = None
			if i != len(keys) - 1:
				rightbound = dict[keys[i + 1]]
			else:
				rightbound = None
			return leftbound, rightbound

		for p in percentiles_reordered:
			if bounds:
				leftbound , rightbound = get_bounds(result,p)
			else:
				leftbound,rightbound = None,None
			res = self.ppf_with_bounds(p,leftbound,rightbound)
			result[p] = res

		sorted_result = {key:value for key,value in sorted(result.items())}
		return sorted_result

scale = math.exp(1)
s = 1

prior = stats.norm(1,1)
likelihood = stats.lognorm(scale=scale,s=s)
posterior = Posterior_scipyrv(prior,likelihood)

percentiles_short = [0.1, 0.9, 0.25, 0.75, 0.5]
percentiles_long = [i/100 for i in range(50)]

# print("Using ppf bounds?",bounds)
# s=time.time()
# posterior.compute_percentiles(percentiles_short)
# e = time.time()
# print("total time to compute percentiles:",e-s,'seconds')
