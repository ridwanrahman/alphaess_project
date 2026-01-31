from textual.app import App, ComposeResult
from textual.widgets import Static

TEXT = """I must not fear.
Fear is the mind-killer.
Fear is the little-death that brings total obliteration.
I will face my fear.
I will permit it to pass over me and through me.
And when it has gone past, I will turn the inner eye to see its path.
Where the fear has gone there will be nothing. Only I will remain."""

class DimensionApp(App):
    def compose(self) -> ComposeResult:
        self.widget = Static(TEXT)
        yield self.widget
        self.widget2 = Static(TEXT)
        yield self.widget2

    def on_mount(self) -> None:
        self.widget.styles.background = "purple"
        self.widget.styles.background = "green"
        self.widget.styles.height = "2fr"
        self.widget2.styles.height = "1fr"

if __name__ == "__main__":
    app = DimensionApp()
    app.run()
