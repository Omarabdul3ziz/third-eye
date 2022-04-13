
from tflite_runtime.interpreter import Interpreter
import numpy as np
from PIL import Image

def what(image_path="/home/pi/third-eye/temp/image.jpg"):
    filename = image_path
    model_path = "/home/pi/third-eye/object_recognition/mobilenet/mobilenet_v1_1.0_224_quant.tflite"
    label_path = "/home/pi/third-eye/object_recognition/mobilenet/labels_mobilenet_quant_v1_224.txt"
    top_k_results = 1

    with open(label_path, 'r') as f:
        labels = list(map(str.strip, f.readlines()))

    # Load TFLite model and allocate tensors
    interpreter = Interpreter(model_path=model_path)
    interpreter.allocate_tensors()

    # Get input and output tensors.
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Read image
    img = Image.open(filename).convert('RGB')

    # Get input size
    input_shape = input_details[0]['shape']
    size = input_shape[:2] if len(input_shape) == 3 else input_shape[1:3]

    # Preprocess image
    img = img.resize(size)
    img = np.array(img)

    # Add a batch dimension
    input_data = np.expand_dims(img, axis=0)

    # Point the data to be used for testing and run the interpreter
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    # Obtain results and map them to the classes
    predictions = interpreter.get_tensor(output_details[0]['index'])[0]

    # Get indices of the top k results
    top_k_indices = np.argsort(predictions)[::-1][:top_k_results]

    results = []
    for i in range(top_k_results):
        results.append(labels[top_k_indices[i]])
        
    return results[0]

