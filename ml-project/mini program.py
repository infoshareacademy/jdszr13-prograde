import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import Entry, Button, Label
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn import svm, metrics
from sklearn.metrics import classification_report
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Funkcja do przekształcenia danych i podziału na zbiór treningowy i testowy
def process_and_split_data():
    df = pd.read_csv(r'C:\Users\neumannp\OneDrive - Jabil\Desktop\Bootcamp\Grupa Prograte\jdszr13-prograde\ml-project\data/neo_v2.csv')

    # Przekształcenie danych
    droppable = ['id', 'name', 'est_diameter_min', 'orbiting_body', 'sentry_object']
    for drop in droppable:
        df.drop(drop, inplace=True, axis='columns')

    df_X = df.drop('hazardous', axis='columns')

    dataset = df_X
    numerical_features = ['est_diameter_max', 'relative_velocity', 'miss_distance', 'absolute_magnitude']

    numeric_pipeline = Pipeline(steps=[
        ('impute', SimpleImputer(strategy='mean')),
        ('scale', MinMaxScaler())
    ])

    full_processor = ColumnTransformer(transformers=[
        ('number', numeric_pipeline, numerical_features),
    ])

    full_processor.fit(dataset)
    X = pd.DataFrame(full_processor.transform(dataset), columns=full_processor.get_feature_names_out())

    X = X.to_numpy()
    y = df['hazardous'].to_numpy()

    # Podział na zbiór treningowy i testowy
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

    print(f"Rozmiar X_train: {X_train.shape}")
    print(f"Rozmiar X_test: {X_test.shape}")
    print(f"Rozmiar y_train: {y_train.shape}")
    print(f"Rozmiar y_test: {y_test.shape}")

    text1 = text1_entry.get()
    text2 = text2_entry.get()
    text3 = text3_entry.get()
    text4 = text4_entry.get()
    print(f"Tekst 1: {text1}")
    print(f"Tekst 2: {text2}")
    print(f"Tekst 3: {text3}")
    print(f"Tekst 4: {text4}") 

    
    text1 = float(text1_entry.get())
    text2 = float(text2_entry.get())
    text3 = float(text3_entry.get())
    text4 = float(text4_entry.get())

    # Stwórz tablicę NumPy z wprowadzonymi wartościami
    X_test = np.array([[text1, text2, text3, text4]])

    y_test = y_test[:1]

    clf = svm.SVC(kernel='rbf', gamma='scale', C=100, probability=True)
    clf.fit(X_train,y_train)

    y_proba = clf.predict_proba(X_test)[:,1]
    y_predicted = y_proba > 0.12

    print(classification_report(y_test, y_predicted))

    display = metrics.ConfusionMatrixDisplay.from_estimator(clf, X_test, y_test)
    
    # Utwórz nowe okno Tkinter
    matrix_window = tk.Tk()
    matrix_window.title("Confusion Matrix")
    
    # Utwórz nowy wykres Matplotlib Figure
    fig, ax = plt.subplots(figsize=(6, 6))
    display.plot(ax=ax)
    
    # Utwórz kontrolkę do wyświetlenia wykresu w oknie Tkinter
    canvas = FigureCanvasTkAgg(fig, master=matrix_window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    #metrics.ConfusionMatrixDisplay.from_predictions(y_test, y_predicted)


# Funkcja do rysowania trajektorii lotu na podstawie wybranych wartości
def draw_trajectory():
    selected_name = name_entry.get()  # Pobierz nazwę z pola tekstowego
    selected_data = data[data['name'] == selected_name]

    if selected_data.empty:
        print("Brak danych dla wybranej nazwy.")
        return

    average_diameter = (selected_data['est_diameter_min'] + selected_data['est_diameter_max']) / 2

    miss_distance = selected_data['miss_distance']
    relative_velocity = selected_data['relative_velocity']

    # Rysowanie trajektorii lotu
    plt.figure(figsize=(10, 6))
    left_points = selected_data[selected_data['miss_distance'] <= miss_distance.values[0]]
    right_points = selected_data[selected_data['miss_distance'] > miss_distance.values[0]]

    plt.scatter(left_points['miss_distance'], left_points['relative_velocity'], label='Trajektoria lotu komety (lewa strona)', color='blue', s=average_diameter.values[0] * 100)

    for i in range(len(right_points)):
        x = right_points['miss_distance'].values[i]
        y = right_points['relative_velocity'].values[i]
        s = average_diameter.values[i] * 100
        plt.scatter(x, y, color='blue', s=s)

        plt.plot([x, x], [y, y + s * 50], color='blue', linewidth=1.5)

        if x > miss_distance.values[0]:
            plt.annotate("^", (x, y), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=10, color='blue')

    plt.xlabel('Miss Distance (km)')
    plt.ylabel('Relative Velocity (km/s)')
    plt.title(f'Trajektoria lotu komety dla {selected_name}')
    plt.grid(True)
    plt.legend()

    earth_image = plt.imread(r"C:\Users\\neumannp\\OneDrive - Jabil\\Desktop\\dzien-ziemi.webp")
    imagebox = OffsetImage(earth_image, zoom=0.1)
    ab = AnnotationBbox(imagebox, (miss_distance.values[0], relative_velocity.values[0]))
    plt.gca().add_artist(ab)
#ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x / 1e6:.0f}'))

    plt.show()

# Ścieżka do pliku CSV
csv_file = "C:\\Users\\neumannp\\OneDrive - Jabil\\Desktop\\Bootcamp\\Grupa Prograte\\jdszr13-prograde\\ml-project\\data\\neo_v2.csv"

# Wczytanie danych z pliku CSV
data = pd.read_csv(csv_file, sep=',')

# Tworzenie okna Tkinter
root = tk.Tk()
root.title("Rysowanie trajektorii lotu komety")

# Pole tekstowe do wprowadzenia nazwy
name_label = Label(root, text="Wprowadź nazwę ciała obcego:")
name_label.pack()
name_entry = Entry(root)
name_entry.pack()

# Przycisk do rysowania trajektorii
draw_button = Button(root, text="Rysuj trajektorię", command=draw_trajectory)
draw_button.pack()

# Pola tekstowe
text1_label = Label(root, text="Mumber__est_diameter_max:")
text1_label.pack()
text1_entry = Entry(root)
text1_entry.pack()

text2_label = Label(root, text="Number__relative_velocity:")
text2_label.pack()
text2_entry = Entry(root)
text2_entry.pack()

text3_label = Label(root, text="Number__miss_distance:")
text3_label.pack()
text3_entry = Entry(root)
text3_entry.pack()


text4_label = Label(root, text="Number__absolute_magnitude:")
text4_label.pack()
text4_entry = Entry(root)
text4_entry.pack()

# Przycisk do zatwierdzania wartości tekstowych
confirm_button = Button(root, text="Zatwierdź", command=process_and_split_data)
confirm_button.pack()

root.mainloop()
