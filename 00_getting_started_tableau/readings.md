# Readings for the course

## Week 0: Readings for Getting Started

Much of the readings for this course are taken from popular
publications that do a good job of communicating arguments using
data. 

1. [Bussed out. How America Moves its homeless](https://www.theguardian.com/us-news/ng-interactive/2017/dec/20/bussed-out-america-moves-homeless-people-country-study)

'Bussed out' required journalists to engage in large-scale data
collection and significant data analysis, along with the resulting
storytelling and visualization. The story excels at humanizing the
problem while maintaining perspective about the magnitude of the
problem.

2. [Hidden spy planes](https://www.buzzfeednews.com/article/peteraldhous/hidden-spy-planes)

'Hidden spy planes' uses data and machine learning to enable an
investigation into mysterous military-like aircraft in American
airspace. Making public claims based on such data-driven results
requires careful reasoning and verification -- indeed, the machine
learning was merely the start of the investigation.

3. [French election results: Macron’s victory in charts](https://www.ft.com/content/62d782d6-31a7-11e7-9555-23ef563ecf9a)

This Financial Times article visually describes the French election
results along a number of commonly used dimensions: geography, age,
income level, education level, and passing time.

## Week 1: Don't trust your data!

1. Gaming the college rankings

College Rankings are derived from models that are supposed to capture
what makes a school successful. However, as college rankings influence
the future success of colleges, many schools try to game the ranking
system -- i.e. the rankings changing what they are attempting
to measure. This is commonly referred to as a "feedback loop".

These stories touch on a few few common themes: that you shouldn't
trust data at face value, that you should try to be aware of *how*
your data is created, and that messy data, such missing data, can
drastically effect the statistics of what's being measured.

* [How Big Data Transformed Applying to College](http://www.slate.com/articles/business/moneybox/2016/09/how_big_data_made_applying_to_college_tougher_crueler_and_more_expensive.html)
  
* [College Ranking Models](https://mathbabe.org/2013/08/26/college-ranking-models/)
     
* [Jukin' the Stats](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2779183)
      

## Week 2: Constructing arguments out of our measurements


1. [The media has a probability problem](https://fivethirtyeight.com/features/the-media-has-a-probability-problem/)


2. [We’re Measuring the Economy All Wrong](https://www.nytimes.com/2018/09/14/opinion/columnists/great-recession-economy-gdp.html)
   
Much of working in data science consists of translating your intuition
into quantitative measurements. The NY Times article discusses the
historical circumstances under which unemployment rates were first
measured. Over the years, myriad policy decisions have been made based
on this measurement. While the economy is experiencing record low
unemployment rates, there are other aspects that aren't capture with
this statistic (such as rising inequality). 

3. [New Statistical Methods](https://fivethirtyeight.com/features/a-flawed-statistical-method-was-just-banned-from-a-major-sports-science-journal/)

Once we decide on what we want to measure, we have to construct an
argument using those measurements. Generally, different subject
domains have different norms and standards for what makes a convincing
argument. However, when certain questions remain stubbornly
intractable to existing "standard" analyses, researchers will use
new or nonstandard techniques to try to make their point. Sometimes
these techniques become accepted and sometime they are deemed
unconvincing.



## Week 3: Summarizing with visualizations

1. [women in congress](https://pudding.cool/2018/07/women-in-congress/) 

2. [murder rates don't tell us everything about gun violence](https://fivethirtyeight.com/features/murder-rates-dont-tell-us-everything-about-gun-violence/)

3. [San Diego PD traffic stops
analysis](http://www.sandiegouniontribune.com/news/public-safety/sd-me-traffic-stops-20161202-story.html)




## Week 4: Digital imags and their (mis)uses. 

1. Scientific Racism's new face:

https://medium.com/@blaisea/physiognomys-new-clothes-f2d4b59fdd6a

2. Don't trust your data: how to spot photoshopped images.

http://blackhat.com/presentations/bh-dc-08/Krawetz/Whitepaper/bh-dc-08-krawetz-WP.pdf

3. An exploration into predicting someones gender from their face.

http://gendershades.org/index.html


## Week 5: You are willingly wiretapping yourself?

1. Home assistants

Home assistants like Alexa, Siri, and Google Home provide users with
science-fiction levels of convenience at the expense of an incredible
amount of intimate user-data being collected and analyzed. These
readings paint a picture of the dangers of such convenience.

An introductory article to the unfolding problem in the New York Times:

[Hidden command audio attacks](https://www.nytimes.com/2018/05/10/technology/alexa-siri-hidden-command-audio-attacks.html)

The paper describing a simple approach toward "hidden audio attacks"
is relatively easy to understand. Though these techniques have
dramatically improved (e.g. hiding commands in arbitrary youtube
videos) since publication, this article is worth reading:

[Cocaine Noodles: Exploiting the Gap between Human and Machine Speech Recognition](https://www.usenix.org/system/files/conference/woot15/woot15-paper-vaidya.pdf)

This webpage gives a demo of how to hide audio commands:

[Audio Adversarial Examples](https://nicholas.carlini.com/code/audio_adversarial_examples/)


2. Music

[How does Spotify know you so well?](https://medium.com/s/story/spotifys-discover-weekly-how-machine-learning-finds-your-new-music-19a41ab76efe)

3. The Hidden Cost of Machine Learning

Alexa is just a small column that sits on your counter, but behind it
is a hidden, massive, human effort.

[Anatomy of an AI System](https://anatomyof.ai/)

# week 6: Fairness and Bias in unstructured text

1. Word Embeddings

The following articles explore a popular method of processing english
text (the word2vec algorithm) and how it encodes societal biases of
the training data.

- [Introduction to word embeddings](https://www.technologyreview.com/s/519581/how-google-converted-language-translation-into-a-problem-of-vector-space-mathematics/)
- [Gender bias in word embeddings](https://www.technologyreview.com/s/602025/how-vector-space-mathematics-reveals-the-hidden-sexism-in-language/)
- [Using bias in word embeddings for historical analyses](https://arxiv.org/pdf/1711.08412.pdf)


# week 7: Fairness and Bias

2. Ethics Case Studies

The following case studies get you thinking about various ways data is
being used to build systems and make decisions -- and the thorny
consequences of these methods. Pick a few case studies from the list.

https://aiethics.princeton.edu/case-studies/
1. While it's often the case that it's impossible to setup an
   randomized controlled trial to answer a causal question,
   conclusions drawn from obvservational studies should be approached
   with caution.
   
   [RCTs vs Observational Studies](https://www.nytimes.com/2018/08/06/upshot/employer-wellness-programs-randomized-trials.html)

2. Read the introduction of a new fairness in machine learning book.

   [Fairness in Machine
   Learning](https://fairmlbook.org/pdf/fairmlbook.pdf)

3. (Un)Controlled experiments on the web

[We Experiment on Human Beings!](https://github.com/afraenkel/DSC96/blob/master/projects/06.Prediction/We%20Experiment%20On%20Human%20Beings!%20%E2%80%93%20The%20OkCupid%20Blog.pdf)


## Week 8: Machine Learning in criminal justice

### Recidivism Report. 

Either of the following:
* https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing
* https://www.themarshallproject.org/2015/08/04/the-new-science-of-sentencing


## Week 9: Conclusion


