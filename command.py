from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class WriteCommand(Command):
    def __init__(self, receiver, text):
        self.receiver = receiver
        self.text = text

    def execute(self):
        self.receiver.write(self.text)

    def undo(self):
        self.receiver.undo()


class TextEditor:
    def __init__(self):
        self.text = ""
        self.history = []

    def write(self, text):
        self.history.append(self.text)
        self.text += text
        print(f"Current Text: {self.text}")

    def undo(self):
        if self.history:
            self.text = self.history.pop()
        print(f"Undo Text: {self.text}")

    def redo(self, text):
        self.history.append(self.text)
        self.text += text
        print(f"Redo Text: {self.text}")


class TextEditorInvoker:
    def __init__(self):
        self.commands = []
        self.undo_commands = []

    def execute_command(self, command):
        command.execute()
        self.commands.append(command)
        self.undo_commands.clear()

    def undo(self):
        if self.commands:
            command = self.commands.pop()
            command.undo()
            self.undo_commands.append(command)

    def redo(self):
        if self.undo_commands:
            command = self.undo_commands.pop()
            command.execute()
            self.commands.append(command)


editor = TextEditor()
invoker = TextEditorInvoker()

command1 = WriteCommand(editor, "Hello ")
invoker.execute_command(command1)

command2 = WriteCommand(editor, "World!")
invoker.execute_command(command2)

invoker.undo()
