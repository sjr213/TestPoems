from random_poems2.poems import declaim

class TestDeclaim:
    def test_declaim(self, capsys):
        title = "Super Cool"
        poem= (
            "Roses are red\nViolets are blue\nI think Global South\nIs super cool"
        )
        author = "Tomino"
        expected_output = (
            "-------------------------------------------------------------\n"
            "Super Cool\n"
            "\n"
            "Roses are red\n"
            "Violets are blue\n"
            "I think Global South\n"
            "Is super cool\n"""
            "\n"
            "By Tomino\n"
            "-------------------------------------------------------------\n"
        )

        declaim(title, poem, author)
        captured = capsys.readouterr()
        assert captured.out == expected_output
