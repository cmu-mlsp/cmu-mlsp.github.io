---
title: "MLSP Group - Publications"
layout: gridlay
excerpt: "MLSP Group -- Publications."
sitemap: false
permalink: /publications/
---


{% for year in (1976..2024) reversed %}

### {{ year }}

{% assign number_printed = 0 %}
{% for publi in site.data.publist %}
{% if publi.year == year %}

<div class="row">
<div class="col-sm-12 clearfix">
 <div class="row">
  <a class="pub1" href="{{ publi.url }}">{{ publi.title }}</a><br>
  <a class="pub2">{{ publi.authors }}</a>
  <a class="pub2"><i>{{ publi.venue }}</i> {{ publi.year }}</a>
 </div>
</div>
</div>

{% endif %}
{% endfor %}
{% endfor %}