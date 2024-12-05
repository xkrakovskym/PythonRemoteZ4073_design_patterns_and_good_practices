import random


class Credentials:
    def get_credentials(self, user_id):
        pass


class AWSSignature(Credentials):
    def get_credentials(self, user_id):
        return "98f92d42-66c7-4ce4-a834-087a783133e7"


class BearerToken(Credentials):
    def get_credentials(self, user_id):
        return "1/mZ1edKKACtPAb7zGlwSzvs72PvhAbGmB8K1ZrGxpcNM"


class UserNameAndPasswordCredentials(Credentials):
    def get_credentials(self, user_id):
        return "andrew:Andrew_123"


class AuthenticationHandler:
    def authenticate(self, credentials):
        pass

    def supports(self, credentials):
        pass


class AWSAuthenticationHandler(AuthenticationHandler):
    def authenticate(self, credentials):
        if self.supports(credentials):
            return self.authenticate_in_aws(credentials)
        return False

    def supports(self, credentials):
        return isinstance(credentials, AWSSignature)

    def authenticate_in_aws(self, credentials):
        return random.randint(1, 3) == 1


class BearerTokenAuthenticationHandler(AuthenticationHandler):
    def authenticate(self, credentials):
        if self.supports(credentials):
            return self.is_token_valid(credentials)
        return False

    def supports(self, credentials):
        return isinstance(credentials, BearerToken)

    def is_token_valid(self, token):
        return random.randint(1, 3) == 1


class UserNameAndPasswordAuthenticationHandler(AuthenticationHandler):
    def authenticate(self, credentials):
        if self.supports(credentials):
            return self.is_password_valid(credentials)
        return False

    def supports(self, credentials):
        return isinstance(credentials, UserNameAndPasswordCredentials)

    def is_password_valid(self, password):
        return random.randint(1, 3) == 1


class ChainAuthenticationElement:
    def __init__(self, authentication_handler, next_element=None):
        self._authentication_handler = authentication_handler
        self._next_element = next_element

    def authenticate(self, credentials):
        if self._authentication_handler.authenticate(credentials):
            print(
                f"Atuhencticated by {self._authentication_handler.__class__.__name__}"
            )
            return True
        elif self._next_element:
            return self._next_element.authenticate(credentials)
        else:
            print("No more authentication handlers")
        return False


username_password_handler = UserNameAndPasswordAuthenticationHandler()
bearer_token_handler = BearerTokenAuthenticationHandler()
aws_signature_handler = AWSAuthenticationHandler()

last_element = ChainAuthenticationElement(aws_signature_handler)
middle_element = ChainAuthenticationElement(bearer_token_handler, last_element)
first_element = ChainAuthenticationElement(username_password_handler, middle_element)

first_element.authenticate(AWSSignature())
