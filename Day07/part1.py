class Card:
  def __init__(self, strength):
    self.strength = strength

  def get_numeric_strength(self):
    strength = self.strength

    if strength.isnumeric():
      return int(self.strength)
    
    match strength:
      case 'T':
        return 10
      case 'J':
        return 11
      case 'Q':
        return 12
      case 'K':
        return 13
      case 'A':
        return 14
  
  def __eq__(self, other):
    if isinstance(other, Card):
      return other.strength == self.strength
    return False

  def __gt__(self, other):
    if not isinstance(other, Card) or other == self:
      return False
    
    return self.get_numeric_strength() > other.get_numeric_strength()

  def __lt__(self, other):
    if not isinstance(other, Card) or other == self:
      return False
    
    return self.get_numeric_strength() < other.get_numeric_strength()

  def __hash__(self):
    return self.get_numeric_strength()

  def __repr__(self):
    return self.strength


class Hand:
  def __init__(self, cards, bet):
    self.cards = cards
    self.cards.sort()
    self.bet = bet

    pairs = 0
    counts = {}

    for card in self.cards:
      if card in counts:
        counts[card] += 1
      else:
        counts[card] = 1
      
    for card in counts:
      count = counts[card]
      if count >= 2:
        pairs += count / 2
    
    self.pairs = pairs
  
  def __eq__(self, other):
    if not isinstance(other, Hand):
      return False
    else:
      for i in range(0, len(self.cards)):
        if self.cards[i] != other.cards[i]:
          return False
      
      return True
  
  def __gt__(self, other):
    if not isinstance(other, Hand):
      return False
    if other.pairs != self.pairs:
      return self.pairs > other.pairs

  def __repr__(self):
    return f'Hand(cards={self.cards}, bet={self.bet}, pairs={self.pairs})'
    

def main():
  hands = []

  with open('./input.txt') as file:
    for line in file:
      tokens = line.strip().split()
      cards = tokens[0]
      bet = int(tokens[1])
      hand_arr = []

      for char in cards:
        card = Card(char)
        hand_arr.append(card)
      
      hand = Hand(hand_arr, bet)
      hands.append(hand)
  
  print(hands)


if __name__ == '__main__':
  main()

