import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue

        text = node.text
        parts = text.split(delimiter)

        for i, part in enumerate(parts):
            # Alternate between the original type and the new type
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.NORMAL))
            else:
                new_nodes.append(TextNode(part, text_type))

    return new_nodes


def extract_markdown_images(text):
    pattern = r'!\[([^\]]+)\]\(([^)]+)\)'
    return re.findall(pattern, text)

def extract_markdown_links(text):
    # Exclude image links by ensuring the link doesn't start with '!'
    pattern = r'(?<!!)\[(.*?)\]\((.*?)\)'
    return re.findall(pattern, text)
