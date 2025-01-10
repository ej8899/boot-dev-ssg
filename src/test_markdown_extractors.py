import unittest
from node_utils import extract_markdown_images, extract_markdown_links  # Replace 'your_module' with the actual module name

class TestMarkdownExtractors(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), 
                                  ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_extract_markdown_images_no_matches(self):
        text = "This is text without images."
        result = extract_markdown_images(text)
        self.assertEqual(result, [])

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("to boot dev", "https://www.boot.dev"), 
                                  ("to youtube", "https://www.youtube.com/@bootdotdev")])

    def test_extract_markdown_links_no_matches(self):
        text = "This is text without links."
        result = extract_markdown_links(text)
        self.assertEqual(result, [])

    def test_extract_markdown_links_and_images(self):
        text = "Link [to boot dev](https://www.boot.dev) and an image ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        links_result = extract_markdown_links(text)
        images_result = extract_markdown_images(text)
        self.assertEqual(links_result, [("to boot dev", "https://www.boot.dev")])
        self.assertEqual(images_result, [("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

if __name__ == "__main__":
    unittest.main()
