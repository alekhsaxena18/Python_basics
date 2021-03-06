import folium,pandas

df=pandas.read_csv('Volcanoes-USA.txt')
map=folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=6)


def color(elev):
    minimum=int(min(df['ELEV']))
    step=int((max(df['ELEV'])-min(df['ELEV']))/3)
    if elev in range(minimum,minimum+step):
        col='green'
    elif elev in range(minimum+step,minimum+step*2):
        col='pink'
    else:
        col='blue'
    return col


for lat,lon,names,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    map.simple_marker(location=[lat,lon],popup=names,marker_color=color(elev))

map.create_map(path='test.html')
