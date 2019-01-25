# Message Bot

Highly customizable bot capable of accepting and answering messages.

## Requirements

- Python 3.7.2

## Installation

- Clone this repository.
- Setup Python interpretor.
- Install `pip` packages from [requirements.txt](requirements.txt).
- Get credentials for engines you use:
	- If your database is powered by `GspreadEngine`, [get OAuth Credentials](https://gspread.readthedocs.io/en/latest/oauth2.html) and save them as `credentials/gspread.json`;
	- If your bot's running `VKEngine`, create a JSON file with the scheme of `{"username": "YOUR_USERNAME", "password": "YOUR_PASSWORD"}` which contains the username and the password from your VK account and save it as `credentials/vk_api.json`.
- *Done.*

## Usage

> **Note:** this project was initially intended as a complete program, which means this is *not* a framework or library. Feel free to fork and personalize the sources as you wish.

- Run `main.py` file.

## License

Distributed under the MIT License. See the [LICENSE.md](LICENSE.md) for details.

## Acknowledgments

- [`vk_api`](https://github.com/python273/vk_api)
- [`gspread`](https://github.com/burnash/gspread)
