class Image:
    def show(self):
        pass


class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self._load_image()

    def _load_image(self):
        print(f"Loading image from {self.filename}")

    def show(self):
        print(f"Displaying {self.filename}")


class ImageProxy(Image):
    def __init__(self, filename):
        self.filename = filename
        self._real_image = None

    def show(self):
        if self._real_image is None:
            self._real_image = RealImage(self.filename)
        self._real_image.show()


def main_proxy():
    proxy_image = ImageProxy("/home/username/photo.jpeg")
    proxy_image.show()
    proxy_image.show()

if __name__ == "__main__":
    main_proxy()