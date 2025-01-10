import unittest
from textnode import TextNode, TextType
from node_utils import text_to_textnodes  # Replace with the actual module name

class TestTextToTextNodes(unittest.TestCase):
    def test_simple_text(self):
        text = "This is plain text."
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "This is plain text.")
        self.assertEqual(nodes[0].text_type, TextType.NORMAL)

    def test_text_with_bold(self):
        text = "This is **bold** text."
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[0].text_type, TextType.NORMAL)
        self.assertEqual(nodes[1].text, "bold")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[2].text, " text.")
        self.assertEqual(nodes[2].text_type, TextType.NORMAL)

    def test_text_with_italic_and_code(self):
        text = "This is *italic* and `code`."
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 5)
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[0].text_type, TextType.NORMAL)
        self.assertEqual(nodes[1].text, "italic")
        self.assertEqual(nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(nodes[2].text, " and ")
        self.assertEqual(nodes[2].text_type, TextType.NORMAL)
        self.assertEqual(nodes[3].text, "code")
        self.assertEqual(nodes[3].text_type, TextType.CODE)
        self.assertEqual(nodes[4].text, ".")
        self.assertEqual(nodes[4].text_type, TextType.NORMAL)

    def test_text_with_images_and_links(self):
        text = "This is a ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)."
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 5)
        self.assertEqual(nodes[0].text, "This is a ")
        self.assertEqual(nodes[0].text_type, TextType.NORMAL)
        self.assertEqual(nodes[1].text, "obi wan")
        self.assertEqual(nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(nodes[1].url, "https://i.imgur.com/fJRm4Vk.jpeg")
        self.assertEqual(nodes[2].text, " and a ")
        self.assertEqual(nodes[2].text_type, TextType.NORMAL)
        self.assertEqual(nodes[3].text, "link")
        self.assertEqual(nodes[3].text_type, TextType.LINK)
        self.assertEqual(nodes[3].url, "https://boot.dev")
        self.assertEqual(nodes[4].text, ".")
        self.assertEqual(nodes[4].text_type, TextType.NORMAL)

    def test_complex_text(self):
        text = "This is **bold** with *italic* and `code` and a ![image](https://example.com/img.png) and a [link](https://example.com)."
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 11)
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[1].text, "bold")
        self.assertEqual(nodes[2].text, " with ")
        self.assertEqual(nodes[3].text, "italic")
        self.assertEqual(nodes[4].text, " and ")
        self.assertEqual(nodes[5].text, "code")
        self.assertEqual(nodes[6].text, " and a ")
        self.assertEqual(nodes[7].text, "image")
        self.assertEqual(nodes[8].text, " and a ")
        self.assertEqual(nodes[9].text, "link")
        self.assertEqual(nodes[10].text, ".")

if __name__ == "__main__":
    unittest.main()
