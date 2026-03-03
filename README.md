<h1 align="center" id="title">🎨 KNN-Based-Real-Time-Color-Detection-using-OpenCV</h1>

<p align="center"><img src="assets\profile.png" alt="project-image"></p>

<p id="description">This project implements a real-time color detection system using the K-Nearest Neighbors (KNN) machine learning algorithm. It captures pixel RGB values from webcam or uploaded images and predicts the closest matching color name using Euclidean distance. The project demonstrates practical application of supervised learning in computer vision.</p>

<p align="center">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green" alt="shields">
  <img src="https://img.shields.io/badge/Python-3.x-blue" alt="shields">
  <img src="https://img.shields.io/badge/Machine-Learning-orange" alt="shields">
</p>

<h2>📸 Demo</h2>
<p align="center"><img src="assets\demo.png" alt="Demo Screenshot"></p>

<h2>⚙️ System Workflow</h2>
<p>To understand how the application processes inputs and predicts colors, refer to the workflow below:</p>

<h2>🧐 Features</h2>
<p>Here're some of the project's best features:</p>
<ul>
  <li>Real-time webcam color detection</li>
  <li>Upload image support</li>
  <li>RGB value extraction on mouse click</li>
  <li>KNN-based color classification</li>
  <li>Displays color name with RGB values</li>
  <li>Simple and lightweight implementation</li>
  <li>Stores detected colors in session</li>
</ul>

<h2>🧠 Algorithm Used</h2>

<p><b>K-Nearest Neighbors (KNN)</b></p>
<ul>
  <li><b>Input Features:</b> RGB values (R, G, B)</li>
  <li><b>Output Label:</b> Color Name</li>
  <li><b>Distance Metric:</b> Euclidean Distance</li>
  <li><b>Neighbors Used:</b> k = 1</li>
</ul>
<p>The model finds the closest RGB match from the dataset and predicts its corresponding color name.</p>

<h2>📂 Project Structure</h2>
<pre><code>├── assets/
│   └── demo.png
├── colors.csv
├── color_detector.py
└── README.md</code></pre>

<h2>🛠️ Installation Steps:</h2>
<pre><code>git clone https://github.com/your-username/knn-color-detection.git
cd knn-color-detection
pip install opencv-python numpy pandas scikit-learn
python color_detector.py</code></pre>

<h2>🎮 How to Use</h2>
<ul>
  <li>📸 <b>Press 'u'</b> → Upload image</li>
  <li>🖱️ <b>Click anywhere</b> on image or webcam feed → Detect color</li>
  <li>❌ <b>Press ESC</b> → Exit program</li>
</ul>

<h2>📊 Dataset</h2>
<p>The project uses a <code>colors.csv</code> dataset containing RGB values and their corresponding color names. Example:</p>
<table>
  <tr>
    <th>R</th>
    <th>G</th>
    <th>B</th>
    <th>Color Name</th>
  </tr>
  <tr>
    <td>255</td>
    <td>0</td>
    <td>0</td>
    <td>Red</td>
  </tr>
  <tr>
    <td>0</td>
    <td>255</td>
    <td>0</td>
    <td>Green</td>
  </tr>
  <tr>
    <td>0</td>
    <td>0</td>
    <td>255</td>
    <td>Blue</td>
  </tr>
</table>

<h2>💻 Built with</h2>
<p>Technologies used in the project:</p>
<ul>
  <li>Python</li>
  <li>OpenCV</li>
  <li>NumPy</li>
  <li>Pandas</li>
  <li>Scikit-learn</li>
  <li>Tkinter</li>
</ul>

<h2>📈 Future Improvements</h2>
<ul>
  <li>Increase K value for better accuracy</li>
  <li>Add confidence score</li>
  <li>Convert into GUI application</li>
  <li>Deploy as web app using Flask</li>
  <li>Use deep learning for advanced color segmentation</li>
</ul>

<h2>🎯 Applications</h2>
<ul>
  <li>Image Processing Projects</li>
  <li>Computer Vision Learning</li>
  <li>Design & UI Color Analysis</li>
  <li>Educational ML Demonstration</li>
</ul>
