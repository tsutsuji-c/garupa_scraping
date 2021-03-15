from event_url.scrape_event_url import scrape_event_url
from event.make_json import make_event_json


def main():
    scrape_event_url()
    make_event_json()


if __name__ == '__main__':
    main()