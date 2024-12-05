from platformdirs import user_cache_dir


class BaseObserver:
    def __init__(self, chat_channel):
        self._chat_channel = chat_channel
        chat_channel.subscribe(self)

    def handle_message(self, message, user_type):
        pass

    def get_observer_type(self):
        pass

    def send_message(self, message):
        self._chat_channel.send_message(message, self.get_observer_type())


class UserObserver(BaseObserver):
    def __init__(self, chat_channel, user_name):
        super().__init__(chat_channel)
        self.user_name = user_name
        print(f"User {self.user_name} is joining the {chat_channel.get_name()}")

    def handle_message(self, message, user_type):
        if user_type != "ADMIN":
            print(f"{self.user_name} sees message {message}")

    def get_observer_type(self):
        return "USER"


class AdminObserver(BaseObserver):
    def __init__(self, chat_channel, admin_name):
        super().__init__(chat_channel)
        self.admin_name = admin_name
        print(f"Admin {self.admin_name} is joining the {chat_channel.get_name()}")

    def handle_message(self, message, user_type):
        print(
            f"{self.admin_name} sees message {message} from user whose type is {user_type}"
        )

    def get_observer_type(self):
        return "ADMIN"


class ChatChannel:
    def __init__(self, name):
        self.name = name
        self.observers = []
        self.messages = []

    def subscribe(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def unsubscribe(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def send_message(self, message, observer_type):
        self.messages.append(message)
        self.notify_about_changes(message, observer_type)

    def notify_about_changes(self, message, observer_type):
        for observer in self.observers:
            observer.handle_message(message, observer_type)

    def get_name(self):
        return self.name


chat_channel = ChatChannel("Design Patterns")

user_a = UserObserver(chat_channel, "Alice")
user_b = UserObserver(chat_channel, "Bob")
admin_a = AdminObserver(chat_channel, "Admin")
admin_b = AdminObserver(chat_channel, "SuperAdmin")

user_a.send_message("Hi all")
user_b.send_message("Hello")
admin_a.send_message("Only for admins")
print(chat_channel.messages)
