class Smartphone:

    def __init__(self, brand, model, color, camera, storage, os):
        self.brand = brand
        self.color = color
        self.camera = camera
        self.storage = storage
        self.model = model
        self._os = os

    def print_info(self):
        print(f"This is a(n) {self.brand} {self.model} {self.color} which has {self.storage} of storage and a {self.camera} of camera and it runs on {self._os}")


iphone14 = Smartphone("Apple", "14 pro", "Gold",
                      "45 megapixel", "264 gb", "IOS")

print(iphone14.color)
print(iphone14.model)

iphone14.print_info()
