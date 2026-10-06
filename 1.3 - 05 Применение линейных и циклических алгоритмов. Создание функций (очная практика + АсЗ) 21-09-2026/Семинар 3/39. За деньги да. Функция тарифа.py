def voice_price(words, rate=10):
    return words * rate


print(voice_price(3))
print(voice_price(4, rate=7))
print(voice_price(0))
print(voice_price(1000, 100))
print(voice_price(1, 1))
print(voice_price(words=7, rate=2))