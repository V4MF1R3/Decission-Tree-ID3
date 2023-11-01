import tkinter as tk
import pickle

class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

def load_model(file_name):
    with open(file_name, 'rb') as file:
        loaded_model = pickle.load(file)
    return loaded_model

def predict_example(x, tree):
    if tree.value is not None:
        return tree.value
    feature_value = x[tree.feature]
    if feature_value < tree.threshold:
        return predict_example(x, tree.left)
    else:
        return predict_example(x, tree.right)

# Create a simple GUI window
root = tk.Tk()
root.title("Play Tennis Predictor")

# Create labels and entry boxes for each feature
tk.Label(root, text="Outlook (Sunny/Overcast/Rain)").grid(row=0)
tk.Label(root, text="Temperature (Hot/Mild/Cold)").grid(row=1)
tk.Label(root, text="Humidity (High/Normal)").grid(row=2)
tk.Label(root, text="Wind (Weak/Strong)").grid(row=3)

entry_outlook = tk.Entry(root)
entry_temperature = tk.Entry(root)
entry_humidity = tk.Entry(root)
entry_wind = tk.Entry(root)

entry_outlook.grid(row=0, column=1)
entry_temperature.grid(row=1, column=1)
entry_humidity.grid(row=2, column=1)
entry_wind.grid(row=3, column=1)



def make_prediction_gui():
    tree = load_model("exp5.pkl")
    map = {"Sunny":2, "Overcast":0, "Rain":1, "Hot":1, "Mild":2, "Cool":0, "High":0, "Normal":1, "Weak":1, "Strong":0}
    input_array = [map[entry_outlook.get()], map[entry_temperature.get()], map[entry_humidity.get()], map[entry_wind.get()]]
    predicted_label = predict_example(input_array, tree)
    if predicted_label:
        result_label.config(text=f"Prediction:YES    You Can Play Tennis")
    else:
        result_label.config(text=f"Prediction:NO     You Can't Play Tennis")


# Create a button to trigger the prediction
predict_button = tk.Button(root, text="Predict", command=make_prediction_gui)
predict_button.grid(row=4, column=0, columnspan=2)

# Create a label for displaying the prediction
result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2)

# Run the main loop
root.mainloop()