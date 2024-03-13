# Write your solution here!
class EdPost:
    _title: str
    _tag: str
    _comments: list[str] = []

    def __init__(
        self, title: str, tag: str = "General", comments: list = None
    ) -> None:
        self._title = title
        self._tag = tag
        self._comments = [] if comments is None else comments

    def get_title(self) -> str:
        return self._title

    def get_tag(self) -> str:
        return self._tag

    def add_comment(self, comment: str) -> None:
        self._comments.append(comment)

    def display(self) -> None:
        print(f"{self._title} ({self._tag})")
        print("Comments:")
        for comment in self._comments:
            print(f"  {comment}")
