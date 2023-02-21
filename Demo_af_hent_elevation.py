# Demo af  hent elevation

def get_elevation(lat: float, long: float) -> float:
    import requests
    import time

    # curl https://api.opentopodata.org/v1/eudem25m?locations=57.688709,11.976404 

    api_url = r'https://api.opentopodata.org/'
    endpoint = 'v1/eudem25m'

    params = {
        'locations' : f"{lat},{long}" #57.688709,11.976404,
        # 'locations' : f"{long},{lat}" #57.688709,11.976404,
    }
    # print(f"params: {params}")

    respons = requests.get(api_url+endpoint, params)

    # print(respons)
    # print("Response status:", respons.status_code)

    if respons.status_code == 200:
        print(respons.json())
        rjson = respons.json()['results'][0]
        elevation_eudem25m = rjson['elevation']
        if elevation_eudem25m is not None:
            return elevation_eudem25m
        else:
            return 'not found'
    else:
        print('-')
        print("Response status:", respons.status_code)
        print(respons.text)
    
def main():
    import time
    from fit_file import read
    fname = "data/intervalløb/C8JI1413.FIT" #C8JI1413.FIT
    points = read.read_points(fname)

    # lat, long = points[5]['latitude'], points[5]['longitude']
    # e = get_elevation(lat, long)
    # print(f'lat:{lat}, long:{long} : orig elevation:{points[1]["altitude"]} new elevation:{e}')

    newPoints = []
    for i, p in enumerate(points):
        # print(p)
        time.sleep(2)
        p['altitude'] = get_elevation(p['latitude'], p['longitude'])
        # points[i]['altitude'] = get_elevation(p['latitude'], p['longitude'])
        print(f"\r{i}: {p['altitude']} of {len(points)}       ", end='')
        newPoints.append(p)

    print(newPoints)
    
    import csv
    with open('data/punkter_m_højde.csv', 'w', newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=points[0].keys() )
        writer.writeheader()
        writer.writerows(points)

    import json
    # print(json.dumps(points, indent=2, default=str))

    import json
    with open('data/punkter_m_højde.json', 'w', newline="") as jsonfile:
        json.dump(points, jsonfile, default=str)
        

if __name__ == '__main__':
    main()