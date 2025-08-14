from qwq_tag import QwqTag

# Malformed XML/HTML
malformed = '<div><p>Unclosed paragraph<span>Text</div>'
try:
    result = QwqTag.from_str(malformed)
    print("Successfully parsed malformed XML!")
    print(str(result[0]))
except Exception as e:
    print(f"Parsing failed: {e}")