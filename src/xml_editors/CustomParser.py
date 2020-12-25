from xml.etree.ElementTree import TreeBuilder, Comment


class CustomParser(TreeBuilder):
    def __init__(self, *args, **kwargs):
        super(CustomParser, self).__init__(*args, **kwargs)

    def comment(self, data):
        self.start(Comment, {})
        self.data(data)
        self.end(Comment)
