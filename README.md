# mastertherm

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

[![hacs][hacsbadge]][hacs]
![Project Maintenance][maintenance-shield]

[![Discord][discord-shield]][discord]
[![Community Forum][forum-shield]][forum]

_Component to integrate with [mastertherm][mastertherm]._

**This component will set up the following platforms.**

To Be Complete!!!

Platform | Description
-- | --
`binary_sensor` | Show something `True` or `False`.
`sensor` | Show info from mastertherm API.
`switch` | Switch something `True` or `False`.

![mastertherm][masterthermimg]

## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `mastertherm`.
4. Download _all_ the files from the `custom_components/mastertherm/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant
7. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Mastertherm"

Using your HA configuration directory (folder) as a starting point you should now also have this:

```text
custom_components/mastertherm/translations/en.json
custom_components/mastertherm/translations/nb.json
custom_components/mastertherm/translations/sensor.nb.json
custom_components/mastertherm/__init__.py
custom_components/mastertherm/api.py
custom_components/mastertherm/binary_sensor.py
custom_components/mastertherm/config_flow.py
custom_components/mastertherm/const.py
custom_components/mastertherm/manifest.json
custom_components/mastertherm/sensor.py
custom_components/mastertherm/switch.py
```

## Configuration is done in the UI

<!---->

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

***

[mastertherm]: https://github.com/shedc/homeassistant-mastertherm
[buymecoffee]: https://www.buymeacoffee.com/shedc
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge
[commits-shield]: https://img.shields.io/github/commit-activity/y/shedc/blueprint.svg?style=for-the-badge
[commits]: https://github.com/shedc/homeassistant-mastertherm/commits/main
[hacs]: https://github.com/custom-components/hacs
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[discord]: https://discord.gg/Qa5fW2R
[discord-shield]: https://img.shields.io/discord/330944238910963714.svg?style=for-the-badge
[masterthermimg]: mastertherm.png
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license-shield]: https://img.shields.io/github/license/shedc/blueprint.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-Richard%20Holmes%20%40shedc-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/shedc/blueprint.svg?style=for-the-badge
[releases]: https://github.com/shedc/homeassistant-mastertherm/releases
