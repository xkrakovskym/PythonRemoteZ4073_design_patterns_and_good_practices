from abc import ABC, abstractmethod


class ChatRoomMediator(ABC):
    @abstractmethod
    def show_message(self, user, message):
        pass


class ChatRoom(ChatRoomMediator):
    def show_message(self, user, message):
        print(f"[{user.get_name()}]: {message}")


class User:
    def __init__(self, name, chat_room):
        self.name = name
        self.chat_room = chat_room

    def get_name(self):
        return self.name

    def send_message(self, message):
        self.chat_room.show_message(self, message)


chat_room = ChatRoom()

user1 = User("Alice", chat_room)
user2 = User("Bob", chat_room)


user1.send_message("Hi there!")
user2.send_message("Hello.")
