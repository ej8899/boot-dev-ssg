import unittest
from textnode import TextNode, TextType
from node_utils import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_single_split(self):
        node = TextNode("This is `code`", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is ")
        self.assertEqual(new_nodes[0].text_type, TextType.NORMAL)
        self.assertEqual(new_nodes[1].text, "code")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[2].text, "")
        self.assertEqual(new_nodes[2].text_type, TextType.NORMAL)

    def test_multiple_splits(self):
        node = TextNode("This `is` code with `multiple` blocks", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 5)
        self.assertEqual(new_nodes[0].text, "This ")
        self.assertEqual(new_nodes[1].text, "is")
        self.assertEqual(new_nodes[2].text, " code with ")
        self.assertEqual(new_nodes[3].text, "multiple")
        self.assertEqual(new_nodes[4].text, " blocks")

    def test_no_delimiter(self):
        node = TextNode("This has no delimiters", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "This has no delimiters")
        self.assertEqual(new_nodes[0].text_type, TextType.NORMAL)

    def test_mixed_text_types(self):
        nodes = [
            TextNode("This is `code`", TextType.NORMAL),
            TextNode("Bold text", TextType.BOLD),
        ]
        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0].text, "This is ")
        self.assertEqual(new_nodes[1].text, "code")
        self.assertEqual(new_nodes[2].text, "")
        self.assertEqual(new_nodes[3].text, "Bold text")
        self.assertEqual(new_nodes[3].text_type, TextType.BOLD)

    def test_italic_splitting(self):
        node = TextNode("This is *italic* text", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is ")
        self.assertEqual(new_nodes[1].text, "italic")
        self.assertEqual(new_nodes[2].text, " text")
        self.assertEqual(new_nodes[1].text_type, TextType.ITALIC)

    def test_nested_calls(self):
        node = TextNode("This *is* text with `code`", TextType.NORMAL)
        nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(len(nodes), 5)
        self.assertEqual(nodes[0].text, "This ")
        self.assertEqual(nodes[1].text, "is")
        self.assertEqual(nodes[2].text, " text with ")
        self.assertEqual(nodes[3].text, "code")
        self.assertEqual(nodes[4].text, "")

if __name__ == "__main__":
    unittest.main()
