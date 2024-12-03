from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def notify(self, message: str):
        pass


class EmailNotification(Notification):
    def notify(self, message: str):
        return f"Email sent with message: {message}"


class SMSNotification(Notification):
    def notify(self, message: str):
        return f"SMS sent with message: {message}"


class PushNotification(Notification):
    def notify(self, message: str):
        return f"Push notification sent with message: {message}"


class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self) -> Notification:
        pass


class EmailNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return EmailNotification()


class SMSNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return SMSNotification()


class PushNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return PushNotification()


def send_notification(factory: NotificationFactory, message: str):
    notification = factory.create_notification()
    print(notification.notify(message))


email_factory = EmailNotificationFactory()
sms_factory = SMSNotificationFactory()
push_factory = PushNotificationFactory()

send_notification(email_factory, "Hello via Email!")
send_notification(sms_factory, "Hello via SMS!")
send_notification(push_factory, "Hello via Push Notification!")