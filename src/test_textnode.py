import unittest

from htmlnode import LeafNode
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", "bold", "www.boot.dev")
        node2 = TextNode("This is a text node", "bold", "www.google.com")
        self.assertNotEqual(node, node2)

    def test_text_node_to_html_node_normal(self):
        text_node = TextNode("Normal text", TextType.NORMAL)
        html_node = text_node_to_html_node(text_node)
        assert isinstance(html_node, LeafNode)
        assert html_node.tag is None
        assert html_node.value == "Normal text"

    def test_text_node_to_html_node_bold(self):
        text_node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        assert isinstance(html_node, LeafNode)
        assert html_node.tag == "b"
        assert html_node.value == "Bold text"

    def test_text_node_to_html_node_italic(self):
        text_node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        assert isinstance(html_node, LeafNode)
        assert html_node.tag == "i"
        assert html_node.value == "Italic text"

    def test_text_node_to_html_node_code(self):
        text_node = TextNode("Code text", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        assert isinstance(html_node, LeafNode)
        assert html_node.tag == "code"
        assert html_node.value == "Code text"

    def test_text_node_to_html_node_link(self):
        text_node = TextNode("Link text", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(text_node)
        assert isinstance(html_node, LeafNode)
        assert html_node.tag == "a"
        assert html_node.value == "Link text"
        assert html_node.props == {"href": "https://example.com"}

    def test_text_node_to_html_node_image(self):
        text_node = TextNode("Alt text", TextType.IMAGE, "https://example.com/image.png")
        html_node = text_node_to_html_node(text_node)
        assert isinstance(html_node, LeafNode)
        assert html_node.tag == "img"
        assert html_node.value == ""
        assert html_node.props == {"src": "https://example.com/image.png", "alt": "Alt text"}

    def test_text_node_to_html_node_invalid(self):
        text_node = TextNode("Invalid text", "INVALID")
        try:
            text_node_to_html_node(text_node)
            assert False, "Expected ValueError for unsupported TextType"
        except ValueError as e:
            assert str(e) == "Unsupported TextType: INVALID"

if __name__ == "__main__":
    unittest.main()