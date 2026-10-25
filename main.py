import os
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Plant Disease Recognition System",
    page_icon="🌿",
    layout="wide"
)

# Class names corresponding to 38 dataset categories
CLASS_NAMES = [
    'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
    'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 
    'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
    'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 
    'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
    'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
    'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 
    'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 
    'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
    'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
    'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
    'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy'
]

# Cache model so it only loads once into memory
@st.cache_resource
def load_disease_model():
    model_dir = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.join(model_dir, "trained_plant_disease_model.keras"),
        os.path.join(model_dir, "trained_plant_disease_model.h5"),
        "trained_plant_disease_model.keras",
        "trained_plant_disease_model.h5"
    ]
    for path in candidates:
        if os.path.exists(path):
            try:
                # Check if it's an HDF5 file with .keras extension
                with open(path, "rb") as f:
                    header = f.read(4)
                if header.startswith(b"\x89HDF"):
                    # Keras 3 requires .h5 extension to load HDF5 format
                    import shutil
                    temp_h5 = path + ".temp.h5"
                    shutil.copyfile(path, temp_h5)
                    model = tf.keras.models.load_model(temp_h5)
                    # Convert to genuine Keras 3 format for future runs
                    try:
                        model.save(path)
                    except Exception:
                        pass
                    if os.path.exists(temp_h5):
                        os.remove(temp_h5)
                    return model
                return tf.keras.models.load_model(path)
            except Exception as e:
                st.warning(f"Note: Error loading {path}: {e}")
                continue
    return None

def format_class_name(raw_name):
    """Converts raw dataset class name like 'Tomato___Early_blight' to human-friendly text."""
    parts = raw_name.split("___")
    plant = parts[0].replace("_", " ").strip()
    condition = parts[1].replace("_", " ").strip() if len(parts) > 1 else ""
    return f"{plant} - {condition}"

def model_prediction(test_image, model):
    image = Image.open(test_image).convert("RGB")
    image = image.resize((128, 128))
    input_arr = np.array(image, dtype=np.float32)
    input_arr = np.expand_dims(input_arr, axis=0)
    predictions = model.predict(input_arr, verbose=0)
    result_index = int(np.argmax(predictions))
    confidence = float(np.max(predictions)) * 100.0
    return result_index, confidence

# Sidebar navigation
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Disease Recognition"])

# ----------------- HOME PAGE -----------------
if app_mode == "Home":
    st.header("PLANT DISEASE RECOGNITION SYSTEM")
    
    image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "home_page.jpeg")
    if os.path.exists(image_path):
        st.image(image_path, use_container_width=True)
    
    st.markdown("""
    Welcome to the Plant Disease Recognition System! 🌿🔍
    
    Our mission is to help in identifying plant diseases efficiently. Upload an image of a plant, and our system will analyze it to detect any signs of diseases. Together, let's protect our crops and ensure a healthier harvest!

    ### How It Works
    1. **Upload Image:** Go to the **Disease Recognition** page and upload an image of a plant with suspected diseases.
    2. **Analysis:** Our system will process the image using advanced algorithms to identify potential diseases.
    3. **Results:** View the results and recommendations for further action.

    ### Why Choose Us?
    - **Accuracy:** Our system utilizes state-of-the-art machine learning techniques for accurate disease detection.
    - **User-Friendly:** Simple and intuitive interface for seamless user experience.
    - **Fast and Efficient:** Receive results in seconds, allowing for quick decision-making.

    ### Get Started
    Click on the **Disease Recognition** page in the sidebar to upload an image and experience the power of our Plant Disease Recognition System!

    ### About Us
    Learn more about the project, our team, and our goals on the **About** page.
    """)

# ----------------- ABOUT PAGE -----------------
elif app_mode == "About":
    st.header("About")
    st.markdown("""
    #### About Dataset
    This dataset is recreated using offline augmentation from the original PlantVillage dataset.
    This dataset consists of about **87K RGB images** of healthy and diseased crop leaves categorized into **38 different classes**.
    The total dataset is divided into an 80/20 ratio of training and validation sets preserving directory structure.
    
    #### Dataset Distribution
    1. **Train:** 70,295 images
    2. **Test:** 33 images
    3. **Validation:** 17,572 images
    
    #### Supported Plant Species & Categories (38 classes):
    - **Apple:** Scab, Black Rot, Cedar Apple Rust, Healthy
    - **Blueberry:** Healthy
    - **Cherry:** Powdery Mildew, Healthy
    - **Corn (Maize):** Cercospora Leaf Spot, Common Rust, Northern Leaf Blight, Healthy
    - **Grape:** Black Rot, Esca (Black Measles), Leaf Blight, Healthy
    - **Orange:** Huanglongbing (Citrus Greening)
    - **Peach:** Bacterial Spot, Healthy
    - **Pepper (Bell):** Bacterial Spot, Healthy
    - **Potato:** Early Blight, Late Blight, Healthy
    - **Raspberry:** Healthy
    - **Soybean:** Healthy
    - **Squash:** Powdery Mildew
    - **Strawberry:** Leaf Scorch, Healthy
    - **Tomato:** Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Spider Mites, Target Spot, Yellow Leaf Curl Virus, Mosaic Virus, Healthy
    """)

# ----------------- DISEASE RECOGNITION PAGE -----------------
elif app_mode == "Disease Recognition":
    st.header("Disease Recognition")
    
    model = load_disease_model()
    if model is None:
        st.error("⚠️ Model file `trained_plant_disease_model.keras` not found! Please run `download_model.py` or `run.bat` to download the pre-trained weights.")
    else:
        st.info("💡 Tip: You can test with sample images from the `sample_test_images/` folder.")
        test_image = st.file_uploader("Choose an Image:", type=["jpg", "jpeg", "png"])
        
        col1, col2 = st.columns([1, 1])
        
        if test_image is not None:
            with col1:
                st.subheader("Uploaded Image")
                st.image(test_image, use_container_width=True)
            
            with col2:
                st.subheader("Prediction")
                if st.button("Predict Disease", type="primary"):
                    with st.spinner("Analyzing plant leaf..."):
                        result_index, confidence = model_prediction(test_image, model)
                        raw_label = CLASS_NAMES[result_index]
                        friendly_label = format_class_name(raw_label)
                        
                        st.snow()
                        if "healthy" in raw_label.lower():
                            st.success(f"🌱 **Result: {friendly_label}**")
                        else:
                            st.warning(f"⚠️ **Result: {friendly_label}**")
                        
                        st.metric(label="Model Confidence", value=f"{confidence:.2f}%")
                        st.caption(f"Raw Label Index: `{raw_label}` (class {result_index})")
        else:
            st.write("Please upload a leaf image to begin.")
