# Django Classnames Tag
Provides a template tag to create css classnames easily.
Inspired by JedWatson/classnames

## Installation
```
$ pip install django-classnames-tag
```

Add the app to INSTALLED_APPS:
```
INSTALLED_APPS += ['django_classnames_tag']
```


## Usage
```
{% classnames <classname>=<bool> <classname>=<value>|eq:3 <classname>=<value>|lte:2 %}
```

Example:
```
{% load classnames %}

<a class="{% classnames success=obj.percentage|gte=90 danger=obj.percentage|lte:10 %}">...</a>
```

There are a bunch of helper filters available:
```
lte, lt, eq, gt, gte
```
