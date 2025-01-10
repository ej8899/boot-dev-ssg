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


def split_nodes_image(old_nodes):
    new_nodes = []
    image_pattern = r'!\[([^\]]+)\]\(([^)]+)\)'

    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue

        text = node.text
        matches = list(re.finditer(image_pattern, text))
        if not matches:
            new_nodes.append(node)
            continue

        last_index = 0
        for match in matches:
            start, end = match.span()
            alt_text, url = match.groups()

            # Add the text before the match
            if start > last_index:
                new_nodes.append(TextNode(text[last_index:start], TextType.NORMAL))

            # Add the image node
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))

            # Update the last index
            last_index = end

        # Add any remaining text after the last match
        if last_index < len(text):
            new_nodes.append(TextNode(text[last_index:], TextType.NORMAL))
        else:
            new_nodes.append(TextNode("", TextType.NORMAL))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'

    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue

        text = node.text
        matches = list(re.finditer(link_pattern, text))
        if not matches:
            new_nodes.append(node)
            continue

        last_index = 0
        for match in matches:
            start, end = match.span()
            anchor_text, url = match.groups()

            # Add the text before the match
            if start > last_index:
                new_nodes.append(TextNode(text[last_index:start], TextType.NORMAL))

            # Add the link node
            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))

            # Update the last index
            last_index = end

        # Add any remaining text after the last match
        if last_index < len(text):
            new_nodes.append(TextNode(text[last_index:], TextType.NORMAL))
        else:
            new_nodes.append(TextNode("", TextType.NORMAL))

    return new_nodes

