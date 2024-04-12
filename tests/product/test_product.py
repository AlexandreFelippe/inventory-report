from inventory_report.product import Product


def test_create_product() -> None:
    product_data = {
        "id": "1",
        "product_name": "Arroz",
        "company_name": "Marca",
        "manufacturing_date": "10-01-2024",
        "expiration_date": "10-01-2025",
        "serial_number": "123456",
        "storage_instructions": "Store in a cool dry place"
    }

    product = Product(**product_data)

    assert product.id == product_data["id"]
    assert product.product_name == product_data["product_name"]
    assert product.company_name == product_data["company_name"]
    assert product.manufacturing_date == product_data["manufacturing_date"]
    assert product.expiration_date == product_data["expiration_date"]
    assert product.serial_number == product_data["serial_number"]
    assert product.storage_instructions == product_data["storage_instructions"]
