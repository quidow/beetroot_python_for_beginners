# def reverse(input_str: str) -> str:
#     """
#     Function returns reversed input string
#     >>> reverse("hello") == "olleh"
#     True
#     >>> reverse("o") == "o"
#     True
#     """

from reverse import reverse

if __name__ == "__main__":
    assert reverse("hello") == "olleh"
    assert reverse("o") == "o"
