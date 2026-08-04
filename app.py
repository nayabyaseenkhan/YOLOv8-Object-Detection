import streamlit as st
from ultralytics import YOLO
from PIL import Image
import pandas as pd
import plotly.express as px
import io
import tempfile

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="YOLOv8 Object Detection",
    page_icon="🎯",
    layout="wide"
)

# ---------------------------------------------------
# Custom CSS
# ---------------------------------------------------

st.markdown("""
<style>

.main{
    background-color:#f8fafc;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

.title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#2563EB;
}

.subtitle{
    text-align:center;
    color:#666666;
    font-size:20px;
    margin-bottom:20px;
}

.metric-card{
    background:#ffffff;
    padding:15px;
    border-radius:12px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
}

.footer{
    text-align:center;
    color:gray;
    padding:20px;
    font-size:15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Load YOLO Model
# ---------------------------------------------------

@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")

model = load_model()

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

st.sidebar.image(
    "https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg",
    use_container_width=True
)

st.sidebar.title("📌 Project Information")

st.sidebar.markdown("""
### Model
YOLOv8 Nano

### Framework
PyTorch

### Library
Ultralytics

### Language
Python

### Interface
Streamlit

### Developer
Nayab Yaseen Khan
""")

st.sidebar.divider()

st.sidebar.info("""
This application detects multiple objects
using a pre-trained YOLOv8 Deep Learning model.
""")

# ---------------------------------------------------
# Header
# ---------------------------------------------------

st.markdown("""
<div class='title'>
🎯 Real-Time Object Detection using YOLOv8
</div>

<div class='subtitle'>
Deep Learning | PyTorch | OpenCV | Streamlit
</div>
""", unsafe_allow_html=True)

st.write(
"""
Upload an image and click **Detect Objects**.

Supported Formats

- JPG
- JPEG
- PNG
"""
)

# ---------------------------------------------------
# File Upload
# ---------------------------------------------------

uploaded_file = st.file_uploader(
    "📤 Upload Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🖼 Original Image")

        st.image(
            image,
            use_container_width=True
        )

    detect_button = st.button(
        "🚀 Detect Objects",
        use_container_width=True
    )

    if detect_button:

        with st.spinner("Running YOLOv8 Model..."):

            results = model(image)

            annotated_image = results[0].plot()

        with col2:

            st.subheader("✅ Detection Result")

            st.image(
                annotated_image,
                use_container_width=True
            )

        boxes = results[0].boxes

        detected_objects = []

        for box in boxes:

            cls = int(box.cls)

            conf = float(box.conf)

            label = model.names[cls]

            detected_objects.append({

                "Object": label,

                "Confidence": round(conf * 100, 2)

            })

        total_objects = len(detected_objects)

        unique_objects = len(
            set(obj["Object"] for obj in detected_objects)
        )

        highest_confidence = max(
            [obj["Confidence"] for obj in detected_objects],
            default=0
        )
                # ---------------------------------------------------
        # Dashboard Metrics
        # ---------------------------------------------------

        st.divider()

        st.subheader("📊 Detection Summary")

        metric1, metric2, metric3 = st.columns(3)

        with metric1:
            st.metric(
                label="Objects Detected",
                value=total_objects
            )

        with metric2:
            st.metric(
                label="Unique Classes",
                value=unique_objects
            )

        with metric3:
            st.metric(
                label="Highest Confidence",
                value=f"{highest_confidence:.2f}%"
            )

        # ---------------------------------------------------
        # Detection Table
        # ---------------------------------------------------

        st.divider()

        st.subheader("📋 Detected Objects")

        if detected_objects:

            df = pd.DataFrame(detected_objects)

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.warning("No objects detected.")

        # ---------------------------------------------------
        # Confidence Progress Bars
        # ---------------------------------------------------

        if detected_objects:

            st.divider()

            st.subheader("📈 Confidence Scores")

            for obj in detected_objects:

                st.write(
                    f"**{obj['Object']}**  ({obj['Confidence']}%)"
                )

                st.progress(
                    obj["Confidence"] / 100
                )

        # ---------------------------------------------------
        # Pie Chart
        # ---------------------------------------------------

        if detected_objects:

            st.divider()

            st.subheader("🥧 Object Distribution")

            pie_chart = px.pie(
                df,
                names="Object",
                title="Detected Objects"
            )

            st.plotly_chart(
                pie_chart,
                use_container_width=True
            )

        # ---------------------------------------------------
        # Bar Chart
        # ---------------------------------------------------

        if detected_objects:

            st.divider()

            counts = (
                df["Object"]
                .value_counts()
                .reset_index()
            )

            counts.columns = [
                "Object",
                "Count"
            ]

            bar_chart = px.bar(
                counts,
                x="Object",
                y="Count",
                text="Count",
                title="Number of Objects Detected"
            )

            st.plotly_chart(
                bar_chart,
                use_container_width=True
            )

        # ---------------------------------------------------
        # Detection Report
        # ---------------------------------------------------

        st.divider()

        st.subheader("📄 Detection Report")

        st.info(f"""
Model Used : YOLOv8 Nano

Total Objects : {total_objects}

Unique Classes : {unique_objects}

Highest Confidence : {highest_confidence:.2f}%

Inference Status : Successful
""")
                # ---------------------------------------------------
        # Download Detection Result
        # ---------------------------------------------------

        st.divider()

        st.subheader("⬇ Download Detection Result")

        result_image = Image.fromarray(annotated_image)

        buffer = io.BytesIO()

        result_image.save(buffer, format="PNG")

        st.download_button(
            label="📥 Download Annotated Image",
            data=buffer.getvalue(),
            file_name="yolov8_detection_result.png",
            mime="image/png",
            use_container_width=True
        )

        # ---------------------------------------------------
        # Detection Insights
        # ---------------------------------------------------

        st.divider()

        st.subheader("💡 Detection Insights")

        if total_objects == 0:

            st.warning(
                "No objects were detected. Try uploading a clearer image."
            )

        else:

            st.success(
                f"Successfully detected {total_objects} object(s) belonging to {unique_objects} unique class(es)."
            )

            most_detected = (
                df["Object"].value_counts().idxmax()
            )

            st.info(
                f"Most frequently detected object: **{most_detected}**"
            )

            avg_conf = df["Confidence"].mean()

            st.info(
                f"Average confidence score: **{avg_conf:.2f}%**"
            )

        # ---------------------------------------------------
        # Detection Tips
        # ---------------------------------------------------

        st.divider()

        st.subheader("📌 Tips")

        st.markdown("""
✅ Upload high-resolution images.

✅ Images with good lighting provide better results.

✅ Multiple objects can be detected simultaneously.

✅ YOLOv8 supports over 80 common object classes.

✅ Detection speed depends on your system configuration.
""")

        # ---------------------------------------------------
        # About YOLOv8
        # ---------------------------------------------------

        with st.expander("📖 About YOLOv8"):

            st.write("""
YOLO (You Only Look Once) is one of the fastest and most accurate
real-time object detection algorithms.

This project uses the **YOLOv8 Nano** model provided by Ultralytics.

Features:

- Real-time Object Detection
- Bounding Box Prediction
- Confidence Scores
- Multiple Object Detection
- Deep Learning using PyTorch
""")

        # ---------------------------------------------------
        # Detection Classes
        # ---------------------------------------------------

        if detected_objects:

            st.divider()

            st.subheader("🏷 Detected Classes")

            classes = sorted(df["Object"].unique())

            for cls in classes:
                st.markdown(f"- **{cls}**")

# ---------------------------------------------------
# Footer
# ---------------------------------------------------

st.divider()

st.markdown("""
<div style='text-align:center; padding:20px;'>

<h3>🎯 YOLOv8 Object Detection</h3>

Built with ❤️ using

<b>Python • YOLOv8 • PyTorch • OpenCV • Streamlit</b>

<br><br>

Developed by <b>Nayab Yaseen Khan</b>

</div>
""", unsafe_allow_html=True)