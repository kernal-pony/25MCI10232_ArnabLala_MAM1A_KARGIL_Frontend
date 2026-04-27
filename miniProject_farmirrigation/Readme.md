## 👨‍💻 Author

**Arnab Lala**

**UID-25MCI10232**

**Branch-25MAM1(A)**

**Date-27/04/26**

---

# 💧 Farm Irrigation Optimizer

A smart irrigation management system that uses **Data Structures and Algorithms** to optimize water distribution across agricultural fields. The project compares multiple allocation strategies and visualizes results through an interactive web interface built with **Streamlit**.

---

## 🚀 Features

* 🌐 **Graph-based Irrigation Network**

  * Models water sources and fields as a network
* 🧠 **Multiple Algorithms Implemented**

  * Greedy Allocation
  * Priority-based Allocation
  * Efficiency-based Allocation
* 📊 **Performance Comparison**

  * Efficiency (%)
  * Water Allocated
  * Water Loss
* 🎛️ **Interactive UI**

  * Adjustable water capacities
  * User-defined field input
* 🔥 **Network Visualization**

  * Graph representation of irrigation system
* 📈 **Dynamic Charts**

  * Algorithm comparison using bar graphs

---

## 🧠 Data Structures Used

* **Graph** → Models irrigation network (sources → fields)
* **Hash Maps (Dictionaries)** → Store nodes and connections
* **Lists & Sorting** → Used in algorithm execution

---

## ⚙️ Algorithms Used

### 1. Greedy Algorithm

* Allocates water to nearest fields first

### 2. Priority-Based Algorithm

* Allocates based on crop importance

### 3. Efficient Allocation Algorithm

* Minimizes water loss using distance-based sorting

---

## 🏗️ Project Structure

```
farmirrigation/
│
├── farmirrigation.py   # Main Streamlit app
├── venv/               # Virtual environment
├── requirements.txt    # Dependencies
```

---

## 🧪 Installation & Setup

### 1. Clone or Download Project

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install streamlit matplotlib networkx
```

---

## ▶️ Run the Application

```bash
streamlit run farmirrigation.py
```

Then open in browser:

```
http://localhost:8501
```

---

## 🎯 How It Works

1. User inputs water capacity and field parameters
2. System builds irrigation network (graph)
3. Algorithms run independently
4. Results are compared and visualized
5. Best performing strategy is identified

---

## 📸 Output Screens

* Network Graph Visualization
* Algorithm Efficiency Chart
* Allocation vs Loss Comparison

---

## 🎓 Learning Outcomes

* Practical application of **Graph Data Structure**
* Understanding of **Greedy Algorithms**
* Visualization of algorithm performance
* Building interactive apps using Streamlit

---

## 📌 Future Improvements

* Water flow animation
* Export results as PDF
* Real-time data integration (IoT sensors)
* Advanced optimization (AI/ML models)

---


## ⭐ Conclusion

This project demonstrates how **Data Structures and Algorithms can solve real-world problems** like irrigation management, making systems more efficient, scalable, and intelligent.
