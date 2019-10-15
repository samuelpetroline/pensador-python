def clear_tags(content, tag):
    [tag.extract() for tag in content.find_all(tag)]

    return content

def get_string_nested(content, tag):
    if (content.find(tag)) is None:
        return content.getText()

    return content.find(tag).getText()
