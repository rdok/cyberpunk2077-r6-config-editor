from xml.etree.ElementTree import TreeBuilder, Comment


class CustomTreeBuilder(TreeBuilder):
    def __init__(self, *args, **kwargs):
        super(CustomTreeBuilder, self).__init__(*args, **kwargs)

    # Instruct XML editor to not remove comments.
    def comment(self, data):
        self.start(Comment, {})
        self.data(data)
        self.end(Comment)
