#!/bin/bash
wget http://data.insideairbnb.com/united-states/ma/boston/2017-10-06/data/listings.csv.gz
wget http://data.insideairbnb.com/united-states/ma/boston/2017-10-06/data/calendar.csv.gz
wget http://data.insideairbnb.com/united-states/ma/boston/2017-10-06/data/reviews.csv.gz
gunzip listings.csv.gz
gunzip calendar.csv.gz
gunzip reviews.csv.gz
wget http://data.insideairbnb.com/united-states/ma/boston/2017-10-06/visualisations/neighbourhoods.csv
wget http://data.insideairbnb.com/united-states/ma/boston/2017-10-06/visualisations/neighbourhoods.geojson
