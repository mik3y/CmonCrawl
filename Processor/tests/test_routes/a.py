from bs4 import BeautifulSoup
from App.Extractor.extractor import BaseExtractor
from processor_utils import PipeMetadata


NAME = "AAA"


class Extractor(BaseExtractor):
    def extract_soup(self, soup: BeautifulSoup, metadata: PipeMetadata):
        return None

    def filter(self, response: str, metadata: PipeMetadata) -> bool:
        return True


extractor = Extractor()
