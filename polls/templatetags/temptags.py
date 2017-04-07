from django import template
import math

register = template.Library()

@register.filter
def roundoff(value):
	"""round off value to arg number of digits"""
	return math.ceil(value*100)/100 # input: 8.8333333333333339, output: 8.84
	