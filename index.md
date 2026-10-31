---
layout: default
title: Home
---

# Hi, I am Rajesh.

I am a software engineer in Chennai, India. I co-founded [Indix](/work/#indix) in 2012 and led its data platform and machine learning teams. Avalara bought Indix in 2019, and I led NLP and classification teams there. Before Indix I was a tech lead on GoCD at ThoughtWorks. I [give talks](/work/#talks) on data pipelines and machine learning.

Outside work I play board games, photograph birds, play badminton and take part in quizzes. Lately I think and write a lot about AI.

This site is my scratchpad. Some posts are finished. Many are notes.

## Topics

<ul class="topics">
{% for t in site.topics %}
  <li><a href="{{ t.url | relative_url }}">{{ t.name }}</a></li>
{% endfor %}
</ul>

## Recent writing

{% include post-list.html posts=site.posts limit=10 %}

[All writing](/writing/)
