---
layout: topic
title: Board Games
topic: boardgames
permalink: /boardgames/
---

Games I play, games I like, and small tools I build for them.

Things I have built:

- [Sagrada scoreboard](https://github.com/codingnirvana/sagrada-scoreboard), a score keeper for Sagrada.
- [Chain-Link](https://github.com/codingnirvana/chain-link), a word game where you guess the next word in a chain of common phrases.
- [Word Racer tournament results](https://github.com/codingnirvana/wordracer-results) from a tournament at Indix in 2017.

## My collection

{{ site.data.boardgames | size }} games, synced weekly from [BoardGameGeek](https://boardgamegeek.com/collection/user/codingnirvana?own=1&subtype=boardgame).

<ul class="game-list">
{% assign games = site.data.boardgames | sort: "name" %}
{% for g in games %}
  <li><a href="https://boardgamegeek.com/boardgame/{{ g.bgg_id }}">{{ g.name }}</a>{% if g.year %} <span class="year">{{ g.year }}</span>{% endif %}</li>
{% endfor %}
</ul>

## Games I have played

{% assign played = site.data.plays %}{% assign total = 0 %}{% for g in played %}{% assign total = total | plus: g.plays %}{% endfor %}
{{ total }} plays of {{ played | size }} games. Most come from plays my friends logged on BoardGameGeek and tagged me in. Synced weekly.

<ul class="game-list">
{% for g in played %}
  <li><a href="https://boardgamegeek.com/boardgame/{{ g.bgg_id }}">{{ g.name }}</a> <span class="year">{{ g.plays }} {% if g.plays == 1 %}play{% else %}plays{% endif %}</span></li>
{% endfor %}
</ul>
