from stegano import lsb
from stegano.lsb import generators
import time
import os
 

class SteganoOperator:

    def __init__(self, input, output, msg):

        self.input_path = input

        self.output_path = output

        self.message = msg

 

    def hide_msg(self):

        try:

            secret = lsb.hide(self.input_path, self.message, generator=generators.eratosthenes())

            secret.save(self.output_path)

        except Exception as e:

            print(f'Error occured while hiding the message: {e}')

   

    def reveal_msg(self):

        try:

            print(lsb.reveal(self.output_path, generator=generators.eratosthenes()))

        except Exception as e:

            print(f'Error occured while revealing the message: {e}')

def print_result(dictionary: dict) -> None:
    for key, value in dictionary.items():
        print(key)
        for record in value:
            print(record)
 
messages = ["Hi!", "Hello, world!", "Greetings from the beautiful land of code!"]
images_paths = ["stegano/first_image.jpg", "stegano/second_image.png", "stegano/third_image.jpg"]
images_hidden_paths = ["stegano/first_image-hidden.jpg", "stegano/second_image-hidden.png", "stegano/third_image-hidden.jpg"]
all_times = {'first':[], 'second': [], 'third': []}

for i in range(0, len(images_paths)):
    curr_array = []
    for msg in messages:
        operator = SteganoOperator(images_paths[i], images_hidden_paths[i], msg)

        before = os.path.getsize(images_paths[i])

        start_hide = time.time()
        operator.hide_msg()
        end_hide = time.time() - start_hide

        after = os.path.getsize(images_hidden_paths[i])

        start_reveal = time.time()
        operator.reveal_msg()
        end_reveal = time.time() - start_reveal
        

        curr_array.append(f'Time taken to hide (s): {end_hide} | Time taken to reveal (s): {end_reveal} | Image size before (bytes): {before} & Image size after (bytes): {after}  & Size difference before-after(bytes): {before-after} | Message: {msg}')
    if 'first' in images_paths[i]:
        all_times['first'] = curr_array
    elif 'second' in images_paths[i]:
        all_times['second'] = curr_array
    elif 'third' in images_paths[i]:
        all_times['third'] = curr_array


print_result(all_times)
#first_op.reveal_msg()