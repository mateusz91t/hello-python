text = 'si-aa-cz_kfs'

text.title().translate("_-")

def to_camel_case(s):
    return s[0] + s.title().translate("-_")[1:] if s else s


to_camel_case(text)