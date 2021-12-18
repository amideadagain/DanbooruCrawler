from scrapy import Spider, Request
from ..items import DanbooruItem


class DanbooruSpider(Spider):
    name = 'pics'
    base_url = 'https://danbooru.donmai.us'
    start_urls = [
        'https://danbooru.donmai.us/posts?tags=mona_%28genshin_impact%29+'
    ]

    def parse(self, response):
        for img_page in response.css("div.posts-container article a::attr(href)"):
            page_link = self.base_url + img_page.get()
            yield Request(page_link, callback=self.parse_pages)

        next_page_url = response.css("a.paginator-next::attr(href)").extract_first()
        if next_page_url is not None:
            yield Request(response.urljoin(next_page_url))

    def parse_pages(self, response):
        original_img_link = response.css("div.notice a.image-view-original-link::attr(href)").get()
        if original_img_link is not None:
            img_link = original_img_link
        else:
            img_link = response.css("section.image-container picture img::attr(src)").get()
            if img_link is None:
                img_link = response.css("section.image-container video::attr(src)").get()

        danbooru_item = DanbooruItem()
        danbooru_item['image_urls'] = [img_link]

        yield danbooru_item

# response.css("div.posts-container article a::attr(href)").get()
# response.css("a.paginator-next::attr(href)").extract_first()
# response.css("picture img::attr(src)").get()
# response.css("div.notice a.image-view-original-link::attr(href)").get()
