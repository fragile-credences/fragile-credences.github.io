---
layout: post
title: "How much of the fall in fertility could be explained by lower mortality?"
image: /assets/images/ourworldindata_scatter-fertility-vs-infant-survival.png
date: 2021-08-05
tags: economics
---

[owid]: https://ourworldindata.org/child-mortality#when-more-infants-survive-fertility-goes-down

[![](../assets/images/ourworldindata_scatter-fertility-vs-infant-survival.png)][owid]

Many people think that lower child mortality causes fertility to decline.

One prominent theory for this relationship, as described by [Our World in Data][owid][^quote-context], is that "infant survival reduces the parents’ demand for children"[^aside-1]. (Infants are children under 1 years old).

[^quote-context]: The quote in context on Our World in Data's [child mortality page](https://ourworldindata.org/child-mortality#when-more-infants-survive-fertility-goes-down): "the causal link between infant [<1 year old] survival and fertility is established in both directions: Firstly, increasing infant survival reduces the parents’ demand for children. And secondly, a decreasing fertility allows the parents to devote more attention and resources to their children."

[^aside-1]: As an aside, my impression is that if you asked an average educated person "Why do women in developing countries have more children?", their first idea would be: "because child mortality is higher". It's almost a trope, and I feel that it's often mentioned pretty glibly, without actually thinking about the decisions and trade-offs faced by the people concerned. That's just an aside though -- the theory clearly has prima facie plausibility, and is also cited in serious places like academia and Our World in Data. It deserves closer examination.

In this article, I want to look at how we can precisify that theory, and what magnitude the effect could possibly take. What fraction of the decline in birth rates could the theory explain?

**Important.** I don't want to make claims here about how parents *actually* make fertility choices. I only want to examine the implications of various models, and specifically how much of the observed changes in fertility the models could explain.

## Constant number of children
One natural interpretation of "increasing infant survival reduces the parents’ demand for children" is that parents are adjusting the number of births to keep the number of surviving children constant. 

Looking at Our World in Data's graph, we can see that in most of the countries depicted, the infant survival rate went from about 80% to essentially 100%. This is a factor of 1.25. Meanwhile, there were 1/3 as many births. If parents were adjusting the number of births to keep the number of surviving children constant, the decline in infant mortality would explain a change in births by a factor of 1/1.25=0.8, a -0.2 change that is only **30%** of the -2/3 change in births. 

The basic mathematical reason this happens is that even when mortality is tragically high, the survival rate is still thankfully much closer to 1 than to 0, so even a very large proportional fall in mortality will only amount to a small proportional increase in survival.

Some children survive infancy but die later in childhood. Although Our World in Data's quote focuses on infant mortality, it makes sense to consider older children too. I'll look at under-5 mortality, which generally has better data than older age groups, and also captures a large fraction of all child mortality[^over-5-data].

[^over-5-data]:  It should be possible to conduct the Africa analysis for different ages using [IMHE](http://ghdx.healthdata.org/gbd-results-tool)'s more granular data, but it's a bit more work. (There appears to be no direct data on deaths _per birth_ as opposed to per capita, and data on fertility is contained in a different dataset from the main Global Burden of Disease data.)

### England (1861-1951)
England is a country with an early demographic transition and good data available. 

[Doepke 2005] quotes the following numbers:

|                         | 1861    | 1951      |
| ----------------------- | ------- | --------- |
| Infant mortality        | 16%     | 3%        |
| 1-5yo mortality         | 13%     | 0.5%      |
| 0-5 yo mortality        | 27%     | 3.5%      |
| **Survival to 5 years** | **73%** | **96.5%** |
| --------- | ---- | ---- |
| Fertility | 4.9  | 2.1  |

Fertility fell by 57%, while survival to 5 years rose by 32%. Hence, if parents aim to keep the number of surviving children constant, the change in child survival can [explain **43%**](https://docs.google.com/spreadsheets/d/1vsQLOVcay-nYTfEZFVST4yO3NiETo2EoafF5PybGBd4/edit#gid=0&range=D45)[^file] of the actual fall in fertility. (It would have explained only 23% had we erroneously considered only the change in infant survival.)

[^file]: All things decay. Should this Google Sheets spreadsheet become inaccessible, you can download [this `.xlsx` copy](/assets/files/fertility-mortality.xlsx) which is stored together with this blog.

### Sub-Saharan Africa (1990-2017)
If we look now at sub-Saharan Africa data from the World Bank, the 1990-2017 change in fertility is from 6.3 to 4.8, a 25% decrease, whereas the 5-year survival rate went from 0.82 to 0.92, a 12% increase. So the fraction of the actual change in fertility that could be explained by the survival rate is **44%**. (This would have been 23% had we looked only at infant survival).

<iframe width="100%" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vQZrbi2ne3PKflmX_s_3iJ209viIQv23K5Ho5mHUZ8oRMwuf-e2Z2q7kfdX6NQESXtAkBlOqSk3GUzP/pubchart?oid=1122146329&amp;format=interactive"></iframe>
*[Source data and calculations](https://docs.google.com/spreadsheets/d/1vsQLOVcay-nYTfEZFVST4yO3NiETo2EoafF5PybGBd4/edit#gid=0). Chart not showing up? [Go to the `.svg` file.](../assets/images/fertility.svg)*

So far, we have seen that this very simple theory of parental decision-making can explain 30-44% of the decline in fertility, while also noticing that considering childhood mortality beyond infancy was important to giving the theory its full due. 

However, in more sophisticated models of fertility choices, the theory looks worse.

## A more sophisticated model of fertility decisions
Let us imagine that instead of holding it constant, parents treat the number of surviving children as one good among many in an optimization problem.

An increase in the child survival rate can be seen as a decrease in the cost of surviving children. Parents will then substitute away from other goods and increase their target number of surviving children. If your child is less likely to die as an infant, you may decide to aim to have *more* children: the risk of experiencing the loss of a child is lower.[^aside-99]

[^aside-99]: In this light, we can see that the constant model is not really compatible with parents viewing additional surviving children as a (normal) good. Nor of course is it compatible with viewing children as a bad, for then parents would choose to have 0 children. Instead, it could for example be used to represent parents aiming for a socially normative number of surviving children.

For a more formal analysis, we can turn to the [Barro and Becker (1989)](https://www.jstor.org/stable/pdf/1912563.pdf) model of fertility. I'll be giving a simplified version of the presentation in [Doepke 2005].

In this model, parents care about their own consumption as well as their number of surviving children. The parents maximise[^uf]

[^uf]: I collapse Doepke's $$\beta$$ and $$V$$ into a single constant $$V$$, since they can be treated as such in Model A, the only model that I will present mathematically in this post. 

$$U(c,n) = u(c) + n^\epsilon V$$

where 

* $$n$$ is the number of surviving children and $$V$$ is the value of a surviving child
* $$\epsilon$$  is a constant $$\in (0,1)$$
* $$u(c)$$ is the part of utility that depends on consumption[^uc] 

[^uc]: Its actual expression, that I omit from the main presentation for simplicity, is $$u(c)=\frac{c^{1-\sigma}}{1-\sigma}$$, the constant relative risk-aversion utility function.

The income of a parent is $$w$$, and there is a cost per birth of $$p$$ and an additional cost of $$q$$ per surviving child[^aside-2]. The parents choose $$b$$, the number of births. $$s$$ is the probability of survival of a child, so that $$n=sb$$. 

Consumption is therefore $$c=w-(p+qs)b$$ and the problem becomes
$$
\max_{b} U = u(w-(p+qs)b) + (sb)^\epsilon V
$$

[^aside-2]: There is nothing in the model that compels us to call $$p$$ the "cost per birth", this is merely for ease of exposition. The model itself only assumes that there are two periods for each child: in the first period, costing $$p$$ to start, children face a mortality risk; and in the second period, those who survived the first face zero mortality risk and cost $$q$$.

Letting $$b^{*}(s)$$ denote the optimal number of births as a function of $$s$$, what are its properties?

The simplest one is that $$sb^*(s)$$, the number of _surviving_ children, is increasing in $$s$$. This is the substitution effect we described intuitively earlier in this section. This means that if $$s$$ is multiplied by a factor $$x$$ (say 1.25), $$b^*(s)$$ will be multiplied *more than* $$1/x$$ (more than 0.8). 

When we looked at the simplest model, with a constant number of children, we guessed that it could explain 30-44% of the fall in fertility. That number is a **strict upper bound** on what the current model could explain.

What we really want to know, to answer the original question, is how $$b^*(s)$$ itself depends on $$s$$. To do this, we need to get a little bit more into the relative magnitude of the cost per birth $$p$$ and the additional cost $$q$$ per surviving child. As Doepke writes, 

> If a major fraction of the total cost of children accrues for every birth, fertility [i.e. $$b^*(s)$$] would tend to increase with the survival probability; the opposite holds if children are expensive only after surviving infancy[^aside-3].

[^aside-3]: Once again, Doepke calls the model's early period "infancy", but this is not inherent in the model.

This tells us that falling mortality could actually cause fertility to *increase* rather than decrease.[^p_q]

[^p_q]: It's difficult to speculate about the relative magnitude of $$p$$ and $$q$$, especially if, departing from Doepke, we make the early period of the model, say, the first 5 years of life. If the first period is only infancy, it seems plausible to me that $$q \gg p$$, but then we also fail to capture any deaths after infancy. On the other hand, extending the early period to 5 incorrectly assumes that parents get no utility from children before they reach the age of 5.

To go further, we need to plug in actual values for the model parameters. Doepke does this, using numbers that reflect the child mortality situation of England in 1861 and 1951, but also what seem to be some pretty arbitrary assumptions about the parent's preferences (the shape of $$u$$ and the value of $$\epsilon$$). 

With these assumptions, he finds that "the total fertility rate falls from 5.0 (the calibrated target) to 4.2 when mortality rates are lowered to the 1951 level"[^quote-context-2], a 16% decrease. This represents is **28%** of the actually observed fall in fertility to 2.1.

[^quote-context-2]:
	The following additional context may be helpful to understand this quote:
	> The survival parameters are chosen to correspond to the situation in England in 1861 . According to Perston et al. (1972) the infant mortality rate (death rate until first birthday) was $$16 \%$$, while the child mortality rate (death rate between first and fifth birthday) was $$13 \%$$. Accordingly, I set $$s_{i}=0.84$$ and $$s_{y}=0.87$$ in the sequential model, and $$s=s_{i} s_{y}=0.73$$ in the other models. Finally, the altruism factor $$\beta$$ is set in each model to match the total fertility rate, which was $$4.9$$ in 1861 (Chenais 1992). Since fertility choice is discrete in Models B and C, I chose a total fertility rate of $$5.0$$ as the target.
	> 
	>Each model is thus calibrated to reproduce the relationship of fertility and infant and child mortality in 1861 . I now examine how fertility adjusts when mortality rates fall to the level observed in 1951 , which is $$3 \%$$ for infant mortality and $$0.5 \%$$ for child mortality. The results for fertility can be compared to the observed total fertility rate of $$2.1$$ in 1951 .
	>
	>In Model A (Barro-Becker with continuous fertility choice), the total fertility rate falls from $$5.0$$ (the calibrated target) to $$4.2$$ when mortality rates are lowered to the 1951 level. The expected number of surviving children increases from $$3.7$$ to $$4.0$$. Thus, there is a small decline in total fertility, but (as was to be expected given Proposition 1) an increase in the net fertility rate.

### Extensions of Barro-Becker model
The paper then considers various extensions of the basic Barro-Becker model to see if they could explain the large decrease in fertility that we observe. 

For example, it has been hypothesized that when there is _uncertainty_ about whether a child will survive (hitherto absent from the models), parents want to avoid the possibility of ending up with zero surviving children. They therefore have many children as a precautionary measure. Declining mortality (which reduces uncertainty since survival rates are thankfully greater than 0.5) would have a strong negative impacts on births.

However, Doepke also considers a third model, that incorporates not only stochastic mortality but also sequential fertility choice, where parents may condition their fertility decisions on the observed survival of children that were born previously. The sequential aspect reduces the uncertainty that parents face over the number of surviving children they will end up with.

The stochastic and sequential models make no clear-cut predictions based on theory alone. Using the England numbers, however, Doepke finds a robust conclusion. In the stochastic+sequential model, for almost all reasonable parameter values, the expected number of surviving children still increases with $$s$$ (my emphasis):

> To illustrate this point, let us consider the extreme case [where] utility from consumption is close to linear, while risk aversion with regards to the number of surviving children is high. ... [W]hen we move (with the same parameters) to the more realistic sequential model, where parents can replace children who die early, ... despite the high risk aversion with regards to the number of children, total fertility drops only to 4.0, and **net fertility rises** to 3.9, just as with the benchmark parameters. ... Thus, in the sequential setup the conclusion that mortality decline raises net fertility is robust to different preference specifications, even if we deliberately emphasize the precautionary motive for hoarding children.

So even here, the fall in mortality would only explain 35% of the actually observed change in fertility. It seems that the ability to "replace" children who did not survive in the sequential model is enough to make its predictions pretty similar to the simple Barro-Becker model. 

[Doepke 2005]: https://link.springer.com/content/pdf/10.1007/s00148-004-0208-z.pdf
