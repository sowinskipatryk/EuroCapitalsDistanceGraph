from geopy.distance import geodesic
import networkx as nx
import matplotlib.pyplot as plt


capitals_coordinates = {
    "Amsterdam": (52.3676, 4.9041),
    "Andorra la Vella": (42.5078, 1.5211),
    "Ankara": (39.9334, 32.8597),
    "Athens": (37.9838, 23.7275),
    # "Baku": (40.4093, 49.8671),
    "Belgrade": (44.7866, 20.4489),
    "Berlin": (52.5200, 13.4050),
    "Bern": (46.9481, 7.4474),
    "Bratislava": (48.1486, 17.1077),
    "Brussels": (50.8503, 4.3517),
    "Bucharest": (44.4268, 26.1025),
    "Budapest": (47.4979, 19.0402),
    "Chisinau": (47.0105, 28.8638),
    "Copenhagen": (55.6761, 12.5683),
    "Dublin": (53.3498, -6.2603),
    "Helsinki": (60.1695, 24.9355),
    "Kiev": (50.4501, 30.5234),
    "Lisbon": (38.7169, -9.1399),
    "Ljubljana": (46.0569, 14.5058),
    "London": (51.5074, -0.1278),
    "Luxembourg": (49.6117, 6.13),
    "Madrid": (40.4168, -3.7038),
    "Minsk": (53.9045, 27.5615),
    "Monaco": (43.7384, 7.4246),
    "Moscow": (55.7558, 37.6176),
    "Nicosia": (35.1856, 33.3823),
    # "Nur-Sultan": (51.1694, 71.4491),
    "Oslo": (59.9139, 10.7522),
    "Paris": (48.8566, 2.3522),
    "Podgorica": (42.4413, 19.2636),
    "Prague": (50.0755, 14.4378),
    "Pristina": (42.6629, 21.1655),
    "Reykjavik": (64.1355, -21.8954),
    "Riga": (56.9496, 24.1052),
    "Rome": (41.9028, 12.4964),
    "San Marino": (43.9333, 12.45),
    "Sarajevo": (43.8563, 18.4131),
    "Skopje": (41.9973, 21.4280),
    "Sofia": (42.6977, 23.3219),
    "Stockholm": (59.3293, 18.0686),
    "Tallinn": (59.4370, 24.7535),
    # "Tbilisi": (41.7151, 44.8271),
    "Tirana": (41.3275, 19.8189),
    "Vaduz": (47.1410, 9.5209),
    "Valletta": (35.8997, 14.5147),
    "Vatican City": (41.9029, 12.4534),
    "Vienna": (48.2082, 16.3738),
    "Vilnius": (54.6872, 25.2797),
    # "Yerevan": (40.1792, 44.4991),
    "Warsaw": (52.2297, 21.0122),
    "Zagreb": (45.8150, 15.9819),
    }

distances = {}
for city1 in capitals_coordinates:
    for city2 in capitals_coordinates:
        if city1 != city2:
            lat1, lon1 = capitals_coordinates[city1][0], capitals_coordinates[city1][1]
            lat2, lon2 = capitals_coordinates[city2][0], capitals_coordinates[city2][1]

            distance = int(geodesic((lat1, lon1), (lat2, lon2)).kilometers)
            distances[(city1, city2)] = distance

G = nx.Graph()

for city, coord in capitals_coordinates.items():
    G.add_node(city, pos=coord)

for (city1, city2), distance in distances.items():
    G.add_edge(city1, city2, weight=distance)

pos = nx.get_node_attributes(G, 'pos')

plt.figure(figsize=(45, 30))
nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10, font_weight="bold", edge_color="gray")

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

plt.title("Euro Capitals Distance Graph")

# plt.show()
plt.savefig('euro_capitals_distance_graph.png', bbox_inches='tight', dpi=300)
