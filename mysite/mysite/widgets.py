def dropdown(cls, choice):
	attrs = {
		'class': "extra-widget extra-widget-dropdown",
	}
	return ChoiceField(
		required=False,
		choices=project_name(choice)
		widget=Select(attrs=attrs)
	)
