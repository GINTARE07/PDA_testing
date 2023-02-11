### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: # should be ==, not single =;
      return True
    else
      return False
# second return after else should be None, not false and in the same level of indentation as "if"(no "else" needed )
   

  dif highest_card(self, card1 card2): #missing semicolon between card1 and card2. # Also "def" not "dif"; 
  if card1.value > card2.value:# if needds to be one level indented, and return after it indented one level more than if
    return card # should be "return card1"
  else:
    return card2

def cards_total(self, cards):
  total #total need to start with  "total = 0"
  for card in cards:
    total += card.value
    return "You have a total of" + total
    
#  return indentation is wrong, need to be in the same level as "for"
 
```
