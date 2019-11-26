import unittest


def get_formatted_name(first, middle, last):
    full_name = first + " " + middle + " " + last
    return full_name.title()


class NameTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name('jania', 'joplin')
        self.assertEqual(formatted_name, "Jania Joplin")


if __name__ == '__main__':
    unittest.main()
