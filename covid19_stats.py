import requests
import json
import datetime
import time

while True:
    # Resquest data from API
    response = requests.get("https://corona-api.com/countries")
    # Create time and date stamp
    timestamp = datetime.datetime.now()
    date = datetime.date.today()

    # If response is successful
    if response.status_code == 200:
        print("Successful")
        infoDict = json.loads(response.text)

        # Create/open file for todays entry
        fileHandle = open("%s.txt" % date, "a")

        # Write timestamp of current entry
        fileHandle.write("\n%s\n" % timestamp)

        # Parsing the data
        for entry in infoDict['data']:
            # 0: Country name   1: Country code   2: Country population
            countryInfo = "%-45s %-5s %-12s " % (entry['name'], entry['code'], entry['population'])
            # 0: Todays deaths   1: Todays confirmed cases
            et = entry['today']
            todayInfo = "%-10s %-10s" % (et['deaths'], et['confirmed'])
            # 0: Total deaths   1: Total confirmed cases   2: Total recoveries   3: Total in critical condition
            el = entry['latest_data']
            fullStats = "%-10s %-10s %-10s %-10s" % (el['deaths'], el['confirmed'], el['recovered'], el['critical'])
            # 0: Death rate of infected   2: Recovery rate   3: Recovered vs dead ratio   4: Cases per million
            elc = el['calculated']
            calculations = "%-8.5s %-8.5s %-8.5s %-10s" % (elc['death_rate'], elc['recovery_rate'], elc['recovered_vs_death_ratio'],
                                            elc['cases_per_million_population'])

            # Convert encodings to ASCII
            stringEntry = (countryInfo + ' ' + todayInfo + ' ' + fullStats + ' ' + calculations)
            stringEntry = stringEntry.encode('utf-8').decode('utf-8')

            # Write data to file
            fileHandle.write("%s\n" % stringEntry)

        # Close the file
        fileHandle.close()

    # Request failed
    else:
        print("Unsuccessful")

        # Write time to an error log file - For simplicity we wait another hour for an entry
        fileHandle = open("covid19_data_error_log.txt", "a")
        fileHandle.write("%s - Request failed with response: %s" % (timestamp, response.status_code))

    # Wait for an hour until processing new request
    time.sleep(3600)
