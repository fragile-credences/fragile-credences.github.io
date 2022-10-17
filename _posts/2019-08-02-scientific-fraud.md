---
layout: post
title: "Why scientific fraud is hard to catch"
tags: science
---

It's nearly impossible to catch a scientific fraudster if they're halfway competent. 

Uri Simonsohn has become a minor nerd celeb by exposing fraudulent academic scientists who used fabricated data to get published. The Atlantic called him "the data vigilante". I'll describe two simple statistical techniques he has used -- and why I'm pessimistic about the impact of such techniques.

If a parameter is measured with many significant digits, the last digit should be distributed uniformly 0-9. In a study of an intervention to increase factory workers' use of hand sanitizer, sanitizer use was measured with a scale sensitive to the 100th of a gram. But the data had an unusual prevalence of 6s, 7s and 9s on the last digit. Uri Simonsohn and colleagues conducted a chi-square test and reject the hypothesis that the digits follow a uniform distribution, p=0.00000000000000001.[^uri]

[^uri]: [http://datacolada.org/74](http://datacolada.org/74), Figure 2

A second sign of fraudulent data is if the baseline means are too similar between treatment groups. In one of the hand sanitizer studies, there were 40 participants, 20 in the control condition and 20 in the treatment condition. Simonsohn used a "bootstrapping" technique -- randomly shuffling the 40 observations into two groups of 20, and repeating this millions of times, in order to estimate how often we would see such similar means if the data were truly drawn randomly (less than once in a 100,000)[^uri2]. 

[^uri2]: [http://datacolada.org/74](http://datacolada.org/74), Problem 4

There are other, more mathematically intense techniques for forensic data analysis[^other], but the common theme among them is to detect fraudsters creating suspiciously non-random data. 

I want to tell these hand sanitizer people: come on, how hard can it be to use a random number generator? We know people are bad at producing randomness. In poker, it's often optimal to play a mixed strategy, which requires randomising your play. But we have a strong natural tendency to play non-randomly, so poker players have developed ad hoc randomisation devices, like looking at your watch and playing call if you're in the first half of the minute and fold if you're in the second half. A similar incapacity to produce enough randomness seems to have befallen these amateurish scientific fakers. In order to produce data that violates the last-digit-uniformity law, you have to literally be writing the fake numbers by hand into a computer!

Savvier baddies would not shoot themselves in the foot in this way. It's very easy to just draw some random numbers from a pre-specified distribution.

I can imagine that as you run more complex experiments, with multiple treatment arms and many potentially correlated parameters, it becomes difficult to create realistic fake data, even if you randomly draw it from a distribution. Some inconsistency could always escape your notice, and a sufficiently determined data sleuth might catch you.

But there's a much easier solution: just run a legitimate experiment, and then add a constant of your choice to all observations in the treatment group. This data would look exactly like the real thing -- the only lie would be that the "treatment" was you logging on to the computer in the middle of the night and changing the numbers. I can't think of any way this misconduct could be detected statistically. And it has the additional benefit that you're running an experiment, so people in your department won't be wondering where you're getting all that data from.

Statistical sleuthing is fun, but I suspect it's powerless against the majority of fraud. 

My broader hope is that we'll see a rise in the norm of having multiple independent replications of a study. This single tide should wash away many of the problems with current science. If a study fails to replicate multiple times, the result will lose credibility -- even if we never find out whether it was due to outright fraud or merely flawed science.

[^other]: see the "fake data" [category](http://datacolada.org/archives/category/fake-data) of Simonsohn's blog Data Colada, which by the way is excellent on many topics besides fraud.

