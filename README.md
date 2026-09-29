<div align="center">

# 🌦️ EasyPeasy Weather

### Type a place. Get the weather, on screen and out loud.

A tiny Python command-line app that fetches live weather from [WeatherAPI](https://www.weatherapi.com/) and reads the report aloud with offline text-to-speech.

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![WeatherAPI](https://img.shields.io/badge/Data-WeatherAPI-1E90FF?style=for-the-badge)](https://www.weatherapi.com/)
[![pyttsx3](https://img.shields.io/badge/Speech-pyttsx3-orange?style=for-the-badge)](https://pypi.org/project/pyttsx3/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

[![Last commit](https://img.shields.io/github/last-commit/HarshCoder1122/EasyPeasy-Weather-app?style=flat-square)](https://github.com/HarshCoder1122/EasyPeasy-Weather-app/commits/main)
[![Issues](https://img.shields.io/github/issues/HarshCoder1122/EasyPeasy-Weather-app?style=flat-square)](https://github.com/HarshCoder1122/EasyPeasy-Weather-app/issues)

</div>

## Table of contents

- [What it does](#what-it-does)
- [Example](#example)
- [Getting started](#getting-started)
- [How it works](#how-it-works)
- [Project structure](#project-structure)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

## What it does

You enter a city, state, or country. The app calls the WeatherAPI *current conditions* endpoint and shows:

| Field | Example |
|---|---|
| Location | City, region, country |
| Temperature | Celsius and Fahrenheit |
| Condition | "Partly cloudy" |
| Wind | Speed in km/h |
| Humidity | Percentage |

It then speaks the same report through your speakers using `pyttsx3`, which works offline using your operating system's built-in voices.

## Example

```text
Enter the city Name: Jaipur
City: Jaipur
State: Rajasthan
Country: India
The Temperature in Celsius: 31.0
The Temperature in Fahrenheit: 87.8
Weather: Sunny
Wind Speed in Km/h: 11.2
Humidity: 42
```

## Getting started

### Prerequisites

- Python 3.8 or newer
- A free API key from [weatherapi.com](https://www.weatherapi.com/signup.aspx)
- On Linux, `espeak` for speech (`sudo apt install espeak`)

### Install and run

```bash
git clone https://github.com/HarshCoder1122/EasyPeasy-Weather-app.git
cd EasyPeasy-Weather-app

python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install requests pyttsx3

python main.py
```

> **Use your own API key.** Open [main.py](main.py) and replace the key in the `link` URL with yours. Never commit a real key to a public repository; prefer reading it from an environment variable.

## How it works

1. `input()` reads the place name.
2. `requests.get()` calls `https://api.weatherapi.com/v1/current.json?key=<KEY>&q=<place>`.
3. The JSON response is parsed and the relevant fields are printed.
4. `pyttsx3` queues one sentence per field and speaks them with `runAndWait()`.

## Project structure

```text
EasyPeasy-Weather-app/
├── main.py              # The whole app: fetch, print, speak
├── README.md
├── LICENSE
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
└── SECURITY.md
```

## Roadmap

- [ ] Read the API key from an environment variable
- [ ] Handle unknown cities and network errors gracefully
- [ ] Add a 3-day forecast
- [ ] Add a `--no-speech` flag

## Contributing

Ideas and pull requests are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## License

Released under the [MIT License](LICENSE).

<div align="center"><sub>Built by <a href="https://github.com/HarshCoder1122">Harsh</a> while learning Python.</sub></div>
