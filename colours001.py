from textual.app import App, ComposeResult
from textual.widgets import Static, Header, Footer
from textual.color import Color


class ColorApp(App):
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("d", "toggle_dark", "Toggle dark mode"),
        ("d", "randon_action", "BITE ME"),
    ]
    def compose(self) -> ComposeResult:
        self.widgets = [Static('') for i in range(10)]
        yield from self.widgets
        yield Header()
        yield Footer()

    def on_mount(self) -> None:
        for index, widget in enumerate(self.widgets, 1):
            alpha = index * 0.1
            import pydevd_pycharm

            pydevd_pycharm.settrace(
                'localhost',
                port=5678,
                stdout_to_server=True,
                stderr_to_server=True,
                suspend=False  # Set to True if you want to pause immediately
            )
            widget.update(f"alpha={alpha:.1f}")
            widget.styles.background = Color(191, 78, 96, a=alpha)

if __name__ == "__main__":
    app = ColorApp()
    app.run()
