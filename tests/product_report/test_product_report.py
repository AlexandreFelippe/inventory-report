from inventory_report.product import Product


def test_product_report() -> None:
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

    assert str(product) == (
        "The product 1 - Arroz"
        " with serial number 123456"
        " manufactured on 10-01-2024"
        " by the company Marca"
        " valid until 10-01-2025"
        " must be stored according to the following instructions:"
        " Store in a cool dry place."
    )
