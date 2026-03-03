import cv2
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tkinter import Tk, filedialog
import os

# ===============================
# 📂 Load and Clean Dataset
# ===============================

csv_file = "colors.csv"

try:
    df = pd.read_csv(csv_file)
    # Clean redundant labels like 'Black_approx' -> 'Black'
    df['clean_name'] = df['color_name'].apply(lambda x: x.split('_')[0])
except FileNotFoundError:
    print(f"Error: {csv_file} not found!")
    exit(1)

# ===============================
# 🎨 Convert RGB Dataset → CIELab
# ===============================

def rgb_to_lab(r, g, b):
    pixel = np.uint8([[[b, g, r]]])  # OpenCV uses BGR
    lab = cv2.cvtColor(pixel, cv2.COLOR_BGR2Lab)
    return lab[0][0]

print("-" * 30)
print("🛠  Initializing Detection Model...")
lab_features = [rgb_to_lab(row['R'], row['G'], row['B']) for _, row in df.iterrows()]

X = np.array(lab_features)
y = df['clean_name']

le = LabelEncoder()
y_encoded = le.fit_transform(y)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

knn = KNeighborsClassifier(n_neighbors=3, weights='distance', metric='euclidean')
knn.fit(X_scaled, y_encoded)

print("✅ Model Ready.")
print("📸 Press 'u' to upload | Press 'ESC' to quit")
print("-" * 30)
print(f"{'COLOR NAME':<20} | {'MATCH %':<8} | {'RGB VALUES':<15}")
print("-" * 30)

# ===============================
# 🎯 Prediction & Utility
# ===============================

def predict_color_name(rgb):
    r, g, b = rgb
    l_val, a_val, b_val = rgb_to_lab(r, g, b)
    lab_scaled = scaler.transform(np.array([[l_val, a_val, b_val]]))
    
    distances, _ = knn.kneighbors(lab_scaled, n_neighbors=1)
    prediction = knn.predict(lab_scaled)
    
    color_name = le.inverse_transform(prediction)[0]
    match_pct = max(0, 100 - int(distances[0][0] * 10)) 
    
    # --- LOG TO TERMINAL ---
    print(f"{color_name:<20} | {match_pct:>6}% | ({r}, {g}, {b})")
    
    return color_name, match_pct

def get_average_rgb(image, x, y, patch_size=11):
    half = patch_size // 2
    h, w = image.shape[:2]
    x1, y1 = max(0, x - half), max(0, y - half)
    x2, y2 = min(w, x + half + 1), min(h, y + half + 1)
    patch = image[y1:y2, x1:x2]
    avg_b, avg_g, avg_r = np.mean(patch, axis=(0, 1))
    return int(avg_r), int(avg_g), int(avg_b)

# ===============================
# 🖱 Mouse Callback & Global State
# ===============================

clicked = False
xpos = ypos = 0
selected_color_name = ""
confidence = 0
r = g = b = 0

def mouse_callback(event, x, y, flags, param):
    global xpos, ypos, clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        xpos, ypos = x, y
        clicked = True

# ===============================
# 🖼 Image Upload Handler
# ===============================

def upload_and_detect():
    global clicked, selected_color_name, confidence, r, g, b
    selected_color_name = ""
    
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
    )
    root.destroy()

    if not file_path: return

    img = cv2.imread(file_path)
    if img is None: return

    win_name = "Image (ESC to go back)"
    cv2.namedWindow(win_name)
    cv2.setMouseCallback(win_name, mouse_callback)

    while True:
        display = img.copy()
        if clicked:
            r, g, b = get_average_rgb(img, xpos, ypos)
            selected_color_name, confidence = predict_color_name((r, g, b))
            clicked = False

        if selected_color_name:
            cv2.drawMarker(display, (xpos, ypos), (0, 255, 0), cv2.MARKER_CROSS, 15, 2)
            cv2.putText(display, f"{selected_color_name} ({confidence}%)", (xpos + 10, ypos - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        cv2.imshow(win_name, display)
        if cv2.waitKey(1) & 0xFF == 27: break
            
    cv2.destroyWindow(win_name)
    selected_color_name = ""

# ===============================
# 📷 Main Webcam Loop
# ===============================

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    upload_and_detect()
else:
    cv2.namedWindow("Live Color Detector")
    cv2.setMouseCallback("Live Color Detector", mouse_callback)

    while True:
        ret, frame = cap.read()
        if not ret: break
        frame = cv2.flip(frame, 1)
        display_frame = frame.copy()

        if clicked:
            r, g, b = get_average_rgb(frame, xpos, ypos)
            selected_color_name, confidence = predict_color_name((r, g, b))
            clicked = False

        if selected_color_name:
            cv2.drawMarker(display_frame, (xpos, ypos), (0, 255, 0), cv2.MARKER_CROSS, 15, 2)
            cv2.putText(display_frame, f"{selected_color_name}", (xpos + 10, ypos),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        cv2.imshow("Live Color Detector", display_frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == 27: break
        elif key == ord('u'):
            upload_and_detect()
            cv2.setMouseCallback("Live Color Detector", mouse_callback)

    cap.release()
    cv2.destroyAllWindows()