from keras.datasets import mnist
from keras.models import load_model
import sys
import random

# np.set_printoptions(threshold=sys.maxsize)


class AI_Digit:

    def __init__(self):
        self.fill_numbers()

    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()

    train_images = train_images.reshape((60000, 28 * 28))
    train_images = train_images.astype('float32') / 255

    rand = random.randint(0, 3000)
    model = load_model('numbers_model')

    numbers = {
        "0": [],
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": [],
        "6": [],
        "7": [],
        "8": [],
        "9": [],
    }

    """
         Mapping mnist digits(images) to 'numbers' dictionary 
    """
    def fill_numbers(self):
        for n, l in zip(self.train_images, self.train_labels):
            self.numbers[str(l)].append(n)

    """
    Faking the handwritten digits recognition
    
        - Picking one random image of provided digit(num_) from 'numbers'
        - Recognize image and map output to 'answer'
        - Consider ~1 as an desired prediction  
    """
    def spit_num(self, num_):
        outputs = {
            "0": [],
            "1": [],
            "2": [],
            "3": [],
            "4": [],
            "5": [],
            "6": [],
            "7": [],
            "8": [],
            "9": [],
        }

        num = self.numbers[str(num_)][self.rand]
        num = num.reshape((-1, 28 * 28))

        pred = self.model.predict(num)
        pred = pred.reshape((10, 1))

        for i, num in enumerate(pred):
            outputs[str(i)].append(num)

        answer = []
        for k, v in outputs.items():
            # zmienic ten warunek na cos pewniejszego
            if v[0] > 0.9:
                answer = int(k)
        return answer
