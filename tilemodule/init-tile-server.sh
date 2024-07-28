#!/bin/bash
docker volume create osm-data
docker run -v $1:/data/region.osm.pbf -v osm-data:/data/database/ overv/openstreetmap-tile-server import