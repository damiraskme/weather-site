from django.forms import Form, CharField

class locForm(Form):
  location = CharField(label="Enter location (city, zipcode):", max_length=200)
