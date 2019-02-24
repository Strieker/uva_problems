import sys
import re
first = True
countries_and_women = {};
for line in sys.stdin:
   line = line.strip()
   if not first:
       (country, woman) = line.split(" ", 1)
       if country in countries_and_women:
           countries_and_women[country].add(woman)
       else:
           countries_and_women[country] = set([woman])
   first = False
for country in sorted(countries_and_women.keys()):
   print(country + " " + str(len(countries_and_women[country])))
