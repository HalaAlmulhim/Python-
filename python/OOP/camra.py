class Camera:
    def __init__(self, zoom, memory, megapixels):
        self.zoom = zoom
        self.memory = []
        self.megapixels = megapixels

    def take_picture(self):
        if len(self.memory) > 29:
            print("Insufficient memory!")
        else:
            print("Took a picture!")
            # add picture object to memory[]

class Phone:
    def __init__(self, screen_size, storage, battery_life):
        self.screen_size = screen_size
        self.storage = storage
        self.battery_life = battery_life
        self.camera = Camera("3x", self.storage, 10)

    def take_picture(self):
        self.camera.take_picture()

    def download_app(self, app):
        self.storage.push(app)



iPhone = Phone("7.5 inch", ["my picture"], "400 hours")
# iPhone.camera = Camera("3x", self.storage, 10)
iPhone.camera.take_picture()
print(iPhone.camera.memory)
print(iPhone.storage)