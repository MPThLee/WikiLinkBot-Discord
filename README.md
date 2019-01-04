WikiLinkBot for Discord
=======================
[WikiLinkBot](https://tools.wmflabs.org/wikilinkbot) but it's on Discord <strike>w/ lack of functions.</strike>

Install
-------
1. Install Python 3.5 and higher. Python 2 is not supported.
2. Install discord.py (Current version: [![PyPI](https://img.shields.io/pypi/v/discord.py.svg)](https://pypi.python.org/pypi/discord.py/))
```bash
python3 -m pip install -U discord.py
```

If your Python version is 3.7 and higher, and `discord.py` is `0.16.x`, Install `discord.py` rewrite branch instead of `0.16.x`
```bash
python3 -m pip install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py
```
3. Edit `setting.py`.
4. [Set a bot config](#Setting).
5. Run script.
```bash
python3 ./bot.py
```

Usage
-----
Write like `[[PAGE_NAME]]` in middle of message. Bot will be transform into wiki link.

Setting
-------
Example is on `setting.py.example`.
See Also: [Make a Discord Bot with Python](https://www.devdungeon.com/content/make-discord-bot-python)

`TOKEN` is bot token.

`BASEURL` is Wiki's baseurl.<br>
`BASEURL = "https://mediawiki.org/wiki/"` and `[[Main Page]]` will transform into `https://mediawiki.org/wiki/Main_Page`

`INTERWIKI` is list of interwikis.<br>
When it starts with one of list. `BASEURL` will replaced to its URL.<br>
With exmaple config, `[[wikipedia:Wikipedia:Bots]]` will transform into `https://en.wikipedia.org/wiki/Wikipedia:Bots`<br>
**WARNING: Interwiki's name is Lowercase ONLY. if isn't, will not WORK**

