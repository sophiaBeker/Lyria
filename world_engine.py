import random

class GlobeGrid:
    def __init__(self, size=10, theme="Bioluminescent Deep Sea"):
        self.size = size
        self.theme = theme
        self.x, self.y = 0, 0
        # The 3 artifacts the team needs to find
        self.items = {(3, 4): "Trident", (7, 2): "Pearl", (5, 8): "Coral"}
        self.inventory = []

    def move(self, direction):
        if direction == "north": self.y = (self.y + 1) % self.size
        elif direction == "south": self.y = (self.y - 1) % self.size
        elif direction == "east": self.x = (self.x + 1) % self.size
        elif direction == "west": self.x = (self.x - 1) % self.size
        return self.get_state()

    def get_state(self):
        item_here = self.items.get((self.x, self.y))
        
        # Dynamic Prompting: This makes sure (0,0) looks different from (9,9)
        # We use the coordinates to describe the 'lighting' or 'vibe'
        lighting = "dim and blue" if self.x < 5 else "bright and glowing green"
        terrain = "sandy floor" if self.y < 5 else "rocky cavern"
        
        prompt = (
            f"A high-quality 2D top-down RPG map tile of a {self.theme}. "
            f"The area has a {terrain} and {lighting} lighting. "
            f"Direct overhead bird's-eye view. No characters visible."
        )
        
        if item_here:
            prompt += f" In the center of the frame, there is a legendary {item_here}."
            
        return {
            "pos": (self.x, self.y),
            "prompt": prompt,
            "item_found": item_here
        }