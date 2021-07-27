#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}

moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']
distance_moscow_london = ((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** 0.5
distance_moscow_paris = ((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** 0.5
distance_london_paris = ((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** 0.5

distances['Moscow'] = {}
distances['London'] = {}
distances['Paris'] = {}
distances['Moscow']['London'] = distance_moscow_london
distances['Moscow']['Paris'] = distance_moscow_paris
distances['London']['Moscow'] = distance_moscow_london
distances['London']['Paris'] = distance_london_paris
distances['Paris']['Moscow'] = distance_moscow_paris
distances['Paris']['London'] = distance_london_paris

print(distances)




