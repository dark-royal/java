import requests

# url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
#
# r = requests.get(url)
# data = r.json()
# print(data['current_units']['time'])


url = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.euphoriazine.com%2Fwp-content%2Fuploads%2F2023%2F02%2FAyra-Starr-Sability-lyrics.webp&tbnid=QGAFuudto1MA5M&vet=12ahUKEwi4n-2D5dqEAxU_hCcCHfweAucQMygjegQIARB4..i&imgrefurl=https%3A%2F%2Fwww.euphoriazine.com%2Fblog%2F2023%2F02%2Fmusic%2Ftracks-ayra-starr-sability%2F&docid=M5UC59TyNdvRWM&w=1200&h=675&q=ayra%20starr%20picture&ved=2ahUKEwi4n-2D5dqEAxU_hCcCHfweAucQMygjegQIARB4"
r = requests.get(url)
with open('ayra starr.png', mode='wb') as what:
    what.write(r.content)