from lxml import html
import cloudscraper

from src.writer import DataWriter


class MeetupDataScrape(DataWriter):
    def __init__(self):
        super(MeetupDataScrape, self).__init__()
        self.__run()

    def __run(self):
        s = cloudscraper.create_scraper()
        urls = self.__load_urls()
        for url in urls:
            resp = s.get(url)
            self.__single_url_scrape(resp)
        self.main_output()

    def __single_url_scrape(self, resp):
        data = {}
        data['Link'] = resp.url

        self.meetup_output(data)

    @staticmethod
    def __load_urls():
        with open(r'C:\Users\dklec\PycharmProjects\Meetups\src\meetup_urls\urls.txt', 'r') as f:
            urls = f.readlines()
            urls = [x.replace('\n', '') for x in urls]
            urls = list(set(urls))
        return urls


if __name__ == '__main__':
    MeetupDataScrape()