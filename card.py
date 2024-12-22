
class Card:
    def __init__(self,number,color,is_special):
        self.number=number
        self.color=color
        self.is_special=is_special

    def draw_two(self):
        pass
    


# special cards
"""
Special cards: 
1. draw 2
2. revers
3. wild (color change)
4. skip : forces the player who would be next to miss their turn.
5. wild (color) draw 4, 
"""
