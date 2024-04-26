---
title: "MLSP Group - Publications"
layout: gridlay
excerpt: "MLSP Group -- Publications."
sitemap: false
permalink: /publications/
---


## Conference Papers

{% assign number_printed = 0 %}
{% for publi in site.data.publist %}

{% if publi.type == 1 %}

<div class="row">

<div class="col-sm-12 clearfix">
 <div class="row">
  <img src="{{ site.url }}{{ site.baseurl }}/images/pubpic/{{ publi.image }}" class="img-responsive" width="25%" style="float: left" />
  <p><a class="pub1" href="{{ publi.link.url }}">{{ publi.title }}</a></p>
  <a class="pub2"> {{ publi.link.display }} </a>
 </div>
</div>

{% endif %}
{% endfor %}

<p> &nbsp; </p>

## Journal Papers

{% assign number_printed = 0 %}
{% for publi in site.data.publist %}

{% if publi.type == 2 %}

<div class="row">

<div class="col-sm-12 clearfix">
 <div class="row">
  <img src="{{ site.url }}{{ site.baseurl }}/images/pubpic/{{ publi.image }}" class="img-responsive" width="25%" style="float: left" />
  <p><a class="pub1" href="{{ publi.link.url }}">{{ publi.title }}</a></p>
  <a class="pub2"> {{ publi.link.display }} </a>
 </div>
</div>

{% endif %}
{% endfor %}

<p> &nbsp; </p>

## Patents

{% assign number_printed = 0 %}
{% for publi in site.data.publist %}

{% if publi.type == 3 %}

<div class="row">

<div class="col-sm-12 clearfix">
 <div class="row">
  <p><a class="pub1" href="{{ publi.link.url }}">{{ publi.title }}</a></p>
  <a class="pub2"> {{ publi.link.display }} </a>
 </div>
</div>

{% endif %}
{% endfor %}

<p> &nbsp; </p>

---

<div>

<br><br><br>

</div>

