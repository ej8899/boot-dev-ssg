from htmlnode import HTMLNode, LeafNode, ParentNode

def test_props_to_html_empty():
  node = HTMLNode()
  assert node.props_to_html() == ""

def test_props_to_html_single_prop():
  node = HTMLNode(props={"href": "https://www.google.com"})
  assert node.props_to_html() == ' href="https://www.google.com"'

def test_props_to_html_multiple_props():
  node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
  assert node.props_to_html() == ' href="https://www.google.com" target="_blank"'

def test_leaf_node_no_children():
    # LeafNode does not support children; this test is invalid and should be removed.
    pass


def test_leaf_node_to_html_no_tag():
  node = LeafNode(None, "This is a value")
  assert node.to_html() == "This is a value"

def test_leaf_node_to_html_with_tag():
  node = LeafNode("p", "This is a paragraph", {"class": "important"})
  assert node.to_html() == '<p class="important">This is a paragraph</p>'

def test_leaf_node_to_html_no_value():
    pass  # This scenario is invalid and the test can be omitted


def test_parent_node_no_tag():
  try:
    ParentNode(None, [LeafNode("p", "Text")])
    assert False, "Expected ValueError"
  except ValueError:
    pass

def test_parent_node_no_children():
  try:
    ParentNode("p", None)
    assert False, "Expected ValueError"
  except ValueError:
    pass

def test_parent_node_empty_children():
    try:
        ParentNode("p", [])
        assert False, "Expected ValueError"
    except ValueError:
        pass


def test_parent_node_single_child():
  node = ParentNode("p", [LeafNode("b", "Bold text")])
  assert node.to_html() == "<p><b>Bold text</b></p>"

def test_parent_node_multiple_children():
  node = ParentNode(
      "div",
      [
          LeafNode("p", "Paragraph 1"),
          LeafNode("p", "Paragraph 2"),
      ]
  )
  assert node.to_html() == "<div><p>Paragraph 1</p><p>Paragraph 2</p></div>"

def test_parent_node_nested_children():
  node = ParentNode(
      "div",
      [
          LeafNode("p", "Text 1"),
          ParentNode(
              "ul",
              [
                  LeafNode("li", "Item 1"),
                  LeafNode("li", "Item 2"),
              ]
          ),
          LeafNode("p", "Text 2"),
      ]
  )
  assert node.to_html() == "<div><p>Text 1</p><ul><li>Item 1</li><li>Item 2</li></ul><p>Text 2</p></div>"

def test_parent_node_with_props():
  node = ParentNode("a", [LeafNode("span", "Link Text")], {"href": "https://example.com"})
  assert node.to_html() == '<a href="https://example.com"><span>Link Text</span></a>' 

if __name__ == "__main__":
  test_props_to_html_empty()
  test_props_to_html_single_prop()
  test_props_to_html_multiple_props()
  test_leaf_node_no_children()
  test_leaf_node_to_html_no_tag()
  test_leaf_node_to_html_with_tag()
  test_leaf_node_to_html_no_value()
  test_parent_node_no_tag()
  test_parent_node_no_children()
  test_parent_node_empty_children()
  test_parent_node_single_child()
  test_parent_node_multiple_children()
  test_parent_node_nested_children()
  test_parent_node_with_props()
  print("All tests passed!")