from enum import Enum
from htmlnode import LeafNode
#from textnode import TextType, TextNode  # Ensure these imports exist if used here

class TextType(Enum):
  NORMAL = "NORMAL"
  BOLD = "BOLD"
  ITALIC = "ITALIC"
  CODE = "CODE"
  LINK = "LINK"
  IMAGE = "IMAGE"

class TextNode:
  def __init__(self, text, text_type, url=None):
    self.text = text
    self.text_type = text_type
    self.url = url

  def __eq__(self, other):
    if not isinstance(other, TextNode):
      return False
    return self.text == other.text and self.text_type == other.text_type and self.url == other.url

  def __repr__(self):
    return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
  

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.NORMAL:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        if not text_node.url:
            raise ValueError("LINK TextType requires a URL")
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        if not text_node.url or not text_node.text:
            raise ValueError("IMAGE TextType requires both a URL and alt text")
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unsupported TextType: {text_node.text_type}")