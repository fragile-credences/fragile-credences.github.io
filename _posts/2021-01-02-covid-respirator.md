---
layout: post
title: "Modified respirator to shield myself and others from COVID"
image: /assets/images/mask/social_image.PNG
tags: ["DIY", "how to"]
---

**Summary:** _I have tried many types of masks and respirators during the 2020 pandemic. My recommendation is to use 'elastomeric' respirators common in industry, and to either filter or completely block off their exhalation valve. The result is a comfortable respirator that I believe offers a high level of protection against airborne diseases to myself and others. I am not an infectious disease expert._

# Contents
{: .no_toc}
1. toc
{:toc}

# Elastomeric respirators
The effectiveness of a mask can be broken down into two parts: how well the mask fits on your face, and the filtration efficiency of the mask. A further important consideration is comfort.

Surgical and cloth masks are comfortable but have poor fit and filtration efficiency. I believe it's possible to do much better.

Respirators that meet the NIOSH [N95 or N99 standards][niosh] for filtration efficiency, such as the N95 respirators pictured below, are popular in healthcare settings.

<div style="display: flex">
![](../assets/images/mask/3M_N95_Particulate_Respirator.png)
![](../assets/images/mask/n95_sailor.webp)
</div>
_3M N95 respirator (left), N95 respirator in a medical setting (right)_

In my experience, these have two main downsides:
- They may be scarce during pandemics. You should probably leave limited supplies for healthcare workers.
- The tight elastic band that ensures a good fit also makes the respirators very uncomfortable for extended use.

KN95 and KF95 are respectively the Chinese and Korean-manufactured masks that claim to have the same efficacy as N95s. They come with ear loops rather than behind-the-head elastic bands, so they have a far looser seal than N95s. I suppose you could add your own elastic bands to them to improve the seal, but then they would be just as uncomfortable as N95s. Therefore, they are not a competitive option.

![](../assets/images/mask/kn95_stock.webp)
_A KN95 mask_

There also exist N95+ masks designed for industrial tasks that produce harmful airborne particles (such as welding or paint spraying). They are called elastomeric respirators, or sometimes industrial respirators.

<div style="display: flex">

![](../assets/images/mask/miller_respirator_stock.webp)
![](../assets/images/mask/3m-half-facepiece-reusable-respirator.webp)
</div>
_High filtration efficiency elastomeric respirators for industrial use. Miller LPR-100 (left), 3M 6200 (right)._

Compared to healthcare N95s, these respirators:
- are more widely available
- achieve superior fit by using elastomers shaped like a human face (there is no need to bend a metal nose bridge)
- are **much more comfortable**, mainly because they:
    - spread the pressure onto a wider area of skin
    - come in multiple sizes
    - have adjustable straps
- won't fog up your glasses

A downside is that it's more difficult to be audible through an elastomeric respirator than through an N95 or surgical mask. I am able to be understood by raising my voice, but smooth social interactions are not guaranteed. It's probably not a great setup for spending time with your friends; you can use a KN95 for that.

The fatal flaw[^fatal] of these elastomerics when it comes to disease control is that they have an exhalation valve that allows unfiltered air to exit the mask. In PPE jargon, they do not provide source control. (This may be about to change in 2021, see this footnote[^MSA]. I will try to keep this post updated.)

<video loop muted controls style="max-height: 75vh; max-width: 50%">
  <source src="../assets/images/mask/valve.webm" type="video/webm">
  Your browser does not support the video tag.
</video>
_The exhalation valve opening on the Miller LPR-100_

We can modify these respirators to filter their exhalation valve (recommendaton A), or completely close it off (recommendation B).

(If infection through the mucosal lining of the eyes is an important concern to you, and you don't wear glasses, you should also wear safety googgles.)

[^fatal]:
    Or is it fatal? I had always assumed it was a fatal flaw, until I found some experts arguing otherwise. In [this commentary](https://www.ajicjournal.org/article/S0196-6553(20)30888-9/fulltext), the authors say: "Data characterizing particle release through exhalation valves are presently lacking; it is our opinion that such release will be limited by the complex path particles must navigate through a valve. We expect that fewer respiratory aerosols escape through the exhalation valve than through and around surgical masks, unrated masks, or cloth face coverings, all of which have much less efficient filters and do not fit closely to the face". 

    I have been able to find some data; this [recent NIOSH study](https://www.cdc.gov/niosh/docs/2021-107/pdfs/2021-107.pdf?id=10.26616/NIOSHPUB2021107) finds that valved N95s have 1-40% penetration. "some models ... had less than 20% penetration even without any mitigation. Other models ... had much greater penetration with a median penetration above 40%." Note that for these tests, the flow rates of 25-85 L/min are higher than the 6 L/min of a person at rest, and that lower flow rates had lower penetration. 

    Penetration rates of tens of percent are not very good, and not acceptable for my standards, but it's less bad than I expected, perhaps competitive with surgical masks, and better than cloth masks!

    ![Niosh](../assets/images/mask/niosh_study_fig5.webp)





[^MSA]:
    In fact, as of November 25 2020, the company MSA Safety announced in a [press release](https://www.prnewswire.com/news-releases/first-elastomeric-respirator-without-exhalation-valve-approved-by-niosh-301180276.html) that the **first elastomeric respirator without an exhalation valve has been approved by NIOSH**. It's called the Advantage 290 Respirator. The [product page](https://us.msasafety.com/p/0001000002W0001120) has some good documentation.

    This [journal article](https://www.journalacs.org/article/S1072-7515(20)30471-3/fulltext) from September 2020, although it does not mention MSA, appears to be about the Advantage 290. (This is based on the picture in Fig 1. resembling the picture in the press release, and the fact that the hospitals in the paper are in Pennsylvania and New York states, while MSA is headquartered in Pennsylvania). The article explains how it was rolled out to thousands of healthcare workers (a first wave had 1,840 users). They claim that the cost was "approximately $20 for an elastomeric mask and $10 per cartridge", which is amazingly low.

    They write: "After more than 1 month of usage, we have found that filters have not needed to be changed more frequently than once a month".

    Unfortunately, it seems to be difficult to get one's hands on one of these right now. The website invites you to contact sales, and the lowest option for "your budget" is "less than $9,999".

    Moreover, even if you were able to get the Advantage 290, it might be too selfish to do so, since this respirator is likely to otherwise be used by healthcare workers. On the other hand, the price signal you create would in expectation lead to greater quantities being produced, partially offsetting the effect. If you are able to get one by paying a large premium over the hospital price, this may even be net positive for others.

    If this respirator became available in large quantities, everything I say here would be obsolete.

    By the way, I am astonished that it took until this November 2020 for a PPE company to create a valveless elastomeric respirator, this seems to be a very useful product for any infectious disease situation.



# CDC recommendation for exhalation valves
During the 2020 pandemic, the US CDC issued the following recommendation, in a [blog post](https://blogs.cdc.gov/niosh-science-blog/2020/09/08/source-control/) from August 8 2020[^cdc]:
> If only a respirator with an exhalation valve is available and source control is needed, cover the exhalation valve with a surgical mask, procedure mask, or a cloth face covering that does not interfere with the respirator fit.

[^cdc]: It's unclear to me how much one should downweight this recommendation due to appearing on a CDC blog rather than as more formal CDC guidance. In the post, the recommendations are called "tips".

# Recommendation A: 3M 6500QL Series with KN95 and surgical mask
If you want to follow something similar to CDC guidance, I recommend:
* A [3M 6500QL series][3m6500] respirator
* A part of a KN95/KF95 mask tightly covering the exhalation valve

<div style="display: flex">
![](../assets/images/mask/3m_original.webp)
![](../assets/images/mask/3m_modified_0.webp)
![](../assets/images/mask/3m_modified_1.webp)
</div>
_3M 6502QL. Unmodified (left), KN95 material covering valve (middle and right)_

You'll likely want to add a surgical mask on top of that: 
* as a backup
* for the very small amount of additional filtration it provides
* to avoid misunderstandings with strangers

<div style="width: 33%">

![](../assets/images/mask/3m_modified_surgical.webp)</div>
_3M 6502QL with KN95 material covering valve and a surgical mask on top_

Surgical masks are not primarily designed to filter aerosols[^surgical_fda]. It seems clear to me that KN95s and KF95s are superior to a surgical mask for covering an exhalation valve (let a alone a cloth mask). (There is a [list][fdaEUAs] of such respirators that have received an emergency use authorization from the FDA. There are probably many low-quality masks fraudulently marketed as KN95 and KF95 at the moment, so make sure you buy from an approved manufacturer.)

In the models I have seen, the material in KN95s is far more flexible than in N95s, making allowing you to shape it so that it tightly covers an exhalation valve. It's slightly fiddly but definitely possible with a bit of dexterity and perseverance. Using a thinner surgical mask would be easier; but the KN95's  extra protection for third parties is well worth it.

Here are the steps you should follow (see video):
* cut a KN95 in half along the fold
* cut one half to size further
* use a rubber band and tape to attach the material over the respirator valve. This is better explained with a video than in words. The main thing to know is that you should use the two small ridges in the plastic below the valve to secure the rubber band.
* add tape on the upper end of the KN95 material

<video controls style="max-height: 100vh; max-width:100%">
  <source src="../assets/images/mask/instructions.webm" type="video/webm">
  Your browser does not support the video tag.
</video>
_Instructions_

Unfortunately, for any valve covering approach, there is a trade-off between a fit and the surface area usable for exhale filtration. I have not been able to achieve a good fit when placing a KN95 or surgical mask more loosely over the valve, which would give more surface area. In my setup a small rectangle of KN95 has to do all the filtration, which likely lowers the efficiency. However, the N95 specification is for a flow rate of 85 liters per minute, which is many times the 6 liters per minute breathed by an individual at rest[^flowrate], so I am not very concerned.

[^flowrate]: 3M [claims](https://risk.arizona.edu/sites/default/files/3mrespiratorsandsurgicalmaskcomparison.pdf) that "85 liters per minute (lpm) represents a very high work rate, equivalent to the breathing rate of an individual running at 10 miles an hour". [These lecture notes](http://webcache.googleusercontent.com/search?q=cache:7nf66Oofo38J:www.umich.edu/~exphysio/mvs110lecture/Readings/Reading7PhysiolSupportSys.doc) say that a person has a pulmonary ventilation of 6 L/min at rest, 75 L/min during moderate exercise, and 150L/min during vigorous exercise.


<div style="width: 50%">

![](../assets/images/mask/ridges.webp)
</div>
_Ridges on 6502QL. Note that in the real setup the KN95 will go below the elastic band._
<div style="width: 50%">

![](../assets/images/mask/3m_modified_valve_rectangle.webp)
</div>
_Location of the valve underneath the KN95 material. View form below the respirator._

[fdaEUAs]: https://www.fda.gov/medical-devices/coronavirus-disease-2019-covid-19-emergency-use-authorizations-medical-devices/personal-protective-equipment-euas

[^surgical_fda]: The [FDA says](https://www.fda.gov/medical-devices/personal-protective-equipment-infection-control/n95-respirators-surgical-masks-and-face-masks#s2): "While a surgical mask may be effective in blocking splashes and large-particle droplets, a face mask, by design, does not filter or block very small particles in the air that may be transmitted by coughs, sneezes, or certain medical procedures."

## Choice of respirator
I have tried two industrial respirator models, the [3M 6502QL](https://www.google.com/search?q=3M%206502QL) and the [Miller LPR-100](https://www.google.com/search?q=miller+lpr-100). I prefer the build quality and aesthetics of the Miller (see [below](#choice-of-respirator-1)), but its shape makes it almost impossible to get a good seal if you attempt to cover the valve with a surgical mask or KN95. So for this technique, I recommend the [3M 6500QL series](https://www.google.com/search?q=3M+6500QL+series).

I am aware of three 3M half-facepiece reusable respirator groups, the 6000 series, the 6500 series, and the 7500 series.

![](../assets/images/mask/3m_lineup.webp)
_3M half-facepiece reusable respirators ([3M.com](https://www.3m.com/3M/en_US/company-us/all-3m-products/~/All-3M-Products/Personal-Protective-Equipment/Reusable-Respirators/?N=5002385+8711017+8720539+8720550+3294857497&rt=r3))_

Since I have only tried a respirator of the 6500 series, I do not have a strong view on which is preferable. I would recommend the 6500, mostly because I have already demonstrated that it's possible to cover the valve. The 6000 series does not have a downward-facing exhalation valve and may be harder to work with. I'm agnostic about the relative merits of the 7500.

The 6500 series has a quick latch version (difference explained [here][3m6500]), which is the one I used. I'd recommend the quick latch 6500QL series, because it seems that the latch makes the fit of the KN95 material to the respirator more secure (see video). By the way, attaching a mask on top of the valve makes the quick-latch mechanism much less effective; I never use it.

Each series comes in three sizes, large, medium and small. I am a male with a medium-to-large head, and I use a medium (the 6502QL).

[3m6500]: https://www.3m.com/3M/en_US/worker-health-safety-us/personal-protective-equipment/half-face-respirator/

Regarding whether airlines will accept this setup, I have heard both some positive anecdotes and one negative anecdote.

## Choice of filters for a 3M respirator
I use the 3M 2097 P100 filters.

You should use lightweight filters that are rated N100, R100 or P100. The "100" [means](https://en.wikipedia.org/wiki/NIOSH_air_filtration_rating) that 99.97% of particles smaller than 0.3 micrometres are filtered out. The letters N, R and P refer to whether the filter is still effective when exposed to oil-based aerosols, this should be irrelevant for our purposes.

The weight of the filters is a crucial determinant of comfort. I originally used the 3M respirator with the 3M 60926 cartridges, which filter gases and vapors as well as particles. This was a mistake, as filtering gases and vapors is irrelevant from the point of view of infectious disease, and these cartridges are much heavier than the 3M 2097 P100 filters. Switching to the lighter filters made a world of difference; now wearing the 3M doesn't bother me at all.

<div style="display: flex">

![](../assets/images/mask/3m_weight_cartridge.webp)
![](../assets/images/mask/3m_weight_filter.webp)
</div>
_The 3M 6502QL respirator weighs 395 g. with 3M 60926 cartridges, but only 128 g. with 3M 2097 filters, a 68% reduction._

# Recommmendation B: Miller LPR-100 with tape and surgical mask
I believe that, in expectation, the previous method offers slightly worse protection to third parties than a well-fit valveless medical N95, because our makeshift exhalation valve filter may not be entirely effective.

This section details another technique which may be able to achieve the best of both worlds: the comfort and availability of industrial masks, and the third-party protection offered by valveless masks.

## How we need to modify the respirator
Let's look at how the valves in industrial masks work. I'll be using the Miller LPR-100, but the 3M is built similarly.

The exhalation valve is at the front. There are also two inhalation valves, one on each side between the mouth and the filter. These only allow air to come into the mask from outside, forcing all the exhaled air to go through the exhalation valve (instead of some of it going back through the filter).

<div style="display: flex">

![](../assets/images/mask/miller_valves_0.webp)
![](../assets/images/mask/miller_valves_1.webp)
</div>
_Miller  LPR-100 valves_

We need to disable both the inhalation and exhalation valves:
* The unfiltered exhalation valve should be completely sealed off.
* In order to allow the user to exhale, the inhalation valves need to be turned into simple holes that allow two-way air circulation.

This will mean that both inhaled and exhaled air will go through the P100 filters.

## Exhalation valve
We can seal off the exhalation valve from the outside with tape[^altmethods]. On the Miller respirator, there is a little plastic cage covering the valve, and this cage can be taped over. Note that tape sticks very poorly to the elastomer (the dark blue material on the Miller). This is why I only place tape on the plastic; this seems to be sufficient.

<div style="display: flex">

![](../assets/images/mask/tape_0.webp)
![](../assets/images/mask/tape_1.webp)
</div>
_Tape on exhalation cage_

I am using [painter's tape](https://www.amazon.com/gp/product/B00004Z4DU/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1) because it's supposed to pull off without leaving a residue of glue. It's possible that it would be better to use tape with a stronger adhesive. (A friend of mine commented: "Some ideas for sealing off the exhalation valve: (1) Butyl tape/self-vulcanizing tape. Not so much a sticky tape as a ribbon of moldable putty, so no adhesive residue. This stuff is pretty much unparalleled if you need to make a fully gas- and watertight seal around an irregularly shaped opening in a pinch without making a mess. The fact that it has no adhesive does put some constraints on the geometry of the part you’re sealing off, but I think it would work (better than painter’s tape, at least) on the Miller. (2) Vinyl tape/electrical tape. It’s relatively water-resistant and can be stretched to some extent. The adhesive also sticks to polymers pretty well (although it does leave a lot of residue after some time, but you can clean that off with a bit of IPA).")

You can check the seal of your tape by pressing the mask onto your face and attempting to exhale (with the inhalation valves intact). Air should only be able to escape through the sides of the mask.

## Inhalation valves
The inhalation valves are removable and can be pulled out. They are very thin and feel like they might be about to break when you pull them out, but I have been able to pull four of them out without a problem.

<div style="display: flex">

![](../assets/images/mask/miller_valves_1.webp)
![](../assets/images/mask/valve_hand.webp)
</div>
_Touching a valve (left), a valve after it has been pulled out (right)_

<div style="display: flex">

![](../assets/images/mask/valves_plugs.webp)
![](../assets/images/mask/valves_removed_0.webp)
</div>
_The two inhalation valves (left), the filter now visible through the holes (right)_


Pushing the valves back in is easy.

The tape can be removed and the valves re-inserted, making my modification fully reversible.

[^altmethods]: I tried two other methods before I settled on using tape: gluing a thin silicon wafer over the valve on the _inside_ of the mask, and applying glue to the valve directly. Both these methods are entirely inferior and should not be used.

## Also use a surgical mask
Even if you're using the tape technique, I recommend also covering the respirator with a surgical mask, since this has no downsides and might have some benefit. The seal on the exhalation valve might not be perfect and may get worse over time, so an extra layer of filtration, however imperfect, is a good backup.

It's also beneficial because it makes what you're doing legible to others. You don't want to explain this weird tape business to strangers, even if it's for their protection.

<div style="display: flex">

![](../assets/images/mask/miller_respirator_tom.webp)
![](../assets/images/mask/miller_tape.webp)
![](../assets/images/mask/industrial_w_surgical.webp)
</div>
_Miller LPR-100. Unmodified (left), with tape (middle), with tape and surgical mask (right)_

## Choice of respirator
For this technique, I recommend the [Miller LPR-100](https://www.google.com/search?q=miller+lpr-100)[^m]. 

I recommend the Miller over the 3M because: 
* its build quality feels superior to me
* it looks better
* it blocks less of your field of view

Since the Miller is better than the 3M, and 3M is such a huge player in this market, I think there's a decent chance that the Miller is in fact one of the very best options that exists.

The Miller weighs 139 g., which is a negligible difference to the 3M's 128 g

I also like the fact that you can buy a neat [rigid case](https://www.google.com/search?q=miller%20283374) to hold the Miller respirator. The case is called the 283374.

<div style="display: flex">

![](../assets/images/mask/miller_case_0.webp)
![](../assets/images/mask/miller_case_1.webp)
</div>
_Miller case, 283374_

The Miller model comes with replaceable P100-rated filters, while the 3M can be used with many types of filters and cartridges.

If you want to implement this technique on the 3M, it should be possible; all steps will be similar.

# Potential concerns
The 3M+KN95 method we discussed earlier can be seen as a simple adaptation of CDC guidelines, so I have fewer concerns about it.

However, the tape technique involves a more fundamental alteration. This might seem unwise. How do I know I haven't messed up something crucial, endangering myself and others?

Before discussing the specific concerns, it's useful to consider: what are the relevant alternatives to my recommendation? 

My best guess is that constantly wearing a correctly fitted medical N95, with the really tight elastic bands, is very slightly safer for others in expectation than the tape method (due to risks of things going wrong, like the tape getting unstuck). However, it is not a likely alternative for everyday use. First, in my experience, N95s are more difficult to fit correctly than industrial masks. Second, for me, these respirators are prohibitively uncomfortable. I have seen few people use them. I think the realistic alternatives for most people are cloth and surgical masks. I am relatively confident that both of my techniques are an improvement on that, for both the user and third parties.

<!-- The probability mass I assign to harm comes mostly from unknown unknowns and the fact that official agencies don't recommend my technique, not from any specific evidence of risks. -->

<!-- I currently don't plant to prioritize writing a full detailed justification of these beliefs for a sceptical audience. Writing such a thing is a great deal of effort and there are benefits to getting the idea out earlier. In order to let you come to the best conclusion for you given your knowledge and risk tolerance, I'm trying to lay out most of the evidence against my proposal that I've considered (without giving the full reasoning for why I find this evidence insufficiently persuasive on balance). -->

By the way, I am not an expert in disease control. I studied economics and philosophy and then worked as a researcher.

## Repeated use
Healthcare N95s are supposed to be used only once before being decontaminated. However, I plan to use the same filters many times. Is this a problem?

Why are N95s supposed to be used once? According to this [CDC guidance](https://www.cdc.gov/niosh/topics/hcwcontrols/recommendedguidanceextuse.html), 

> the most significant risk [of extended use and reuse] is of contact transmission from touching the surface of the contaminated respirator. ... Respiratory pathogens on the respirator surface can potentially be transferred by touch to the wearer’s hands and thus risk causing infection through subsequent touching of the mucous membranes of the face. ...
> 
> While studies have shown that some respiratory pathogens remain infectious on respirator surfaces for extended periods of time, in microbial transfer [touching the respirator] and reaerosolization [coughing or sneezing through the respirator] studies more than ~99.8% have remained trapped on the respirator after handling or following simulated cough or sneeze.

Since I plan to leave the respirator unused for hours or days between each use, and any viral dose on the exterior of the filters is likely to be very small, I don't think this is a huge concern overall. I am very open to contrary evidence.

By the way, based on this guidance, it seems to me we should also worry less about reusing respirators and masks in general, even without decontamination. (Decontamination makes a lot more sense for health care workers who are exposed to COVID patients).

It's good to remember to avoid touching the filters.

## CDC guidelines
As explained above, the CDC recommends a surgical or cloth mask to cover the valve. There is no evidence that they considered either of the techniques I described above when issuing their blog post.

The tape method is a greater deviation from the CDC guidelines than the KN95-covering method, so if you care about following official guidance you could use the latter.

## Concerns specific to tape method
I assign a relatively low chance that the tape method is worse than the CDC recommendation of covering the valve with a surgical mask (my views depend considerably on the tightness of the surgical mask seal). 
and a very low chance that it's worse than a surgical mask alone. The probability mass I assign to harm is a combination of concerns about exhaling through the filter reducing its efficacy, and unknown unknowns.

### C02 rebreathing
Without the valves, part of the air you inhale will be air that you just exhaled, which contains more C02. I have not personally noticed any effects from this.

### Exhaling through filter
Could exhaling through the filter be a bad thing somehow? I wasn't able to find any source making an explicit statement on this, but I think it's unlikely to be a problem.

One reason to worry is that the founder of [Narwall Mask](https://narwallmask.com/) has told me that, according to one filtration expert he spoke to, one-way airflow greatly prolongs the life of the filters compared to two-way airflow. However, based on my small amount of research, I don't think the life of the filters would be affected to a degree that is practically important.

The MSA valveless elastomeric respirator that I mentioned in this footnote[^MSA] appears to have filters that can be used for more than 1 month of daily use during the workday; and moreover, we can see in the respirator's [brochure](https://msa.webdamdb.com/directdownload.php?ti=42341334&tok=sKRw3WQqRXhcJ/V4EfuwtARR) that these filters, with model number 815369, are the same as those that are used in MSA's line of regular, valved elastomeric respirators (see [here](http://msa.webdamdb.com/bp/#/folder/1749983/50030424)). From this I conclude that: two-way airflow through regular P100 filters was considered an acceptable design choice by MSA; and these filters can be used two-way for at least a month of hospital use.

In addition, healthcare N95s (without valves) are designed to be exhaled through. They are only rated for a day of use, but I believe this is _not_ because the filter loses efficacy (see [section on repeated use](#repeated-use)).

Exhaled air has a [relative humidity](https://en.wikipedia.org/wiki/Humidity#Relative_humidity) close to 100%. Could exposure to humid air reduce the efficacy of the filters? In [this study](https://academic.oup.com/annweh/article/59/5/629/2196149) of N95 filters, the difference penetration rose from around 2% to around 4% when relative humidity went from 10% to 80%, and this effect increased with duration of continuous use. The flow rate was 85 L/min.

![](../assets/images/mask/humidity_0.webp)
_Combination of figures 3 and 5, [Mahdavi et al.](https://academic.oup.com/annweh/article/59/5/629/2196149)_

Note that this study, which simulates inhalation of humid air, does not address (except very indirectly) the question of how the _exhalation_ humidity affects the _inhalation_ filtration.

### Discussion of tape technique by others
* [This NIOSH study](https://www.cdc.gov/niosh/docs/2021-107/pdfs/2021-107.pdf?id=10.26616/NIOSHPUB2021107) tested three modifications of valved respirators: covering the valve on the interior with surgical tape, covering the valve on the interior with an electrocardiogram (ECG) pad, and stretching a surgical mask over the exterior of the respirator.
    * They found that "penetration was 23% for the masked-over mitigation; penetration was 5% for the taped mitigation; penetration was 2% for the [ECG pad] mitigation". I would be very interested in more discussion of why the ECG pad did so much better than the surgical tape, the authors don't say much. One guess could be that the ECG pad has a more powerful adhesive, which would suggest that it's important to choose a strongly adhesive tape if implementing my technique.
    * When discussing the choice of modification strategies, the authors wrote that "two concerns are that the adhesive could pull away from the surface, thereby not blocking airflow to the same degree over time, and that these adhesives could contain chemicals that have toxicological effects."
![study](../assets/images/mask/niosh_study.webp)
* In an [FAQ released by 3M](https://multimedia.3m.com/mws/media/1791526O/respiratory-protection-faq-general-public-tb.pdf), in response to the question of whether one should tape over the exhalation valve, they wrote "3M does not recommend that tape be placed over the exhalation valve", but do not give any reasons for this beyond the fact that it may become "more difficult to breathe through ... if the exhalation valve is taped shut". 
* The state of Maine's Department of Public Safety [recommends against tape-covering](https://www.maine.gov/ems/sites/maine.gov.ems/files/inline-files/2020-08-21%20Operational%20Bulletin%20Regarding%20Masks%20with%20Exhalation%20Valves.pdf), but merely because "this would be considered altering the device and violates the manufacturer’s recommendation".



[niosh]: https://en.wikipedia.org/wiki/NIOSH_air_filtration_rating

[^m]: The model number is ML00895 for the M/L size, and ML00894 for the S/M size.

# Overall recommendation
I think it's about 50/50 which of my two methods is better all things considered. They're close enough that I think the correct decision depends on how much you care about protecting yourself vs source control. If source control is a minor consideration to you, I'd go with the KN95 valve coverage method, otherwise the tape method.

(As I said in a previous footnote[^MSA], if a valveless elastomeric mask is widely available by the time you read this, that is absolutely a superior option to the hacks I have developed.)

(The [Narwall Mask](https://narwallmask.com/) is a commercial solution based on a snorkel mask that may be appealing if you don't mind (i) the lack of NIOSH-approval and (ii) buying from a random startup, and (iii) you don't mind or even prefer the full-facepiece design.)
