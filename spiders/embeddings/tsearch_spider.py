from collections import deque
import scrapy
from urllib.parse import urlparse, urljoin

def extract_hostname(url):
    parsed_url = urlparse(url)
    return parsed_url.hostname

# Set to track visited URLs
url_seen = set()
# Queue to store URLs to be crawled
urls_frontier = deque()

class TechSpider(scrapy.Spider):
    name = "tsearch"

    def __init__(self):
        self.number_parsed = 1

    def start_requests(self):
        # Seed URLs (Initial crawl points)
        urls = [
            "https://www.cc.gatech.edu/",
            "https://library.gatech.edu/",
            "https://pe.gatech.edu/degrees/computer-science",
            "https://www.reddit.com/r/OMSCS/",
            "https://www.reddit.com/r/gatech/",
            "https://www.omscentral.com/",
            "https://spp.gatech.edu/spp_newsletters",
            "https://scs.gatech.edu/news",
            "https://db.cc.gatech.edu/",
            "https://coe.gatech.edu/"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        text_content = ""
        p_tag_content = response.xpath('//p')
        
        # Extract text from <p> tags
        for p_tag in p_tag_content:
            p_text = p_tag.xpath('string()').get().strip()
            text_content += p_text
            yield {
                "paragraph": p_text
            }

        # Custom filtering logic: Here, we check if the page has meaningful content
        if len(text_content) > 200:  # Example threshold: 200 characters
            self.number_parsed += 1
            links = response.xpath('//a/@href').extract()

            for href in links:
                # Normalize relative URLs
                if not href.startswith("http"):
                    href = urljoin(response.url, href)

                # Add to queue if not already seen
                if href not in url_seen:
                    url_seen.add(href)
                    urls_frontier.append(href)

            # Get a valid URL from the queue
            while urls_frontier and urls_frontier[0] is None:
                urls_frontier.popleft()

            try:
                next_url = urls_frontier.popleft()
                if next_url:
                    print("***** Exploring URL *****", next_url, "Total Visited:", len(url_seen))
                    yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)
            except:
                pass