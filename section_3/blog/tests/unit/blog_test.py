from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Test Author')
        b2 = Blog('My Day', 'Rolf')

        self.assertEqual('Test by Test Author (0 posts)', b.__repr__())
        self.assertEqual('My Day by Rolf (0 posts)', b2.__repr__())

    def test_repr_multiple_posts(self):
        b = Blog('Test', 'Test Author')
        b.posts = ['test']
        b2 = Blog('My Day', 'Rolf')
        b2.posts = ['test', 'test 2']

        self.assertEqual('Test by Test Author (1 post)', b.__repr__())
        self.assertEqual('My Day by Rolf (2 posts)', b2.__repr__())

    def test_create_post_in_blog(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Content')

        self.assertEqual(1, len(b.posts))
        self.assertEqual('Test Post', b.posts[0].title)
        self.assertEqual('Test Content', b.posts[0].content)

    def test_json(self):
        pass

