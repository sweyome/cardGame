# card game class
# by Sent

# card

Values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5,
          "Six": 6, "Sven": 7, "Eight": 8, "Nine": 9,
          "Ten": 10, "Jack": 11, "Queen": 12, "King": 13,
          "Ace": 14}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


two_hearts = Card("values", "Two")

# Suit/Rank,Value

vale = Values[two_hearts.rank]
print(vale)
# Deck


# A Player
