FROM osgeo/gdal:ubuntu-small-3.1.3

ARG DEBIAN_FRONTEND=noninteractive

ARG LANDSAT_USER

ENV LANDSAT_USER=$LANDSAT_USER

ARG LANDSAT_PASSWORD

ENV LANDSAT_PASSWORD=$LANDSAT_PASSWORD

WORKDIR /cog

COPY . /cog

RUN apt update -y 

RUN apt install -y \ 
	python3-pip \
	unzip \
	wget

RUN pip3 install landsatxplore rio-cogeo

RUN landsatxplore search --username $LANDSAT_USER --password $LANDSAT_PASSWORD --dataset SENTINEL_2A --location 45.3586 -75.5951 --start 2020-01-01 --end 2020-12-31

RUN landsatxplore download --username $LANDSAT_USER --password $LANDSAT_PASSWORD --output data L1C_T18TVR_A023689_20200104T160808

RUN unzip data/L1C_T18TVR_A023689_20200104T160808.zip -d data

WORKDIR /cog/data/S2A_MSIL1C_20200104T160641_N0208_R097_T18TVR_20200104T192150.SAFE/GRANULE/L1C_T18TVR_A023689_20200104T160808/IMG_DATA

RUN chmod u+x /cog/scripts/geotiff.sh && /cog/scripts/geotiff.sh

RUN chmod u+x /cog/scripts/reproject.sh && /cog/scripts/reproject.sh

RUN chmod u+x /cog/scripts/cog.sh && /cog/scripts/cog.sh

RUN chmod u+x /cog/scripts/validate-cog.sh && /cog/scripts/validate-cog.sh

WORKDIR /cog
