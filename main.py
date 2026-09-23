from abc import ABC, abstractmethod

class instrument(ABC):
    def __init__(self, name, category):
        self.name=name
        self.category=category
    def display_info(self):
        print(f"Insturment name: {self.name}")
        print(f"Category: {self.category}")
    @abstractmethod
    def play_sound(self):
        pass

class Guitar(instrument):
    def __init__(self, name, category, strings):
        super().__init__(name, category)
        self.strings = strings
    def play_sound(self):
        print(f"{self.name} has {self.strings} strings sound like: Strum Strum!")

class Drum(instrument):
    def __init__(self, name, category, drum_type):
        super().__init__(name, category)
        self.drum_type = drum_type
    def play_sound(self):
        print(f"{self.name} has {self.drum_type} strings sound like: Boom Boom!")

class Flute(instrument):
    def __init__(self, name, category, material):
        super().__init__(name, category)
        self.material = material
    def play_sound(self):
        print(f"{self.name} has {self.material} strings sound like: Toot Toot!")

instrument_1 = Guitar("Acoustic Guitar", "String Instrument", 6)
instrument_2 = Drum("BAss Drum", "Percussion Insturment", "large drum")
instrument_3 = Flute("Bamboo FLute", "Wind Instrument", "bamboo")

print("===== Music Sound Show =====")
for i in [instrument_1, instrument_2, instrument_3]:
    i.display_info()
    print()
    i.play_sound()
    print()

