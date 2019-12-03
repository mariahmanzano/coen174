# Widget to allow for selection from a dropdown menu.
# Picks from different porjects in a dropdown.
def dropdown(cls, choice):
	attrs = {
		'class': "extra-widget extra-widget-dropdown",
	}
	return ChoiceField(
		required=False,
		choices=project_name(choice)
		widget=Select(attrs=attrs)
	)
