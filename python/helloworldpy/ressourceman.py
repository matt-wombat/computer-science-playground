from contextlib import contextmanager
from email.message import Message

@contextmanager
def message_from_template1(basefile, sender, receiver):
  template_file = open(basefile, 'r')
  message_file = open(f"temp.txt", 'w')

  try:
    message_file.write(f"Hello {receiver}, \n\n")
    message_file.write(template_file.read())
    message_file.write(f"\n\nResistance is futile, {sender} \n\n")
    yield message_file

  finally:
    template_file.close()
    message_file.close()


class MessageFromTemplate2:
  def __init__(self, sender, receiver):
    self.sender = sender
    self.receiver = receiver
    self.file = open(f"temp.txt", 'w')

  def __enter__(self):
    self.file.write(f'Dear {self.receiver}\n\n')
    return self.file
  
  def __exit__(self, exc_type, exc_value, Traceback):
    self.file.write('\n\n')
    self.file.write(f'Sincerely {self.sender}\n\n')
    self.file.close()


def res_man_func():
    with create_message_file("zenofpython.txt", "The Borg Queen", "Seven of Nine") as message_file:
        print('Card Generated! \n')

    with open("temp.txt", "r") as message_file:
        print(message_file.read())


def res_man_class():
    with MessageFromTemplate2('Seven of Nine','Borg Queen') as message_file:
        message_file.write('"Impossible" is a word that humans use far too often.')

    with open('temp.txt','r') as message_file:
        print(message_file.read())
