class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self, object):
        pass

    def create_post(self, title, content):
        self.title = title
        self.content = content

    def json(self):
        return{
            'title': self.title,
            'content': self.content,
        }