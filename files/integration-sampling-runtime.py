import math
from scipy import stats
from scipy import integrate
import numpy as np
import time


# Normalization constant
prior = stats.lognorm(scale=math.exp(1),s=4)
likelihood = stats.norm(loc=5,scale=2)
def unnormalized_posterior_pdf(x):
	return prior.pdf(x)*likelihood.pdf(x)
start = time.time()
normalization_constant = integrate.quad(unnormalized_posterior_pdf,-np.inf,np.inf)[0]
end = time.time()
print('Compute normalization_constant:')
print(1000*(end-start),'milliseconds')


# Sampling
def is_a_distribution(obj):
	if issubclass(type(obj),stats.rv_continuous):
		return True
	if isinstance(obj,stats._distn_infrastructure.rv_frozen):
		return True
	return False

class Product_pdf(stats.rv_continuous):
	def __init__(self,d1,d2):
		super(Product_pdf,self).__init__()
		if not is_a_distribution(d1):
			raise TypeError("First argument must be a distribution")
		if type(d2) is not float and type(d2) is not int and not is_a_distribution(d2):
			raise TypeError("Second argument must be a distribution or a number")
		self.d1= d1
		self.d2= d2
	def _pdf(self,x):
		if type(self.d2) is float:
			ret = self.d1.pdf(x)*self.d2
		if type(self.d2) is stats._distn_infrastructure.rv_frozen:
			ret = self.d1.pdf(x)*self.d2.pdf(x)
		return ret

def normalize(distr):
	integral = integrate.quad(distr.pdf,-np.inf,np.inf)[0]
	ret = Product_pdf(distr,1/integral)
	return ret

def update(prior,likelihood):
	unnormalized_posterior = Product_pdf(prior,likelihood)
	posterior = normalize(unnormalized_posterior)
	return posterior

n = 1
posterior = update(prior,likelihood)
start = time.time()
posterior.rvs(size=n)
end = time.time()
print('Get',n,' sample(s) from posterior:')
print(1000*(end-start),'milliseconds')

n = 10000
start = time.time()
x = prior.rvs(size=n)
end = time.time()
print('Get',n,'sample(s) from prior:')
print(1000*(end-start),'milliseconds')

import emcee

ndim, nwalkers, nruns = 1, 20, 500
list = stats.halfnorm.rvs(size=nwalkers)
p0 = []
for item in list:
	p0.append([item])
p0 = np.array(p0)

start = time.time()
def log_prob(x):
	if posterior.pdf(x)>0:
		return math.log(posterior.pdf(x))
	else:
		return -np.inf
sampler = emcee.EnsembleSampler(nwalkers, 1, log_prob)
sampler.run_mcmc(p0, nruns)
samples = sampler.get_chain(flat=True)[:, 0]
end = time.time()
print(nwalkers*nruns,'samples from posterior using emcee')
print(1000*(end-start),'milliseconds')

from matplotlib import pyplot as plt
plt.hist(samples)
plt.show()