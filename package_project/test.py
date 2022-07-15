import pycountry

# get state list

cities = list(pycountry.subdivisions)

subs = pycountry.subdivisions.get(country_code='ZW')

sub_name = []
sub_code = []
div_list = []   # add to widgets

for sub in subs:
    sub_name.append(sub.name)
    sub_code.append(sub.country_code)

# div_list.append([list(x) for x in zip(sub_code, sub_name)])
div_list.extend(x for x in zip(sub_code, sub_name))
print(div_list)