class TestScope:
    def test_class_scope(self, page):
        assert "SUPER" in page
