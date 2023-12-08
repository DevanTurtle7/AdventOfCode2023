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
        return 1
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
    self.bet = bet

    score = 0
    counts = {}
    config = []
    num_j = 0

    for card in self.cards:
      if card.strength == 'J':
        num_j += 1
        continue

      if card in counts:
        counts[card] += 1
      else:
        counts[card] = 1
      
    for card in counts:
      count = counts[card]
      config.append(count)
    
    config.sort(reverse=True)
    
    if len(config) == 0:
      config.append(0)

    config[0] += num_j

    if config[0] == 5:
      score = 6
    elif config[0] == 4:
      score = 5
    elif config[0] == 3 and config[1] == 2:
        score = 4
    elif config[0] == 3 and config[1] == 1:
        score = 3
    elif config[0] == 2 and config[1] == 2:
      score = 2
    elif config[0] == 2 and config[1] == 1:
      score = 1
    else:
      score = 0
    
    self.score = score
  
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
    if other.score != self.score:
      return self.score > other.score
    else:
      for i in range(0, len(self.cards)):
        if self.cards[i] == other.cards[i]:
          continue
        else:
          return self.cards[i] > other.cards[i]

  def __repr__(self):
    return f'Hand(cards={self.cards}, bet={self.bet}, score={self.score})'
    

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
  
  hands.sort()
  winnings = 0
  
  for i in range(0, len(hands)):
    winnings += (i + 1) * hands[i].bet

  print(winnings)


if __name__ == '__main__':
  main()

