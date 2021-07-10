import base64

import cloudscraper
import json


class MeetupUrlsScrape(object):
    def __init__(self):
        super(MeetupUrlsScrape, self).__init__()
        self.__run()

    def __run(self):
        s = cloudscraper.create_scraper()
        true = 'true'
        false = 'false'
        null = 'null'

        pld = json.load(open(r'C:\Users\dklec\PycharmProjects\Meetups\src\payload.txt'))

        to_get, raw = 0, 0
        # while True:
        for i in range(5):
            to_get += 20
            raw += 20
            to_get = base64.b64encode(str(to_get).encode())
            pld['variables']['after'] = to_get.decode()
            to_get = raw

            url = 'https://www.meetup.com/gql'

            r = s.post(url, json=pld)
            print(r.status_code)
            rj = r.json()
            edges = rj['data']['results']['edges']
            urls = [x['node']['result']['eventUrl'] for x in edges]

            with open(r'C:\Users\dklec\PycharmProjects\Meetups\src\meetup_urls\urls.txt', 'a') as f:
                for x in urls:
                    f.write(f'{x}\n')



if __name__ == '__main__':
    MeetupUrlsScrape()