---
title: "MLSP Group - Research"
layout: gridlay
excerpt: "MLSP Group -- Research"
sitemap: false
permalink: /projects/vpc/
---

## 

### Project Members 

{% assign member_names = "Kashu Yamazaki" | split: "," %}

{% for member in site.data.team_members %}
{% if member_names contains member.name %}
<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4><a href="{{ site.url }}{{ site.baseurl }}/team/{{ member.url }}" class="off">{{ member.name }}</a></h4>
  <i>{{ member.info }}</i>
</div>
{% endif %}
{% endfor %}