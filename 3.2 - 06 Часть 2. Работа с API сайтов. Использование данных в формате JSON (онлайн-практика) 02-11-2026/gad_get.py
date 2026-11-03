from abc import ABC, abstractmethod

# class Gadget(ABC):
#     @abstractmethod
#     def talk(self):
#         ...
#
#     @abstractmethod
#     def inet(self):
#         ...
#
#     @abstractmethod
#     def video(self):
#         ...


# class Smartphone(Gadget):
#     def talk(self):
#         print('talk')
#
#     def inet(self):
#         print('inet')
#
#     def video(self):
#         print('video')


# class Telehone(Gadget):
#     def talk(self):
#         print('talk')
#
#     def inet(self):
#         pass
#
#     def video(self):
#         pass
#

class Talk(ABC):
    @abstractmethod
    def talk(self):
        ...

class Video(ABC):
    @abstractmethod
    def video(self):
        ...

class Inet(ABC):
    @abstractmethod
    def inet(self):
        ...

classes = (Talk, Inet, Video)

class Smartphone(*classes):
    def talk(self):
        print('talk')

    def inet(self):
        print('inet')

    def video(self):
        print('video')


class Telehone(Talk):
    def talk(self):
        print('talk')


sm = Smartphone()
sm.talk()
sm.video()
sm.inet()