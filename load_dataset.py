# Task 1
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
import matplotlib.pyplot as plt



# LOAD MNIST DATASET
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# display shapes of the datasets
print("Training images shape:", x_train.shape)
print("Training labels shape:", y_train.shape)
print("Testing images shape:", x_test.shape)
print("Testing labels shape:", y_test.shape)

# visualizing a sample image from the training set
plt.imshow(x_train[0], cmap='gray')
plt.title(f"Sample Digit: {y_train[0]}")
plt.show()


# normalization- Convert pixel values from 0–255 to 0–1

x_train = x_train / 255.0
x_test = x_test / 255.0

# building the model
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# model compilation
model.compile(
    optimizer='adam',  
    loss='sparse_categorical_crossentropy',  
    metrics=['accuracy']  
)
# model training
model.fit(x_train, y_train, epochs=5)

loss, accuracy = model.evaluate(x_test, y_test)

print("\nModel Accuracy:", accuracy)


# make predictions
prediction = model.predict(x_test)

predicted_label = prediction[0].argmax()

print("\nPredicted Digit:", predicted_label)
print("Actual Digit:", y_test[0])