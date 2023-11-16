Rivers = {
'Nile': 'Egypt',
'Ganga': 'India',
'Amazon': 'Colombia/Peru',
'Mississippi': 'United States',
}
for River, country in Rivers.items():
    print("The " + River + " flows Within " + country.title() + ".")

print("\nThese following rivers are included within this data set:")
for River in Rivers.keys():
    print("- " + River)

print("\nThese following countries are included within this data set:")
for country in Rivers.values():
    print("- " + country)