# World News — Wednesday, 18 November 2026

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/zhazha473/makefun-news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/zhazha473/makefun-news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

Entry for make.fun bounty **news-image-20261118** ("Sum up 18 November's
world news in one image"). Free to enter; $250 prize pool, 50 paid places.

## What it is

A one-page newspaper front page summarising the biggest world stories of
Wednesday, 18 November 2026: the widening war in the Gulf (US strikes on
Qeshm Island, Iranian drones at Kuwait and Bahrain), Ukraine's second-day
strike on the Kerch bridge to Crimea, Xi hosting Putin in Shenzhen ahead
of their summit with Trump, Democrats taking the US Senate 56–44 as
Peltola wins Alaska, the Ebola surge in DR Congo, and Category 5 Cyclone
Xavier hitting the Northern Cook Islands — plus a footer strip with the
US losing measles-free status, the Siberian military plane crash, Nvidia's
revenue doubling, and COP31 talks stalling.

`main.py` (Python 3.13, standard library only) copies the bundled image
`news.png` to `/output/entry.png`. No network access; running it twice
produces byte-identical output. The image is 1024x1024 px, under 1 MiB.

The infographic was composed at build time by `build/compose.py` (PIL)
from researched reporting; the text panels were drawn in code so every
fact is spelled exactly as reported.

## Run

```sh
python3 main.py   # writes /output/entry.png
```

## Sources (18 November 2026)

- Gulf escalation: US strike on Qeshm Island; Iranian drone attacks on
  Kuwait's Ali Al Salem Air Base and Bahrain — Reuters, Wall Street
  Journal, via https://www.justsecurity.org/165038/early-edition-november-18-2026/
- Kerch bridge struck for a second day, road span partly collapsed —
  https://oneturn.news/news/ and
  https://openchronicle.org/2026/11/18/global-news-brief-key-developments-around-the-world-november-18-2026/
- Xi–Putin meeting in Shenzhen ahead of trilateral summit with Trump —
  AFP / AP via https://openchronicle.org/2026/11/18/global-news-brief-key-developments-around-the-world-november-18-2026/
- Peltola wins Alaska; Democrats take Senate 56–44 — AP via
  https://www.reuters.com/world/us/democrat-peltola-wins-alaska-securing-56-44-us-senate-majority-2026-11-18/
- Ebola in DR Congo: 11,000+ cases, 5,400 deaths, outbreak more than
  doubled in three months — UN via https://oneturn.news/news/
- Cyclone Xavier, Category 5, hits Northern Cook Islands —
  https://oneturn.news/news/
- Also: US loses measles-free status; Russian military plane crash kills
  19 in Siberia; Nvidia revenue doubles; COP31 talks stall in Antalya —
  https://www.horizonapp.link/en/2026/11/18 and
  https://human-synthesis.ghost.io/2026/11/18/ai-chat-world-news-18-11-2026/

## License

MIT — see `LICENSE`.

<sub>Entered on [make.fun](https://make.fun/?ref=2zha-zha&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
