class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children or []
    self.props = props or {}

  def to_html(self):
    raise NotImplementedError("Subclasses must implement to_html")

  def props_to_html(self):
    if not self.props:
      return ""
    props_html = []
    for key, value in self.props.items():
      props_html.append(f' {key}="{value}"')
    return "".join(props_html)

  def __repr__(self):
    return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
  def __init__(self, tag, value, props=None):
    # Remove 'children' argument from the constructor call
    super().__init__(tag, value, props=props) 

  def to_html(self):
    if self.value is None:
      raise ValueError("LeafNode must have a value")
    if self.tag is None:
      return self.value
    return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
  
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("ParentNode must have a tag")
        if not children:  # This handles both `None` and empty lists
            raise ValueError("ParentNode must have at least one child")
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.children:
            raise ValueError("ParentNode must have at least one child")

        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"