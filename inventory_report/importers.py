import csv
from typing import Dict, Type, List
from abc import ABC, abstractmethod
from inventory_report.product import Product
import json


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> List[Product]:
        raise NotImplementedError


class JsonImporter(Importer):
    def import_data(self) -> List[Product]:
        products = []
        with open(self.path, 'r') as file:
            data = json.load(file)
            for item in data:
                product = Product(**item)
                products.append(product)
        return products


class CsvImporter(Importer):
    def import_data(self) -> List[Product]:
        products = []
        with open(self.path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                product = Product(**row)
                products.append(product)
        return products


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
