from email.header import Header

from textual.app import App, ComposeResult
from textual.screen import ModalScreen
from textual.widgets import Static, Button, Header, Footer
from textual.containers import Container

class WelcomeScreen(ModalScreen):

    def compose(self) -> ComposeResult:
        with Container(id="welcome-box"):
            yield Static("SOLAR_OS v2.4", id="welcome-title")
            yield Static("Remote Monitoring Station\nInitializing...", id="welcome-message")
            yield Button("Enter System", id="enter-btn", variant="primary")
            # yield Button("Click me!", id="button", variant="primary")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "enter-btn":
            self.app.log("Button pressed!")
            self.dismiss(result=None)


class MyApp(App):
    CSS_PATH = "tui_stypes.tcss"
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("d", "toggle_dark", "Toggle dark mode"),
        ("d", "randon_action", "BITE ME"),
    ]
    def compose(self) -> ComposeResult:
        yield Static("Main dashboard content")
        yield Header()
        yield Footer()

    def on_welcome_dismissed(self) -> None:
        self.app.log("Welcome screen dismissed!")

    def on_mount(self) -> None:
        self.push_screen(WelcomeScreen())

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

if __name__ == "__main__":
    MyApp().run()