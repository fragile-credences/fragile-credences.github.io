---
layout: post
title: "Eliciting probability distributions from quantiles"
image: /assets/images/quantiles/metalog.png
tags: software probability
---

We often have intuitions about the probability distribution of a variable that we would like to translate into a formal specification of a distribution. Transforming our beliefs into a fully specified probability distribution allows us to further manipulate the distribution in useful ways.

For example, you believe that the cost of a medication is a positive number that's about 10, but with a long right tail: say, a 10% probability of being more than 100. To use this cost estimate in a Monte Carlo simulation, you need to know exactly what distribution to plug in. Or perhaps you have a prior about the effect of creatine on cognitive performance, and you want to formally [update that prior using Bayes' rule](http://bayesupdate.com/) when a new study comes out. Or you want to make a forecast about a candidate's share of the vote and evaluate the accuracy of your forecast using a [scoring rule](https://en.wikipedia.org/wiki/Scoring_rule).

In most software, you have to specify a distribution by its parameters, but these parameters are rarely intuitive. The normal distribution's mean and standard deviation are somewhat intuitive, but this is the exception rather than the rule. The lognormal's mu and sigma correspond to the mean and standard deviation of the variable's _logarithm_, something I personally have no intuitions about. And I don't expect good results if you ask someone to supply a beta distribution's alpha and beta shape parameters.

I have built a tool that creates a probability distribution (of a given family) from user-supplied _quantiles_, sometimes also called percentiles. Quantiles are points on the cumulative distribution function: $$(p,x)$$ pairs such that $$P(X<x)=p$$. To illustrate what quantiles are, we can look at the example distribution below, which has a 50th percentile (or median) of -1 and a 90th percentile of 10. 

<img src="/assets/images/quantiles/quantiles-example.png" width="50%">  
_A cumulative distribution function with a median of -1 and a 90th percentile of 10_

The [code is on GitHub](https://github.com/tadamcz/make-distribution), and the webapp is [here](http://makedistribution.com).

Let's run through some examples of how you can use this tool. At the end, I will discuss how it compares to other probability elicitation software, and why I think it's a valuable addition.

# Traditional distributions
The tool supports the normal and lognormal distributions, and more of the usual distribution families could easily be added. The user supplies the distribution family, along with an arbitrary number of quantiles. If more quantiles are provided than the distribution has parameters (more than two in this case), the system is over-determined. The tool then uses least squares to find the best fit.

This is some example input:
```python
family = 'lognormal'
quantiles = [(0.1,50),(0.5,70),(0.75,100),(0.9,150)]
```
And the corresponding output:
```text
More than two quantiles provided, using least squares fit

Lognormal distribution
mu 4.313122980928514
sigma 0.409687416531683

quantiles:
0.01 28.79055927521217
0.1 44.17183774344628
0.25 56.64439363937313
0.5 74.67332855521319
0.75 98.44056294458953
0.9 126.2366766332274
0.99 193.67827989071688
```
<img src="/assets/images/quantiles/lognormal.png" width="70%"/>

# Metalog distribution

The feature I am most excited about, however, is the support for a new type of distribution developed specifically for the purposes of flexible elicitation from quantiles, called the meta-logistic distribution. It was first described in [Keelin 2016](http://www.metalogdistributions.com/images/quantiles/The_Metalog_Distributions_-_Keelin_2016.pdf), which puts it at the cutting edge compared to the venerable normal distribution invented by Gauss and Laplace around 1810. The meta-logistic, or metalog for short, does not use traditional parameters. Instead, it can take on as many terms as the user provides quantiles, and adopts whatever shape is needed to fit these quantiles very closely. Closed-form expressions exist for its quantile function (the inverse of the CDF) and for its PDF. This leads to attractive computational properties (see footnote)[^computational].

[^computational]:
    For the quantile function expression, see [Keelin 2016](http://www.metalogdistributions.com/images/quantiles/The_Metalog_Distributions_-_Keelin_2016.pdf), definition 1. The fact that this is in closed form means, first, that sampling randomly from the distribution is computationally trivial. We can use the inverse transform method: we take random samples from a uniform distribution over $$[0,1]$$ and plug them into the quantile function. Second, plotting the CDF for a certain range of probabilities (e.g. from 1% to 99%) is also easy.
    
    The expression for the PDF is unusual in that it is a function of the cumulative probability $$p \in (0,1)$$, instead of a function of values of the random variable. See [Keelin 2016](http://www.metalogdistributions.com/images/quantiles/The_Metalog_Distributions_-_Keelin_2016.pdf), definition 2. As Keelin explains (p. 254), to plot the PDF as is customary we can use the quantile function $$q(p)$$ on the horizontal axis and the PDF expression $$f(p)$$ on the vertical axis, and vary $$p$$ in, for example, $$[0.01,0.99]$$ to produce the corresponding values on both axes.

    Hence, for (i) querying the quantile function of the fitted metalog, sampling, and plotting the CDF, and (ii) plotting the PDF, everything can be done in closed form.

    To query the CDF, however, numerical equation solving is applied. Since the quantile function is differentiable, Newton's method can be applied and is fast. (Numerical equation solving is also used to query the PDF as a function of values of the random variable -- but I don't see why one would need densities except for plotting.)

Keelin explains that
> [t]he metalog distributions provide a convenient way to translate CDF data into smooth, continuous, closed-from distribution functions that can be used for real-time feedback to experts about the implications of their probability assessments. 

The metalog quantile function is derived by modifying the logistic quantile function,

$$
\mu + s \ln{\frac{y}{1-y}} \quad\text{ for } 0 < y < 1
$$

by letting $$\mu$$ and $$s$$ depend on $$y$$ instead of being constant. 

As Keelin writes, given a systematically increasing $$s$$ as one moves from left to right, a right skewed distribution would result. And a systematically decreasing $$\mu$$ as one moves from left to right would make the distribution spikier in the middle with correspondingly heavier tails.

By modifying $$s$$ and $$\mu$$ in ever more complex ways we can make the metalog take on almost any shape. In particular, in most cases the metalog CDF passes through all the provided quantiles exactly[^feasibility]. Moreover, we can specify the metalog to be unbounded, to have arbitrary bounds, or to be semi-bounded above or below.

[^feasibility]:
    In most cases, there exists a metalog whose CDF passes through all the provided quantiles exactly. In that case, there exists an expression of the metalog parameters that is in closed form as a function of the quantiles ("$$a = Y^{−1}x$$", [Keelin 2016](http://www.metalogdistributions.com/images/quantiles/The_Metalog_Distributions_-_Keelin_2016.pdf), p. 253. Keelin denotes the metalog parameters $$a$$, the matrix $$Y$$ is a simple function of the quantiles' y-coordinates, and the vector $$x$$ contains the quantiles' x-coordinates. The metalog parameters $$a$$ are the numbers that are used to modify the logistic quantile function. This modification is done according to equation 6 on p. 254.) 

    If there is no metalog that fits the quantiles exactly (i.e. the expression for $$a$$ above does not imply a valid probability distribution), we have to use optimization to find the feasible metalog that fits the quantiles most closely. In this software implementation, "most closely" is defined as minimizing the absolute differences between the quantiles and the CDF (see [here](https://github.com/isaacfab/rmetalog/issues/13) for more discussion).

    In my experience, if a small number of quantiles describing a PDF with sharp peaks are provided, the closest feasible metalog fit to the quantiles may not pass through all the quantiles exactly. 

Instead of thinking about which of several highly constraining distribution families to use, just choose the metalog and let your quantiles speak for themselves. As Keelin says:

> one needs a distribution that has flexibility far beyond that of traditional distributions -- one that enables “the data to speak for itself” in contrast to imposing unexamined and possibly inappropriate shape constraints on that data.


For example, we can fit an unbounded metalog to the same quantiles as above:
```python
family = 'metalog'
quantiles = [(0.1,50),(0.5,70),(0.75,100),(0.9,150)]
metalog_leftbound = None
metalog_rightbound = None
```

```text
Meta-logistic distribution

quantiles:
0.01 11.968367580205552
0.1 50.000000000008185
0.25 58.750000000005215
0.5 70.0
0.75 100.00000000000519
0.9 150.00000000002515
0.99 281.7443263650518
```
<img src="/assets/images/quantiles/metalog.png" width="70%"/>

The metalog's actual parameters (as opposed to the user-supplied quantiles) have no simple interpretation and are of no use unless the next piece of software you're going to use knows what a metalog is. Therefore the program doesn't return the parameters. Instead, if we want to manipulate this distribution, we can use the expressions of the PDF and CDF that the software provides, or alternatively export a large number of samples into another tool that accepts distributions described by a list of samples (such as the Monte Carlo simulation tool [Guesstimate](https://getguesstimate.com)). By default, 5000 samples will be printed; you can copy and paste them.


# Approaches to elicitation
How does this tool compare to other approaches for creating subjective belief distributions? Here are the strategies I've seen.

## Belief intervals
The first approach is to provide a belief interval that is mapped to some fixed quantiles, e.g. a 90% belief interval (between the 0.05 and 0.95 quantile) like on [Guesstimate](http://getguesstimate.com). [Metaculus](http://metaculus.com) provides a graphical way to input the same data, allowing the user to drag the quantiles across a line under a graph of the PDF. This is the simplest and most user-friendly approach. The tool I built incorporates the belief interval approach while going beyond it in two ways. First, you can provide completely arbitrary quantiles, instead of specifically the 0.05 and 0.95 -- or some other belief interval symmetric around 0.5. Second, you can provide more than two quantiles, which allows the user to query intuitive information about more parts of the distribution. 

<img src="/assets/images/quantiles/guesstimate.png">  
_Guesstimate_

<img src="/assets/images/quantiles/metaculus.png" width="70%">  
_Metaculus_

## Drawing
Another option is to draw the PDF on a canvas, in free form, using your mouse. This is the very innovative approach of [probability.dev](http://probability.dev).[^canvas]

<img src="/assets/images/quantiles/dev.png">  
_probability.dev_

## Ought's elicit
Ought's [elicit](https://elicit.ought.org) lets you provide quantiles like my tool, or equivalently bins with some probability mass in each bin[^b]. The resulting distribution is by default piecewise uniform (the cdf is piecewise linear), but it's possible to apply smoothing. It has all the features I want, the drawback is that it only supports bounded distributions[^elicit].

[^b]: To provide quantiles, simply leave the Min field empty -- it defaults to the left bound of the distribution.


<img src="/assets/images/quantiles/ought.png">  
_Elicit_

[^canvas]: Drawing the PDF instead of the CDF makes it difficult to hit quantiles. But drawing the CDF would probably be less intuitive -- I often have the rough shape of the PDF in mind, but I never have intuitions about the rough shape of the CDF. The canvas-based approach also runs into difficulty with the tail of unbounded distributions. Overall I think it's very cool but I haven't found it that practical.
[^elicit]: I suspect this is a fundamental problem of the approach of starting with piecewise uniforms and adding smoothing. You need the tails of the CDF to asymptote towards 0 and 1, but it's hard to find a mathematical function that does this while also (i) having the right probability mass under the tail (ii) stitching onto the piecewise uniforms in a natural way. I'd love to be proven wrong, though; the user interface and user experience on Elicit are really nice. (I'm aware that Elicit allows for 'open-ended' distributions, where probability mass can be assigned to an out-of-bounds outcome, but one cannot specify how that mass is distributed inside the out-of-bounds interval(s). So there is no true support for unbounded distributions. The 'out-of-bounds' feature exists because Elicit seems to be mainly intended as an add-on to Metaculus, which supports such 'open-ended' distributions but no truly unbounded ones.)

## Mixtures
A meta-level approach that can be applied to any of the above is to allow the user to specify a mixture distribution, a weighted average of distributions. For example, 1/3 weight on a `normal(5,5)` and 2/3 weight on a `lognormal(1,0.75)`. My opinion on mixtures is that they are good if the user is thinking about the event disjunctively; for example, she may be envisioning two possible scenarios, each of which she has a distribution in mind for. But on Metaculus and Foretold my impression is that mixtures are often used to indirectly achieve a single distribution whose rough shape the user had in mind originally.

# The future
This is an exciting space with many recent developments. Guesstimate, Metaculus, Elicit and the metalog distribution have all been created in the last 5 years.