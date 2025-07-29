# Image-Analysis-with-Azure-AI-Vision

## Description
The Image Analysis Web App is an interactive application powered by Azure AI Vision. It allows users to upload an image and receive a detailed analysis, including automated captions, content tags, and the detection of objects and people within the image.
Built with a Flask backend, this project demonstrates a practical use case for cloud-based computer vision. The application not only returns textual data but also visualizes the results by drawing bounding boxes around detected objects and people, saving them as new images. This serves as an excellent starter project for anyone interested in integrating advanced image analysis into web applications.

---

##  Features
-  **Caption Generation**: Creates a concise, human-readable description of the image content.
-  **Dense Captioning**: Provides more granular descriptions for different regions within the image.
-  **Content Tagging**: Generates a list of relevant tags based on the image's subjects, actions, and setting.
-  **Object Detection**: Identifies common objects and draws bounding boxes around them in a separate image.
-  **People Detection**: Locates people in the image and highlights them with bounding boxes.

---

##  Tech Stack
- Python 3.x
- Flask: For the web server and user interface.
- Azure AI Vision SDK: The azure-ai-vision-imageanalysis==1.0.0 package for communicating with the Azure service.
- Pillow: For image manipulation.
- Matplotlib: Used to draw bounding boxes and annotate the images.
- Python-Dotenv: For managing environment variables. 


---

##  Project Structure
```
├── app.py                  # Main Flask application file
├── image_analysis.py       # Module for Azure AI Vision analysis logic
├── requirements.txt        # Project dependencies
├── .env                    # Environment variables for Azure keys
├── README.md
├── LICENSE
├── static/
│   ├── uploads/            # Stores user-uploaded images
│   └── annotated/          # Stores images with detected objects/people
└── templates/
    ├── index.html          # The main page with the file upload form
    └── results.html        # The page to display analysis results

```

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/JoshuaFerando/Image-Analysis-with-Azure-AI-Vision
cd Image-Analysis-with-Azure-AI-Vision
```

### 2. Install Dependencies
Using **pip**:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Azure AI Vision Setup
1. Create an **AI Vision** resource in the Azure portal.
2. Once deployed, navigate to the Keys and Endpoint section of your resource.
3. You will need the following credentials:
   - **API Endpoint**
   - **API Key**
  
4. Add these to your environment variables:
   ```bash
   AI_SERVICE_ENDPOINT="YOUR_AZURE_VISION_ENDPOINT"
   AI_SERVICE_KEY="YOUR_AZURE_VISION_KEY"
   ```

---

## Running the Web App
```bash
python app.py
```
Then open your browser and navigate to:
```
http://localhost:5000
```

---

## Deployment
You can deploy this project to:
- **Azure App Service**
- **Replit**
- **Heroku**
- **Any cloud hosting that supports Flask**

---

## License
This project is licensed under the **Apache-2.0 license**.

---

### 👨‍💻 Author
Developed by **Joshua Fernando**  
Feel free to contribute or open issues!
