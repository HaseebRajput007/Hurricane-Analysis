# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
damages_in_float = []
def damage_into_float(datas):
  for data in datas:
    if data[-1] == "M":
      damages_in_float.append(float(data[:-1])*1000000)
    elif data[-1] == "B":
      damages_in_float.append(float(data[:-1])* 1000000000)
    else:
      damages_in_float.append(data)

damage_into_float(damages)
# print(damages_in_float)

# write your construct hurricane dictionary function here:

hurricane_records = {}
def hurricane_data(names, months, years, max_sustained_winds, areas_affected, deaths):
  for index in range(len(names)):
    hurricane_records[names[index]] = {"Name": names[index],"Month": months[index],"Year": years[index],"Max Sustained Wind": max_sustained_winds[index],"Areas Affected": areas_affected[index],"Damage": damages[index],"Deaths": deaths[index]}

hurricane_data (names, months, years, max_sustained_winds, areas_affected, deaths)

print("=========================")
# print(hurricane_records)

# write your construct hurricane by year dictionary function here:
by_year = {}
def hurricanes_by_year(hurricane_records):
    for key,value in hurricane_records.items():
      # print(value)
      current_year = value["Year"]
      # print(current_year)
      if  not (current_year in by_year):
        by_year[current_year] = [value]
      elif current_year in by_year:
        by_year[current_year].append(value)

hurricanes_by_year(hurricane_records)
print("=========================")
print(by_year)

# write your count affected areas function here:

affected_count = {}
# print(areas_affected)
def affected_area(areas_affected):
  for countries in areas_affected:
    for country in countries:
      if not(country in affected_count):
        affected_count[country] = 1
      else:
        affected_count[country] += 1

affected_area(areas_affected)
print("=========================")
# print(affected_count)

# write your find most affected area function here:

def most_affected_country(affected_count):
  most_affect = 0
  cntry = ""
  for country , count in affected_count.items():
    if count > most_affect :
      most_affect = count
      cntry = country
  return cntry, most_affect
print("=========================")
# print(most_affected_country(affected_count))

# write your greatest number of deaths function here:

def most_deaths(hurricane_records):
  most_death = 0
  hurricane = ""
  for key , value in hurricane_records.items():
    death_count = value["Deaths"]
    if most_death < death_count:
      most_death = death_count
      hurricane = key
  return hurricane , most_death
print("=========================")
# print(most_deaths(hurricane_records))
    
# write your catgeorize by mortality function here:
hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
def rates_hurricanes(hurricane_records):
  for key,value in hurricane_records.items():
    deaths = value["Deaths"]
    if deaths == 0:
      hurricanes_by_mortality[0].append(key)
    elif deaths >0 and deaths <=100:
      hurricanes_by_mortality[1].append(key)
    elif deaths >100 and deaths <=500:
      hurricanes_by_mortality[2].append(key)
    elif deaths > 500 and deaths <= 1000:
      hurricanes_by_mortality[3].append(key)
    else:
      hurricanes_by_mortality[4].append(key)

rates_hurricanes(hurricane_records)
print("=========================")
# print(hurricanes_by_mortality)

# write your greatest damage function here:

def greates_damage(damages_in_float):
  max = 0 
  for damage in damages_in_float:
    if damage == 'Damages not recorded':
      continue
    elif max < damage :
      max = damage
  return max

print("=========================")
# print(greates_damage(damages_in_float))

# write your catgeorize by damage function here:

damage_rate = {0:[], 1:[], 2:[], 3:[], 4:[]}
def rate_hurricane_damage(damages_in_float):
  for damage in damages_in_float:
    if (damage == "Damages not recorded") or (damage <= 0):
      damage_rate[0].append(damage)
    elif (damage <=100000000):
      damage_rate[1].append(damage)
    elif (damage <= 1000000000):
      damage_rate[2].append(damage)
    elif (damage <= 10000000000):
      damage_rate[3].append(damage)
    else:
      damage_rate[4].append(damage)
  return damage_rate


print("=========================")
# print(rate_hurricane_damage(damages_in_float))

    






