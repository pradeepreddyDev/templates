# templates

https://djangobook.com/mdj2-django-templates/

- Display Logic. E.g. {% if %}...{% endif %}
- Loop Control. E.g. {% for x in y %}...{% endfor %}
- Block Declaration. E.g. {% block content %}...{% endblock %}
- Content Import. E.g. {% include "header.html" %}
- Inheritance. E.g. {% extends "base.html" %}

Template variables don’t just handle simple data, they work with more complex data structures too. For example:

- Simple Variable. E.g. {{ title }}
- Object Attribute. E.g. {{ page.title }}
- Dictionary Lookup. E.g. {{ dict.key }}
- List Index. E.g. {{ list_items.0 }}
- Method Call. E.g. {{ var.upper }}

Filters modify a variable for display. A filter is applied to a variable using the pipe (|) character. There are dozens of built-in filters, here are some examples:

- Change Case. E.g. {{ name|title }} or {{ units|lower }}
- Truncation. E.g. {{ post_content|truncatewords:50 }}
- Date Formatting. E.g. {{ order_date|date:"D M Y" }}
- List Slicing. E.g. {{ list_items|slice:":3" }}
- Default Values. E.g. {{ item_total|default:"nil" }}
