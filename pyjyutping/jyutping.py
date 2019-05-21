from pyjyutping import dictionaries as dicts
import re
import sys


def main():
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
        print(convert(text))
    else:
        print("Usage: pyjyutping 你想轉做粵拼嘅中文字或者句子")


def convert(text, tone=True):
    """
    Converts the specified Chinese text to Jyutping.

    Parameters
    ----------
    text : str
        The Chinese text to be converted to Jyutping.
    tone : bool, optional
        Includes the Jyutping tone number if `True`, by default `True`.

    Returns
    -------
    str
        Jyutping representation of the specified text.

    Raises
    ------
    TypeError
        If `text` is not a string.
    """
    if isinstance(text, str):
        if not text:
            return ""
        elif re.search("[\u4e00-\u9fff]+", text) is not None:
            converted = text.translate(dicts.toned if tone else dicts.toneless)
            return " ".join(converted.split())
        else:
            return text
    else:
        raise TypeError("Cannot convert a non-string 'text'")


if __name__ == "__main__":
    main()
