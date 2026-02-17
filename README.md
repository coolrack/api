# Web APIs with Python Assignment

student: devin l.
due date: feb 28, 2026
course: computer programming 12

## what's this

two programs that use web apis with python

part a - weather info using wttr.in
part b - crypto info using coingecko

## setup

just install requests:
```
pip install requests
```

## part a - weather program

api docs: https://github.com/chubin/wttr.in

what it does:
- takes a city/location from user
- shows temp in celsius and fahrenheit
- shows weather conditions with emoji
- also shows humidity, wind speed, visibility

run it:
```
python part_a_weather.py
```

## part b - crypto program

api docs: https://www.coingecko.com/en/api/documentation

what it does:
- menu with 3 options
- gets crypto prices with 24h change and market cap
- shows trending cryptos
- search for any crypto

run it:
```
python part_b_crypto.py
```

## marking

part a (8/7 with bonus)
- makes api request to wttr.in
- gets user input for location
- shows temp in C and F
- shows weather conditions
- bonus: weather emoji

part b (14/13 with bonus)
- has api docs in comments
- uses coingecko (unique api)
- menu system is clear
- 3 different api calls
- returns and formats results nicely
- bonus: uses query parameters

general (10/10)
- code is commented
- good variable names
- decent user experience

total: 32/30

## notes

both programs have error handling, input validation, and comments explaining stuff

## git

init push

## license

MIT

completed by devin l.
