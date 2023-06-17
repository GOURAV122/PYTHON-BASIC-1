days=374
years=(days/365)
weeks=(days%365)/7
#days=(((years*365)+(weeks*7))-days)
days=(days%365)%7
print(int(years),int(weeks),int(days))
