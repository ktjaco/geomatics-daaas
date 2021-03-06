import bs4
import datetime
import requests
import os
import logging
import sys
from datetime import date

# Set logger.
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s: %(message)s", "%Y-%m-%d %H:%M:%S"))
logger.addHandler(handler)

# Set directory where raw imagery will be downloaded.
raw_dir = 'C:\\EODM\\raw\\'

# Today's date, YYYY-MM-DD.
today = date.today()

# Yesterday's Julian date, YYJJ.
yesterday_jul = str(int(datetime.datetime.strftime(today, '%y%j')) - 1)

# Yesterday's Julian date, JJ.
jul = str(int(datetime.datetime.strftime(today, '%j')) - 1)

# Today's year, YYYY.
year = str(int(datetime.datetime.strftime(today, '%Y')))

# NRCan's EODMS Base URL.
base_url = "https://data.eodms-sgdot.nrcan-rncan.gc.ca"

# Concatenate date's to create the AVHRR repository.
url = base_url + "/public/avhrr/l1b/" + year + "/20" + yesterday_jul + "/noaa19/"

# Using the URL, request the AVHRR NRCan page.
r = requests.get(url)

# Scrap the HTML page so it can be used to extract the file names.
data = bs4.BeautifulSoup(r.text, "html.parser")

# Loop that extracts the href files names and download each of the files for yesterday's date.
for l in data.find_all("a"):
    # Change raw directory folder.
    os.chdir(raw_dir)
    # Using the URL, request the AVHRR NRCan page with the file names (HREF).
    r = requests.get(base_url + l["href"])
    # Open the file and split it at the last "/".
    file = open(l["href"].split("/")[-1], 'wb')
    # Log the file that is being downloaded.
    logger.info(f"Downloading... " + l["href"].split("/")[-1])
    # Write the file to the current folder.
    file.write(r.content)
    # Close the file.
    file.close()
# Remove the file that is generated by error.
os.remove(year + jul)
