import requests as req
import time
import json
import math


class CasnScrapper():
    resources = []
    idPendidikan = None
    delayInSeconds = 1
    perPage = 10
    url = "https://api-sscasn.bkn.go.id/2024/portal/spf?kode_ref_pend=[pendidikan]&offset=[offset]"
    headers = {'Origin': 'https://sscasn.bkn.go.id'}
    totalData = None

    def __init__(self, idPendidikan):
        # Example: Pendidikan Teknik Komputer dan Informatika (5101087)
        self.idPendidikan = idPendidikan

    def getData(self, pendidikan, offset=0):
        # Make the API request with the provided offset and pendidikan ID
        url = self.url\
            .replace("[pendidikan]", str(self.idPendidikan))\
            .replace("[offset]", str(offset))
        response = req.get(url, headers=self.headers)

        # Parse the response to json
        data = response.json()

        print('----------------------------------------------------------------')
        print(f'Offset start from {offset}')
        time.sleep(self.delayInSeconds)

        if data is not None and data['data'] is not None and data['data']['data'] is not None:
            self.resources.extend(data['data']['data'])

        if self.totalData is None:
            self.totalData = data['data']['meta']['total']
            self.perPage = data['data']['page']['total']

    def saveToJson(self):
       with open('data.json', 'w') as file:
           file.write(json.dumps(self.resources))
           print("Data saved successfully")

    def run(self):
        if self.totalData is None:
            self.getData(self.idPendidikan)
        totalPage = math.ceil(self.totalData / self.perPage)
        for i in range(1, totalPage):
            self.getData(self.idPendidikan, i * self.perPage)

        print(f"Total Data: {self.totalData} data")
        self.saveToJson()
