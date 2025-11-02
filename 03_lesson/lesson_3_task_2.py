from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 13 Pro Max", "+79181234567"))
catalog.append(Smartphone("Samsung", "Galaxy S22 Ultra", "+79187654321"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 10", "+79189876543"))
catalog.append(Smartphone("Huawei", "P40 Lite", "+79182345678"))
catalog.append(Smartphone("Google", "Pixel 6a", "+79183456789"))

for item in catalog:
    print(f"{item.phone_brand} - {item.phone_model}. {item.phone_number}")