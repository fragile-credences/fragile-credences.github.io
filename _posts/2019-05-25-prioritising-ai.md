---
title: "A shift in arguments for AI risk"
layout: post
tags: ["existential risk"]
---

Different arguments have been made for prioritising AI. In _Superintelligence_, we find a detailed argument with three features: (i) the alignment problem as the source of AI risk, (ii) the hypothesis that there will be a sharp, discontinuous jump in AI capabilities, and (iii) the resulting conclusion that an existential catastrophe is likely. Arguments that abandon some of these features have recently become prominent. Christiano and Grace drop the discontinuity hypothesis, but keep the focus on alignment. Even under more gradual scenarios, they argue, misaligned AI could cause human values to lose control of the future.  Moreover, others have proposed AI risks that are unrelated to the alignment problem: for example, the risk that AI might be misused or could make war between great powers more likely. It would be beneficial to clarify which arguments actually motivate people who prioritise AI.[^ack]

[^ack]: This post was written in February 2019 while at the Governance of AI Programme, within the Future of Humanity Institute. I'm publishing it as it stood in February, since I'm starting a new job and anticipate I won't have time to update it. I thank Markus Anderljung, Max Daniel, Jeffrey Ding, Eric Drexler, Carrick Flynn, Richard Ngo, Cullen O'Keefe, Stefan Schubert, Rohin Shah, Toby Shevlane, Matt van der Merwe and Remco Zwetsloot for help with previous versions of this document. Ben Garfinkel was especially generous with his time and many of the ideas in this document were originally his.

# Long summary

Many people now work on ensuring that advanced AI has beneficial consequences. But members of this community have made several quite different arguments for prioritising AI.

Early arguments, and in particular _Superintelligence_, identified the “alignment problem” as the key source of AI risk. In addition, the book relies on the hypothesis that superintelligent AI is likely to emerge through a discontinuous jump in the capabilities of an AI system, rather than through gradual progress. This premise is crucial to the argument that a single AI system could gain a “decisive strategic advantage”, that the alignment problem cannot be solved through trial and error, and that there is likely to be a “treacherous turn”. Hence, the discontinuity hypothesis underlies the book’s conclusion that existential catastrophe is a likely outcome. 

The argument in _Superintelligence_ combines three features: (i) a focus on the alignment problem, (ii) the discontinuity hypothesis, and (iii) the resulting conclusion that an existential catastrophe is likely. 

Arguments that abandon some of these features have recently become prominent. They also generally tend to have been made in less detail than the early arguments.

One line of argument, promoted by Paul Christiano and Katja Grace, drops the discontinuity hypothesis, but continues to view the alignment problem as the source of AI risk. Even under more gradual scenarios, they argue that, unless we solve the alignment problem before advanced AIs are widely deployed in the economy, these AIs will cause human values to eventually fade from prominence. They appear to be agonistic about whether these harms would warrant the label “existential risk”.

Moreover, others have proposed AI risks that are unrelated to the alignment problem. I discuss three of these: (i) the risk that AI might be misused, (ii) that it could make war between great powers more likely, and (iii) that it might lead to value erosion from competition. These arguments don’t crucially rely on a discontinuity, and the risks are rarely existential in scale.

It’s not always clear which of the arguments actually motivates members of the beneficial AI community. It would be useful to clarify which of these arguments (or yet other arguments) are crucial for which people. This could help with evaluating the strength of the case for prioritising AI, deciding which strategies to pursue within AI, and avoiding costly misunderstanding with sympathetic outsiders or sceptics.

# Contents
{: .no_toc}
1. toc
{:toc}


# Early arguments: the alignment problem and discontinuity hypotheses

## Concerns about AI before _Superintelligence_

Since the early days of the field of AI, people have expressed scattered concerns that AI might have a large-scale negative impact. In a 1959 lecture, _Speculations on Perceptrons and other Automata_, I.J. Good wrote that 

> whether \[an intelligence explosion[^1]\] will lead to a Utopia or to the extermination of the human race will depend on how the problem is handled by the machines. The important thing will be to give them the aim of serving human beings.

Around the turn of the millennium, related concerns were being gestured at in Ray Kurzweil’s _The Age of Spiritual Machines_ (1999) and in a popular essay by Bill Joy, _Why the Future Doesn't Need Us_ (2000). These concerns did not directly draw on I.J. Good's concept of an intelligence explosion, but did suggest that progress in artificial intelligence could ultimately lead to human extinction. Joy's emphasizes the idea that AI systems "would compete vigorously among themselves for matter, energy, and space," suggesting this may cause their prices to rise "beyond human reach" and therefore causing biological humans to be "squeezed out of existence."

As early as 1997, in _How long before superintelligence?_, Nick Bostrom highlighted the need to suitably “arrange the motivation systems of [....] superintelligences”. In 2000, Eliezer Yudkowsky co-founded the Machine Intelligence Research Institute (MIRI), then named Singularity institute, with [the goal](https://web.archive.org/web/20060703223530/http://www.singinst.org/why-singularity.html) of "sparking the Singularity" by creating a "transhuman AI." From its inception, MIRI [emphasized](https://web.archive.org/web/20060806061855/http://www.singinst.org/friendly/whatis.html) the importance of ensuring that advanced AI systems are "Friendly," in the sense of being "beneficial to humans and humanity." Over the following decade, MIRI's aims shifted away from building the first superintelligent AI system and toward ensuring that the first such system -- no matter who it is built by -- will be beneficial to humanity. In a series of essays, Yudkowsky produced the first extensive body of writing describing what is now known as the _alignment problem_: the problem of building powerful AI systems which reliably try to do what their operators want them to do. He argued that superintelligent AI is likely to come very suddenly, in a single event that leaves humans powerless; if we haven’t already solved the alignment problem by that time, the AI will cause an existential catastrophe.

In _Facing the Intelligence Explosion_ (2013), Luke Muehlhauser, a former executive director of MIRI, gave a succinct account of this concern:


> AI leads to intelligence explosion, and, because we don’t know how to give an AI benevolent goals, by default an intelligence explosion will optimize the world for accidentally disastrous ends. A controlled intelligence explosion, on the other hand, could optimize the world for good.

The intelligence explosion, where an AI rapidly and recursively self-improves to become superintelligent, features prominently in this picture. For this essay I find useful the broader notion of a _discontinuity_ in AI capabilities. I’ll define a discontinuity as an improvement in the capabilities of powerful AI that happens much more quickly than what would be expected based on extrapolating past progress. (I further disambiguate this term in the appendix). An intelligence explosion is clearly sufficient, but isn’t necessary for there to be a discontinuity.

In Yudkowsky’s _Artificial Intelligence as a Positive and Negative Factor in Global Risk_ (2008), he expands on the importance of discontinuities to his argument: 


> From the standpoint of existential risk, one of the most critical points about Artificial Intelligence is that an Artificial Intelligence might increase in intelligence extremely fast. [...]
>
>
>The possibility of sharp jumps in intelligence [...] implies a higher standard for Friendly AI techniques. The technique cannot assume the programmers’ ability to monitor the AI against its will, rewrite the AI against its will, bring to bear the threat of superior military force; nor may the algorithm assume that the programmers control a “reward button” which a smarter AI could wrest from the programmers; et cetera.[^3] 


## Bostrom’s _Superintelligence_

_Superintelligence_ remains by far the most detailed treatment of the issue, and came to be viewed by many as the canonical statement of the case for prioritising AI. It retains some of the key features of the earlier writing by Bostrom, Yudkowsky, and Muehlhauser.

In particular, in the book we find:

* the alignment problem as the key source of AI risk
* discontinuities in AI trajectories as a premise[^5] for the argument that:
    * 1) a single AI system could gain a decisive strategic advantage[^4]
    * 2) we cannot use trial and error to ensure that this AI is aligned
    * 3) the treacherous turn will make it much more difficult to react
* the resulting conclusion that an existential catastrophe is likely

If a decisive strategic advantage were gained by an AI that is not aligned with human values, the result would likely be human extinction:


>Taken together, these three points \[decisive strategic advantage, the orthogonality thesis, and instrumental convergence\] thus indicate that the first superintelligence may shape the future of Earth-originating life, could easily have non-anthropomorphic final goals, and would likely have instrumental reasons to pursue open-ended resource acquisition. If we now reflect that human beings consist of useful resources (such as conveniently located atoms) and that we depend for our survival and flourishing on many more local resources, we can see that the outcome could easily be one in which humanity quickly becomes extinct. (Chapter 8).

Let us now turn to the three ways in which the discontinuity hypothesis is a crucial premise in the argument. 


### How a single AI system could obtain a decisive strategic advantage

It is the discontinuity hypothesis that enables Bostrom to argue that a single AI system will gain a decisive strategic advantage, over humans and other AI systems.

If there is no discontinuity, the AI frontrunner is unlikely to obtain far more powerful capabilities than its competitors. The first system that could be deemed superintelligent will emerge in a world populated by only slightly less powerful systems. On the other hand, if an AI system does make discontinuous progress, this progress would put it head and shoulders above the competition, and it could even gain a decisive strategic advantage.

Bostrom’s analysis of AI trajectories focuses on “takeoff”, the time between the “human-level general intelligence” and “radical superintelligence”. A “fast take-off” is one that occurs over as minutes, hours, or days. Bostrom argues that “if and when a takeoff occurs, it will likely be explosive.”[^takeoffargument]

[^takeoffargument]: Bostrom gives detailed arguments for this claim in chapter 4, "the kinetics of an intelligence explosion". I don't discuss these arguments because they are incidental to this post.

Notice that my definition of a discontinuity in AI capabilities does not exactly coincide with that of a “fast take-off”. This difference, which I explain in more detail in the appendix, is sometimes important. In Chapter 5, Bostrom writes that the frontrunner could “attain a decisive strategic advantage even if the takeoff is not fast”. However, he justifies this with reference to a scenario that involves a strong discontinuity[^6].


### The impossibility of alignment by trial and error

The discontinuity removes the option of using trial and error to solve the alignment problem. The technical problem of aligning an AI with human interests remains regardless of the speed of AI development[^7]. But if AI systems are developed more slowly, one might expect these problems to be solved by trial and error as the AI gains in capability and begins to cause real-world accidents. In a continuous scenario, AI remains at the same level of capability long enough for us to gain experience with deployed systems of that level, witness small accidents, and fix any misalignment. The slower the scenario, the easier it is to do this. In a moderately discontinuous scenario, there could be accidents that kill thousands of people. But it seems to me that a very strong discontinuity would be needed to get a single moment in which the AI causes an existential catastrophe. 


### The treacherous turn

A key concept in Bostrom’s argument is that of the treacherous turn:


>_The treacherous turn_—While weak, an AI behaves cooperatively (increasingly so, as it gets smarter). When the AI gets sufficiently strong—without warning or provocation—it strikes, forms a singleton[^8], and begins directly to optimize the world according to the criteria implied by its final values.

The treacherous turn implies that:



* the AI might gain a decisive strategic advantage without anyone noticing
* the AI might hide the fact that it is misaligned

Bostrom explains that: 


>\[A\]n unfriendly AI of sufficient intelligence realizes that its unfriendly final goals will be best realized if it behaves in a friendly manner initially, so that it will be let out of the box. [...] At some point, an unfriendly AI may become smart enough to realize that it is better off concealing some of its capability gains. It may underreport on its progress and deliberately flunk some of the harder tests, in order to avoid causing alarm before it has grown strong enough to attain a decisive strategic advantage. The programmers may try to guard against this possibility by secretly monitoring the AI’s source code and the internal workings of its mind; but a smart-enough AI would realize that it might be under surveillance and adjust its thinking accordingly.

In these scenarios, Bostrom is imagining an AI with the ability for very sophisticated deception. Crucially, the AI goes from being genuinely innocuous to being a cunning deceiver without passing through any intermediate steps: there are no small-scale accidents that could reveal the AI’s misaligned goals, nor does the AI ever make a botched attempt at deception that other actors can discover. This relies on the hypothesis of a very strong discontinuity in the AI’s abilities. The more continuous the scenario, the more experience people are likely to have with deployed systems of intermediate sophistication, the lower the risk of a treacherous turn.


# The alignment problem without a discontinuity

More recently, Paul Christiano and Katja Grace have argued that, even if there is no discontinuity, AI misalignment still poses a risk of negatively affecting the long-term trajectory[^9] of earth-originating intelligent life. According to this argument, once AIs do nearly all productive work, humans are likely to lose control of this trajectory to the AIs. Christiano and Grace argue that (i) solving the alignment problem and (ii) reducing competitive pressures to deploy AI would help ensure that human values continue to shape the future.

In terms of our three properties: Christiano and Grace drop the discontinuity hypothesis, but continue to view the alignment problem as the source of AI risk. It’s unclear whether the risks they have in mind would qualify as existential.

The arguments in this section and the next section (“arguments unrelated to the alignment problem”) have been made much more briefly than the early arguments. As a result, they leave a number of open questions which I’ll discuss for each argument in turn. 


## The basic picture

The argument appears to be essentially the following. When AIs become more capable than humans at economically useful tasks, they will be given increasingly more control over what happens. The goals programmed into AIs, rather than human values, will become the primary thing shaping the future. Once AIs make most of the decisions, it will become difficult to remove them or change the goals we have given them. So, unless we solve the alignment problem, we will lose (a large chunk of) the value of the future.

This story is most clearly articulated in the writings of Paul Christiano, a prominent member of the AI safety community who works in the safety team at OpenAI. In a 2014 blog post, _Three Impacts of Machine Intelligence_, he writes: 


>it becomes increasingly difficult for humans to directly control what happens in a world where nearly all productive work, including management, investment, and the design of new machines, is being done by machines. [...] I think human management becomes increasingly implausible as the size of the world grows (imagine a minority of 7 billion humans trying to manage the equivalent of 7 trillion knowledge workers; then imagine 70 trillion), and as machines’ abilities to plan and decide outstrip humans’ by a widening margin. In this world, the AI’s that are left to do their own thing outnumber and outperform those which remain under close management of humans.

As a result, AI values, rather than human values, will become the primary thing shaping the future. The worry is that we might therefore get “a future where our descendants maximiz[e] some uninteresting values we happened to give them because they were easily specified and instrumentally useful at the time.”

In his interview on the 80,000 Hours podcast, Christiano explains that he sees two very natural categories of things that affect the long run trajectory of civilisation: extinction, which is sticky because we can never come back from it, and changes in the distribution of values among agents, which “can be sticky in the sense that if you create entities that are optimizing something, those entities can entrench themselves and be hard to remove”. The most likely way the distribution of values will change, according to him, is that as we develop AI, we’ll “pass the torch from humans, who want one set of things, to AI systems, that potentially want a different set of things.”

Katja Grace, the founder of AI Impacts, explicitly addresses the point about development trajectories (also on the 80,000 Hours podcast): “even if things happen very slowly, I expect the same problem to happen in the long run: AI being very powerful and not having human values.” She gives an example of this slow-moving scenario:


>suppose you’re a company mining coal, and you make an AI that cares about mining coal. Maybe it knows enough about human values to not do anything terrible in the next ten years. But it’s a bunch of agents who are smarter than humans and better than humans in every way, and they just care a lot about mining coal. In the long run, the agents accrue resources and gain control over things, and make us move toward mining a lot of coal, and not doing anything that humans would have cared about.[^10]


## The importance of competitive pressures

There is likely to be a trade-off, when building an AI, between making it maximally competent at some instrumentally useful goal, and aligning it with human values.[^11]

In the 80,000 Hours interview, Christiano said: “I think the competitive pressure to develop AI, in some sense, is the only reason there’s a problem”, because it takes away the option of slowing down AI development until we have a good solution to the alignment problem. 

According to Christiano, there are therefore two ways to make a bad outcome less likely: coordinating to overcome the competitive pressure, or making technical progress to alleviate the trade-off.


## Questions about this argument

This argument for prioritising AI has so far only been sketched out in a few podcast interviews and blog posts. It has also been made at a high level of abstraction, as opposed to relying on a concrete story of how things might go wrong. Some key steps in the argument have not yet been spelled out in detail. For example:



* There isn’t really a very detailed explanation of why misalignment at an early stage (e.g. of a coal-mining AI) couldn’t be reversed as the AI begins to do undesirable things. If AIs only gradually gain the upper hand on humanity, one might think there would be many opportunities to update the AIs’ values if they cease to be instrumentally useful.
* In particular, competitive pressures explain why we would deploy AI faster than is prudent, but they don’t explain why relatively early misalignment should quickly become irreversible. If my AI system is accidentally messing up my country, and your AI system is accidentally messing up your country, we both still have strong incentives to figure out how to correct the problem in our own AI system.


# Arguments unrelated to the alignment problem

Recently, people have given several new arguments for prioritising AI, including: (i) risks that AI might be misused by bad actors, (ii) that it might make great-power war more likely and (iii) value erosion from competition. These risks are unrelated to the alignment problem. Like those in the previous section, these new arguments have mostly been made briefly.


## Misuse risks


### The basic argument

The Open Philanthropy Project (OpenPhil) is a major funder in AI safety and governance. In OpenPhil’s [main blog post](https://www.openphilanthropy.org/blog/potential-risks-advanced-artificial-intelligence-philanthropic-opportunity) on potential risks from advanced AI, their CEO Holden Karnofsky writes: 


>One of the main ways in which AI could be transformative is by enabling/accelerating the development of one or more enormously powerful technologies. In the wrong hands, this could make for an enormously powerful tool of authoritarians, terrorists, or other power-seeking individuals or institutions. I think the potential damage in such a scenario is nearly limitless (if transformative AI causes enough acceleration of a powerful enough technology), and could include long-lasting or even permanent effects on the world as a whole.[^12]

Karnofsky’s argument (which does not crucially rely on discontinuities) seems to be the following:



* AI will be a powerful tool
* If AI will be a powerful tool, then AI presents severe bad-actor risks
* The damage from bad-actor AI risks could be long-lasting or permanent

For a more detailed description of particular misuse risks, we might turn to the report titled _The Malicious Use of Artificial Intelligence: Forecasting, Prevention, and Mitigation_ (2018). However, this report focuses on negative impacts that are below the level of a global catastrophic risk, for example: cyberattacks, adversarial examples and data poisoning, autonomous weapons, causing autonomous vehicles to crash, and similar.


#### Questions about this argument



* Overall, the argument from the misuse risks discussed above seems to have only been briefly sketched out.
* Karnofsky’s argument is very general, and doesn’t fully explain the focus on AI as opposed to other technologies
* A similar argument to Karnofsky’s could be made for any potentially transformative technology (e.g. nanotechnology). Why focus on the misuse of AI? There are many potential reasons, for example:
    * AI is far more transformative than other technologies, and therefore far more dangerous in the wrong hands.
    * We are in a particularly good position to prevent misuse of AI, compared to misuse of other technologies.
    * The blog post does not say which reasons are the crucial drivers of Karnofsky’s view that AI misuse risks are particularly deserving of attention.
* The inference “If AI will be a powerful tool, then AI presents severe bad-actor risks” hasn’t been explained in detail.
    * A technology can be powerful without increasing bad actor risks. Whether a given technology increases bad actor risks seems to hinge on complicated questions around the relative efficacy of offensive vs. defensive applications, the way in which capabilities will be distributed between different actors.
    * Even nuclear weapons have arguably decreased the risk of "bad actor" states initiating invasions or wars.
* No-one has yet made a detailed case for why we should expect the risks discussed in this section to rise to the level of global catastrophic risks


### Robust totalitarianism

One type of misuse risk that has been described in slightly more detail is that of totalitarian regimes using AI to entrench their power, possibly for the very long-run. One of the four sources of catastrophic risk on the research agenda of the [Center for the Governance of AI](http://governance.ai) (GovAI) is “robust totalitarianism ​[...] enabled by advanced lie detection, social manipulation, autonomous weapons, and ubiquitous physical sensors and digital footprints.” The research agenda states that “power and control could radically shift away from publics, towards elites and especially leaders, making democratic regimes vulnerable to totalitarian backsliding, capture, and consolidation.” The argument from totalitarianism does not crucially depend on discontinuity assumptions.[^13] 

According to this argument, AI technology has some specific properties, such that AI will shift the balance of power towards leaders, and facilitate totalitarian control.


#### Questions about this argument



* No detailed case yet regarding the effects of AI on totalitarianism
    * It seems plausible that the technologies mentioned (“advanced lie detection, social manipulation, autonomous weapons, and ubiquitous physical sensors and digital footprints”) would be useful to totalitarians. But some applications of them surely push in the other direction. For example, lie detection could be applied to leaders to screen for people likely to abuse their power or turn away from democratic institutions.
    * In addition, it is conceivable that other AI-enabled technologies might push against totalitarianism.
    * As of yet, in the public literature, there has been no systematic examination of the overall effect of AI on the probability of totalitarianism. 
* Long-term significance has not been much argued for yet
    * Suppose that AI-facilitated totalitarianism is plausible. From a long-termist point of view, the important question is whether this state of affairs is both (i) relatively avoidable and (ii) stable for the very long term.[^14] Such points of leverage, where something could go one way or the other, but then “sticks” in a foreseeably good or bad way, are probably rare. 
    * The only academic discussion of the topic I could find is Caplan 2008, “The Totalitarian Threat”. The article discusses risk factors for stable totalitarianism, including technological ones, but takes the view that improved surveillance technology is unlikely to make totalitarianism last longer.[^15]

## Increased likelihood of great-power war

The GovAI research agenda presents four sources of catastrophic risk from AI. One of these is the risk of “preventive, inadvertent, or unmanageable great-power (nuclear) war​.” The research agenda explains that:


>Advanced AI could give rise to extreme first-strike advantages, power shifts, or novel destructive capabilities, each of which could tempt a great power to initiate a preventive war. Advanced AI could make crisis dynamics more complex and unpredictable, and enable faster escalation than humans could manage, increasing the risk of inadvertent war.[^16]

Breaking this down, we have two risks, and for each risk, some reasons AI could heighten it:



1. Preventive war
    1. First-strike advantages
    2. Power shifts
    3. Novel destructive capabilities
2. Inadvertent war
    4. More complex and unpredictable crisis dynamics
    5. Faster escalation than humans can manage

This [publication](https://www.rand.org/content/dam/rand/pubs/perspectives/PE200/PE296/RAND_PE296.pdf) from the RAND Corporation summarises the conclusions from a series of workshops that brought together experts in AI and nuclear security to explore how AI might affect the risk of nuclear war by 2040. The authors discuss several illustrative cases, for example the possibility that AI might undermine second-strike capability by allowing better targeting and tracking of mobile missile launchers.[^17] 


### Questions about this argument



* Specificity to AI is still unclear
    * With the exception of point 2.2 (AIs enabling faster escalation than humans can manage), these arguments don’t seem very specific to AI. 
    * Many technologies could lead to more complex crisis dynamics, or give rise to first-strike advantages, power shifts, or novel destructive capabilities.
    * It could still be legitimate to prioritise the AI-caused risks most highly. But it would require additional argument, which I haven’t seen made yet. 
* What is the long-termist significance of a great-power war? 
    * Great-power nuclear war would lead to a nuclear winter, in which the burning of cities sendings smoke into the upper atmosphere. 
    * There is significant uncertainty about whether a nuclear winter would cause an existential catastrophe. My impression is that most people in the existential risk community believe that even if there were an all-out nuclear war, civilisation would eventually recover, but I haven’t carefully checked this claim[^18].
    * According to a [blog post](https://blog.givewell.org/2015/08/13/the-long-term-significance-of-reducing-global-catastrophic-risks/) by Nick Beckstead, many long-termists believe that a catastrophic risk reduction strategy should be almost exclusively focused on reducing risks that would kill 100% of the world’s population, but Beckstead believes that sub-extinction catastrophic risks should also receive attention in a long-termist portfolio.
    * It has been suggested that great-power war could accelerate the development of new and potentially very dangerous technologies.
* What are the practical implications of the argument? If great-power nuclear war were one of the main risks from AI, this might lead us to work directly on improving relations between great powers or reducing risks of nuclear war rather than prioritising AI. 


## Value erosion from competition

According to the GovAI research agenda, another source of catastrophic risk from AI is


>systematic value erosion from competition, in which each actor repeatedly confronts a steep trade-off between pursuing their final values or pursuing the instrumental goal of adapting to the competition so as to have more power and wealth.

As stated, this is an extremely abstract concern. Loss of value due to competition rather than cooperation is ubiquitous, from geopolitics to advertising. Scott Alexander [vividly describes](https://slatestarcodex.com/2014/07/30/meditations-on-moloch/) the value that is destroyed in millions of suboptimal Nash equilibria throughout society. 

Why might AI increase the risk of such value erosion to a catastrophic level? 

In the publicly available literature, this risk has not been described in detail. But some works are suggestive of this kind of risk: 



* In _The Age of Em_, Robin Hanson speculates about a future in which AI is first achieved through emulations (“ems”) of human minds. He imagines this as a hyper-competitive economy in which, despite fantastic wealth from an economy that doubles every month or so, wages fall close to Malthusian levels and ems spend most of their existence working. However, they “need not suffer physical hunger, exhaustion, pain, sickness, grime, hard labor, or sudden unexpected death.” There is also a section in _Superintelligence_ asking, “would maximally efficient work be fun?”
* In _Artificial Intelligence and Its Implications for Income Distribution and Unemployment_ (Section 6) Korinek and Stiglitz imagine an economy in which humans compete with much more productive AIs. AIs bid up the price of some scarce resource (such as land or energy) which is necessary to produce human consumption goods. Humans “lose the malthusian race” as growing numbers of them decide that given the prices they face, they prefer not to have offspring.[^19] 

### Questions about this argument

This argument is highly abstract, and has not yet been written up in detail. I’m not sure I’ve given an accurate rendition of the intended argument. So far I see one key open question:



* Collective action problems which we currently face typically erode some, but not all value. Why do we expect more of the value to be eroded once powerful AI is present?


# People who prioritise AI risk should clarify which arguments are causing them to do so


## How crucial is the alignment problem?

The early case for prioritising AI centered on the alignment problem. Now we are seeing arguments that focus on other features of AI; for example, AI’s possible facilitation of totalitarianism, or even just the fact that AI is likely to be a transformative technology. Different members of the broad beneficial AI community might view the alignment problem as more or less central.


## What is the attitude towards discontinuity hypotheses?

For long-termists, I see three plausible attitudes[^20]:



* They prioritise AI because of arguments that rely on a discontinuity, and they think a discontinuous scenario is probable. The likelihood of a discontinuity is a genuine crux of their decision to prioritise AI.
* They prioritise AI for for reasons that do not rely on a discontinuity 
* They prioritise AI because of possibility of discontinuity, but its likelihood is not a genuine crux, because they see no plausible other ways of affecting the long-term future.

Of course, these are three stylised attitudes. It’s likely that many people have an intermediate view that attaches some credence to each of these stories. Even if most people are somewhere in the middle, identifying these three extreme points on the spectrum can be a helpful starting point.

The third of these attitudes is really exclusive to long-termists. For more conventional ways of prioritising, there are many plausible contenders for the top priority, and the likelihood of a risk scenario should be crucial to the decision of whether to prioritise mitigating that risk. Non long-termists could take either of the other two attitudes towards discontinuities. 


## Benefits of clarification

My view that people should clarify why they prioritise AI is mostly based on a heuristic that confusion is bad, and we should know why we make important decisions. I can also try to give some more specific reasons:



* The motivating scenario should have strong implications about which activities to prioritise within AI. To take the most obvious example, technical work on the alignment problem is critical for the scenarios that center around misalignment, and unimportant otherwise. Preparing for a single important ‘deployment’ event only makes sense under discontinuous scenarios.[^21]
* Hopefully, the arguments that motivate people are better than the other arguments. So focusing on these should facilitate the process of evaluating the strength of the case for AI, and hence the optimal size of the investment in AI risk reduction.
* _Superintelligence_ remains the only highly detailed argument for prioritising AI. Other justifications have been brief or informal. Suppose we learned that one of the latter group of arguments is what actually motivates people. We would realise that the entire publicly available case for prioritising AI consists of a few blog posts and interviews.
* Costly misunderstandings could be avoided, both with people who are sceptical of AI risk and with sympathetic people who are considering entering this space.
    * Many people are sceptical of AI risk. It may not currently be clear to everyone involved in the debate why some people prioritise AI risk. I would expect this to lead to unproductive or even conflictual conversations, which could be avoided with more clarification.
    * People who are considering entering this space might be confused by the diversity of arguments, and might be led to the wrong conclusion about whether their skills can be usefully applied.
* If arguments which assume discontinuities are the true motivators, then the likelihood of discontinuities is plausibly a crux of the decision to prioritise AI. This would suggest that there is very high value of information in forecasting the likelihood of discontinuities.


# Appendix: What I mean by “discontinuities”

By _discontinuity_ I mean an improvement in the capabilities of powerful AI that happens much more quickly than what would be expected based on extrapolating past progress. This is obviously a matter of degree. In this document I apply the label “discontinuity” only to very large divergences from trend, roughly those that could plausibly lend themselves to a single party gaining a decisive strategic advantage.

If there is a discontinuity, then the first AI system to undergo this discontinuous progress will become much more capable than other parties. The sharper the discontinuity, the less likely it is that many different actors will experience the discontinuity at the same time and remain at comparable levels of capability.

Below I detail two ways in which this notion of discontinuity differs from Bostrom’s “fast take-off”.


## Discontinuities aren’t defined by absolute speed

Bostrom defines a “fast take-off” as one that occurs over minutes, hours, or days. 

The strategically relevant feature of the discontinuous scenarios is that a single AI system increases in capabilities much faster than other actors. (These actors could be other AIs, humans, or humans aided by AI tools). No actor can react quickly enough to ensure that the AI system is aligned; and no actor can prevent the AI system from gaining a decisive strategic advantage.

By defining a “fast take-off” with the absolute numerical values “minutes, hours, or days”, Bostrom is essentially making the prediction that such a “take-off” would indeed be fast in a strategically relevant sense. But this could turn out to be false. For example, Paul Christiano predicts that “in the worlds where AI radically increases the pace of technological progress [...] everything is getting done by a complex ecology of interacting machines at unprecedented speed.” 

The notion of discontinuities is about the shape of the “curve of AI progress” -- specifically, how discontinuous or kinked it is -- and is agnostic about absolute numerical values. In this way, I think it better tracks the strategically relevant feature.


## Discontinuities could happen before “human-level”

Bostrom’s analysis of AI trajectories is focused on the “take-off” period, which he defines as the period of time that lies between the development of the first machine with “human-level general intelligence” and the development of the first machine that is “radically superintelligent”. There is little analysis of trajectories before “human-level general intelligence” is achieved.

One approach is to define a machine as having “human-level general intelligence” if it is at least as good as the average human at performing (or perhaps quickly learning) nearly any given cognitive task. But then it seems that many risky events could occur before human-level general intelligence. For example, one could imagine an AI system that is capable of running most of a country’s R&D efforts, but lacks the ability to engage in subtle forms of human interaction such as telling jokes.

The notion of discontinuity is not restricted in this way. A discontinuity could occur at any point during the development of powerful AI systems, even before “human-level”.

[^1]:
     In an intelligence explosion, an AI rapidly and recursively self-improves to become superintelligent.

[^3]:
     Yudkowsky does not explicitly say whether discontinuity hypotheses are a crux of his interest in AI risk. He merely remarks: “I tend to assume arbitrarily large potential jumps for intelligence because (a) this is the conservative assumption; (b) it discourages proposals based on building AI without really understanding it; and (c) large potential jumps strike me as probable-in-the-real-world.” In a 2016 Facebook [post](https://www.econlib.org/archives/2016/03/so_far_unfriend.html), reprinted by Bryan Caplan, Yudkowsky describes “rapid capability gain” as one of his three premises for viewing AI as a critical problem to be solved. If discontinuities imply “a higher standard for Friendly AI techniques”, this suggests that AI safety work would still be needed in more continuous scenarios, but would only need to meet a lower standard. But we are not told how low this standard would be, and it if would still, in Yudkowsky’s view, justify prioritising AI. Regardless, Yudkowsky has not given any detailed argument for viewing AI as a catastrophic risk (let alone an existential one) if there are no discontinuities.

[^4]:
     Defined by Bostrom as “a level of technological and other advantages sufficient to enable [...] complete world domination”.

[^5]:
     My claim is that discontinuities are a crucial premise for the conclusion that AI is likely to lead to an existential catastrophe. Strictly speaking, it's incidental to my claim whether Bostorm assigns a high or low likelihood to a discontinuity. In fact, he says a discontinuity is "likely". He also discusses multipolar scenarios that could result from more continuous trajectories (chapter 11), and some of these scenarios could arguably be sufficiently bad to warrant the label “existential risk” -- but these scenarios are not the focus of the book and nor, in my view, did they seem to shape the priorities inspired by the book.

[^6]:
     Bostrom writes: “Consider the following medium takeoff scenario. Suppose it takes a project one year to increase its AI’s capability from the human baseline to a strong superintelligence, and that one project enters this takeoff phase with a six-month lead over the next most advanced project. The two projects will be undergoing a takeoff concurrently. It might seem, then, that neither project gets a decisive strategic advantage. But that need not be so. Suppose it takes nine months to advance from the human baseline to the crossover point, and another three months from there to strong superintelligence. The frontrunner then attains strong superintelligence three months before the following project even reaches the crossover point. This would give the leading project a decisive strategic advantage [...]. Since there is an especially strong prospect of explosive growth just after the crossover point, when the strong positive feedback loop of optimization power kicks in, a scenario of this kind is a serious possibility, and it increases the chances that the leading project will attain a decisive strategic advantage even if the takeoff is not fast.” In this scenario, what enables the frontrunner to obtain a decisive strategic advantage is the existence of crossover point just after which there is explosive growth. But that is precisely a discontinuity.

[^7]:
     The paper _Concrete Problems in AI Safety_ describes five sources of AI accidents. They stand on their own, separate from discontinuity considerations.

[^8]:
     A singleton is “a world order in which there is at the global level a single decision-making agency”.

[^9]:
     Here and in the rest of the document, I mean “long-term” in the sense of potentially many millions of years. Beckstead (2013), _On the overwhelming importance of shaping the far future_, articulated “long-termism”, the view that we should focus on the trajectory of civilisation over such very long time-scales. See [here](https://80000hours.org/articles/future-generations/) for a short introduction to long-termism. 

[^10]:
     This quote is lightly edited for clarity.

[^11]:
     If we don’t know anything about alignment, the trade-off is maximally steep: we can either have unaligned AI or no AI. Technical progress on the alignment problem would partially alleviate the trade-off. In the limit of a perfect solution to the alignment problem, there would be no trade-off at all.

[^12]:
     To be clear, in addition to misuse risks, OpenPhil is also interested in globally catastrophic accidents from AI.

[^13]:
     Of course, AI trajectories might have some bearing on the argument. One might believe that civil society will be slow to push back against new AI-enabled totalitarian threats, while states and leaders will be quick to exploit AI for totalitarian purposes. If this is true, very fast AI development might slightly increase the risk of totalitarianism.

[^14]:
     If it were the nearly unavoidable consequence of AI being developed, there would be no point trying to oppose it. If the totalitarian regime would eventually collapse, (i.e. fail to be robust for the very long run), then, although an immeasurable tragedy from a normal perspective, its significance would be small from the long-termist point of view.

[^15]:
     Caplan writes: “Orwell's _1984_ described how new technologies would advance the cause of totalitarianism.  The most vivid was the "telescreen," a two-way television set.  Anyone watching the screen was automatically subject to observation by the Thought Police.  Protagonist Winston Smith was only able to keep his diary of thought crimes because his telescreen was in an unusual position which allowed him to write without being spied upon. Improved surveillance technology like the telescreen would clearly make it easier to root out dissent, but is unlikely to make totalitarianism last longer.  Even without telescreens, totalitarian regimes were extremely stable as long as their leaders remained committed totalitarians.  Indeed, one of the main lessons of the post-Stalin era was that a nation can be kept in fear by jailing a few thousand dissidents per year.”

[^16]:
     It’s worth noting that this set of risks is distinct from misuse risks. Misuse involves the intentional use of AI for bad purposes, whereas here, the argument is that AI might make war more likely, regardless of whether any party uses an AI system to directly harm an adversary. See [this essay](https://www.lawfareblog.com/thinking-about-risks-ai-accidents-misuse-and-structure) for an explanation of how some risks from AI arise neither from misuse nor from accidents.

[^17]:
     Mobile missile launchers move regularly via road or rail. Many states use them because they are difficult to track and target, and therefore constitute a credible second-strike capability. The RAND publication states that “AI could make critical contributions to intelligence, surveillance, and reconnaissance (ISR) and analysis systems, upending these assumptions and making mobile missile launchers vulnerable to preemption.”

[^18]:
     This [post](http://www.overcomingbias.com/2012/11/nuclear-winter-and-human-extinction-qa-with-luke-oman.html) by Carl Schulman is relevant. 

[^19]:
     The details of the model are in Korinek (2017), a working paper called _Humanity, Artificial Intelligence, and the Return of Malthus_, which is not publicly available online. [Here](https://www.aeaweb.org/conference/2018/preliminary/powerpoint/7yiDBfHY) are slides from a talk about the working paper.

[^20]:
     There are some other conceivable attitudes too. One could, for example, find a discontinuity probable, but still not focus on those scenarios, because one finds that we're certainly doomed under such a scenario.

[^21]:
     These are just some quick examples. I would be interested in a more systematic investigation of what chunks of the problem people should break off depending on what they believe the most important sources of risk are.


<!-- Docs to Markdown version 1.0β17 -->
 