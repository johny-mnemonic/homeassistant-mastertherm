"""Constants used by Home Assistant Components."""
from homeassistant.const import Platform

NAME = "Mastertherm"
DOMAIN = "mastertherm"

API_VERSIONS = {
    "v1": "mastertherm.vip-it.cz (< 2022)",
    "v2": "mastertherm.online (> 2022)",
}

# Platforms
PLATFORMS = [Platform.SENSOR]
