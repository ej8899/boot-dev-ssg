import unittest
from textnode import TextNode, TextType
from node_utils import split_nodes_image, split_nodes_link  # Update with actual module name

class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_image_single(self):
        node = TextNode("Text with an ![image](https://example.com/image.png)", TextType.NORMAL)
        new_nodes = split_nodes_image([node])
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "Text with an ")
        self.assertEqual(new_nodes[0].text_type, TextType.NORMAL)
        self.assertEqual(new_nodes[1].text, "image")
        self.assertEqual(new_nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(new_nodes[1].url, "https://example.com/image.png")
        self.assertEqual(new_nodes[2].text, "")
        self.assertEqual(new_nodes[2].text_type, TextType.NORMAL)

    def test_split_nodes_image_multiple(self):
        node = TextNode(
            "Text ![image1](https://example.com/1.png) and ![image2](https://example.com/2.png)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(len(new_nodes), 5)
        self.assertEqual(new_nodes[0].text, "Text ")
        self.assertEqual(new_nodes[1].text, "image1")
        self.assertEqual(new_nodes[1].url, "https://example.com/1.png")
        self.assertEqual(new_nodes[2].text, " and ")
        self.assertEqual(new_nodes[3].text, "image2")
        self.assertEqual(new_nodes[3].url, "https://example.com/2.png")
        self.assertEqual(new_nodes[4].text, "")

    def test_split_nodes_link_single(self):
        node = TextNode("This is a [link](https://example.com)", TextType.NORMAL)
        new_nodes = split_nodes_link([node])
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is a ")
        self.assertEqual(new_nodes[1].text, "link")
        self.assertEqual(new_nodes[1].url, "https://example.com")
        self.assertEqual(new_nodes[2].text, "")

    def test_split_nodes_link_multiple(self):
        node = TextNode(
            "Link [one](https://example.com/1) and [two](https://example.com/2)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(len(new_nodes), 5)
        self.assertEqual(new_nodes[0].text, "Link ")
        self.assertEqual(new_nodes[1].text, "one")
        self.assertEqual(new_nodes[1].url, "https://example.com/1")
        self.assertEqual(new_nodes[2].text, " and ")
        self.assertEqual(new_nodes[3].text, "two")
        self.assertEqual(new_nodes[3].url, "https://example.com/2")
        self.assertEqual(new_nodes[4].text, "")

    def test_no_images(self):
        node = TextNode("No images here", TextType.NORMAL)
        new_nodes = split_nodes_image([node])
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "No images here")

    def test_no_links(self):
        node = TextNode("No links here", TextType.NORMAL)
        new_nodes = split_nodes_link([node])
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "No links here")

if __name__ == "__main__":
    unittest.main()
