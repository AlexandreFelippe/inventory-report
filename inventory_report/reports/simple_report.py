from typing import List
from inventory_report.reports.report import Report
from inventory_report.inventory import Inventory
from datetime import datetime


class SimpleReport(Report):
    def __init__(self):
        self.inventories: List[Inventory] = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.inventories.append(inventory)

    def generate(self) -> str:
        oldest_manufacturing_date = self._get_oldest_manufacturing_date()
        closest_expiration_date = self._get_closest_expiration_date()
        largest_inventory_company = self._get_largest_inventory_company()

        report = (
            f"Oldest manufacturing date: {oldest_manufacturing_date}\n"
            f"Closest expiration date: {closest_expiration_date}\n"
            f"Company with the largest inventory: {largest_inventory_company}"
        )

        return report

    def _get_oldest_manufacturing_date(self) -> str:
        oldest_date = None
        for inventory in self.inventories:
            for product in inventory.data:
                manufacturing_date = datetime.strptime(
                    product.manufacturing_date, "%Y-%m-%d"
                )
                if oldest_date is None or manufacturing_date < oldest_date:
                    oldest_date = manufacturing_date
        if oldest_date:
            return oldest_date.strftime("%Y-%m-%d")
        else:
            return ""

    def _get_closest_expiration_date(self) -> str:
        closest_date = None
        today = datetime.now().date()
        for inventory in self.inventories:
            for product in inventory.data:
                expiration_date = datetime.strptime(
                    product.expiration_date, "%Y-%m-%d"
                ).date()
                if expiration_date > today and (
                    closest_date is None or expiration_date < closest_date
                ):
                    closest_date = expiration_date
        if closest_date:
            return closest_date.strftime("%Y-%m-%d")
        else:
            return ""

    def _get_largest_inventory_company(self) -> str:
        company_inventory = {}
        for inventory in self.inventories:
            for product in inventory.data:
                if product.company_name in company_inventory:
                    company_inventory[product.company_name] += 1
                else:
                    company_inventory[product.company_name] = 1
        if company_inventory:
            return max(
                company_inventory, key=lambda x: int(company_inventory[x])
                )
        else:
            return ""
