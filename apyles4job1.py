import json
import requests
from pathlib import Path
import urllib.parse


class WikiCountries:

    def __init__(self, file_json):
        self.host = "https://en.wikipedia.org/wiki"
        self.cursor = None
        self.file_json = file_json
        self.country_list = []

    def __iter__(self):
        with open(self.file_json, 'r', encoding='UTF-8') as fh:
            self.country_list = json.loads(fh.read())
        return self

    def __next__(self):
        if len(self.country_list) == 0:
            raise StopIteration
        country_name = self.country_list.pop(0)["name"]["common"]
        country_parse = urllib.parse.quote(country_name)
        country_ref = f'{self.host}/{country_parse}'
        return country_name, country_ref, self.call_wiki(country_ref)

    def call_wiki(self, link):
        response = requests.get(link)
        return response.raise_for_status()


p = Path('.')
f_name = p.cwd() / 'countries.json'
countries_ref = WikiCountries(f_name)
with open("country_refs.txt", "w", encoding='utf8') as f:
    for country_name, country_href, r_status in countries_ref:
        if r_status:
            s = f'{country_name} -> None\n'
        else:
            s = f'{country_name} -> {country_href}\n'
        f.write(s)
        # print(country_name, country_ref, r_status)
