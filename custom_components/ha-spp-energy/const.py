"""Constants for the ha-spp-energy sensor integration."""

SENSOR_NAME_LOW_TARIFF = 'SPP Energy Price - Low Tariff'
SENSOR_NAME_HIGH_TARIFF = 'SPP Energy Price - High Tariff'

DOMAIN = 'ha-spp-energy'

SPP_API_URL = 'https://www.spp.sk/wp-json/spp/v1/price-list/active/2'

DISTRIBUTION_AREAS = {
    'VSD': 'Východoslovenská distribučná, a.s.',
    'ZSD': 'Západoslovenská distribučná, a.s.',
    'SSD': 'Stredoslovenská distribučná, a.s.',
}

TARIFFS = {
    "DD1",
    "DD2",
    "DD3",
    "DD4",
    "DD5",
    "DD6",
    "DD7",
    "DD8",
}
