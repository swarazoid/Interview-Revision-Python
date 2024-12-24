"""
Use case: when client wants to get something from real object, but we need to do something in between
For example:
1 - In college if we access internet, it goes through a proxy server to see if the site is blocked
2 - proxy server migth check in cache before sending request to real object
3 - when we want to preprocess before reaching the final object
"""

from abc import ABC, abstractmethod

class WebsiteHandlerInterface(ABC):
    @abstractmethod
    def get_site(self, website):
        pass

class WebsiteHandler(WebsiteHandlerInterface):
    def get_site(self, website):
        print("Fetched website: ", website)

class WebsiteHandlerProxy(WebsiteHandlerInterface):
    def __init__(self, website_handler):
        self.blocked_sites = ("youtube", "instagram", "myntra")
        self.cached_sites = set()
        self.website_handler = website_handler

    def get_site(self, website):
        if website in self.blocked_sites:
            print(website, " is blocked")
        elif website in self.cached_sites:
            print("Fetched website from cache: ", website)
        else:
            self.website_handler.get_site(website)
            self.cached_sites.add(website)
            print(f"Adding {website} to cache")

website_handler = WebsiteHandler()
browser = WebsiteHandlerProxy(website_handler)
browser.get_site("google")
browser.get_site("facebook")
browser.get_site("google")
browser.get_site("instagram")
browser.get_site("youtube")
browser.get_site("reddit")
browser.get_site("myntra")