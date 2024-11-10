from math import ceil


class PhotoAlbum:
    PAGE_SIZE = 4

    def __init__(self, pages: int) -> None:

        self.pages = pages
        self.photos: list[list] = [[] for i in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        album_pages = ceil(photos_count/cls.PAGE_SIZE)
        return cls(album_pages)

    def add_photo(self, label: str) -> str:
        for num, page in enumerate(self.photos):
            if len(page) < PhotoAlbum.PAGE_SIZE:
                page.append(label)
                return f"{label} photo added successfully on page {(num + 1)} slot {len(page)}"
        return "No more free slots"

    def display(self):
        result = f'{"-" * 11}\n'
        for page in range(self.pages):
            result += ' '.join(['[]' for el in self.photos[page] if el]) + "\n"
            result += f'{"-" * 11}\n'

        return result.strip()
#from judge 
import unittest


class TestsPhotoAlbum(unittest.TestCase):
    def test_init_creates_all_attributes(self):
        album = PhotoAlbum(2)
        self.assertEqual(album.pages, 2)
        self.assertEqual(album.photos, [[], []])

    def test_from_photos_should_create_instace(self):
        album = PhotoAlbum.from_photos_count(12)
        self.assertEqual(album.pages, 3)
        self.assertEqual(album.photos, [[], [], []])

    def test_add_photo_with_no_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.add_photo("prom")
        self.assertEqual(result, "No more free slots")

    def test_add_photo_with_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        self.assertEqual(album.photos, [['baby', 'first grade', 'eight grade', 'party with friends']])

    def test_display_with_one_page(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.display().strip()
        self.assertEqual(result, "-----------\n[] [] [] []\n-----------")

    def test_display_with_three_pages(self):
        album = PhotoAlbum(3)
        for _ in range(8):
            album.add_photo("asdf")
        result = album.display().strip()
        self.assertEqual(result, "-----------\n[] [] [] []\n-----------\n[] [] [] []\n-----------\n\n-----------")


if __name__ == "__main__":
    unittest.main()

