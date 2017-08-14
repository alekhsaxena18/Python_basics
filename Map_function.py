##Map Function

people=['Dr. chis brook','dr alu sax','dr Bhalu']

def split_tile_name(person):
    title = person.split()[0]
    last_name = person.split()[-1]
    return title+' '+last_name
    #return '{}{}'.format(title,last_name)

print(list(map(split_tile_name,people)))

print(map(split_tile_name,people))
#print(split_tile_name(people))
