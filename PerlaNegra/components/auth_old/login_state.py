from .local_auth_state import LocalAuthState


class LoginState(LocalAuthState):
    """Define your login state here."""

    username: str = ""
    password: str = ""

    def login(self, username, password):
        # authenticate
        # authenticate(...)

        # Set the var on the parent state.
        self.current_user = username
