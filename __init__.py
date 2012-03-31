import re
from django import forms
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe

def replace(match):
    _content = match.group(0)
    _errors = match.group(1)
    _type = match.group(3)
    if _type == 'checkbox' or _type == 'radio':
        _class = 'ym-fbox-check'
    elif _type == 'submit' or _type == 'button' or _type == 'reset':
        _class = 'ym-fbox-button'
    elif _content.find('<select') > -1:
        _class = 'ym-fbox-select'
    else:
        _class = 'ym-fbox-text'
    if _errors:
        _class += ' ym-fbox-error'
        _content = _content.replace(_errors, strip_tags(_errors))
    return _content.replace('class="row"', 'class="%s"' % _class)

def as_yaml(self):
    "Returns this form rendered as HTML <div>s."
    return mark_safe(re.sub(r'<div class="row"><p class="ym-message">(.*?)</p>(.+?)type="(.+?)"(.+?)</div>', replace, self._html_output(u'<div class="row"><p class="ym-message">%(errors)s</p>%(label)s%(field)s%(help_text)s</div>', u'%s', '</div>', u'<small class="ym-message">%s</small>', False)))

forms.ModelForm.as_yaml = as_yaml
