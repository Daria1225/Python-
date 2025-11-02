from address import Address
from mailing import Mailing

to_addr = Address(
    index="394016",
    city="Воронеж",
    street="Московский проспект",
    house="46",
    apartment="5"
)

from_addr = Address(
    index="117312",
    city="Москва",
    street="Вавилова",
    house="19",
    apartment="1"
)

my_mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=500,
    track="TRK123569789RU"
)

print(f"Отправление {my_mailing.track} из {my_mailing.from_address.index}, {my_mailing.from_address.city}, "
      f"{my_mailing.from_address.street}, {my_mailing.from_address.house} - {my_mailing.from_address.apartment} "
      f"в {my_mailing.to_address.index}, {my_mailing.to_address.city}, {my_mailing.to_address.street}, "
      f"{my_mailing.to_address.house} - {my_mailing.to_address.apartment}. Стоимость {my_mailing.cost} рублей.")