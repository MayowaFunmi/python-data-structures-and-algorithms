import pycountry


class Country:
    def __init__(self):
        pass

    def all_countries(self):
        country_list = []
        countries = list(pycountry.countries)

        for country in countries:
            country_list.append(country.name)
        return country_list

    def print(self):
        pass

    def count_country(self):
        return len(self.all_countries())

    def countries_with_alpha(self):
        countries = list(pycountry.countries)

        country_name = []
        country_code = []
        country_list = []  # add to widgets

        for country in countries:
            country_name.append(country.name)
            country_code.append(country.alpha_2)

        country_list.extend(a for a in zip(country_code, country_name))
        return country_list

    def search_country(self, country_name):
        search = pycountry.countries.search_fuzzy(country_name)
        query = {}
        try:
            for data in search:
                query['alpha_2'] = data.alpha_2
                query['alpha_3'] = data.alpha_3
                query['flag'] = data.flag
                query['name'] = data.name
                query['numeric'] = data.numeric
                try:
                    query['official_name'] = data.official_name
                except:
                    query['official_name'] = 'Official Name Not Available'
            return query
        except:
            return f'Country {country_name} not on the list. Try again with another name'

    def states_in_country(self, country_name):
        search = pycountry.countries.search_fuzzy(country_name)
        country_code = ''
        for data in search:
            country_code = data.alpha_2
        subs = pycountry.subdivisions.get(country_code=country_code)
        sub_name = []
        sub_code = []
        div_list = []  # add to widgets

        for sub in subs:
            sub_name.append(sub.name)
            sub_code.append(sub.country_code)

        # div_list.append([list(x) for x in zip(sub_code, sub_name)])
        div_list.extend(x for x in zip(sub_code, sub_name))
        div_list = sorted(div_list)
        return div_list


if __name__ == '__main__':
    c = Country()
    print(c.states_in_country('united kingdom'))