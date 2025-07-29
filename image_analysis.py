from dotenv import load_dotenv
import os
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
import uuid

def analyze_image(image_file, annotated_folder):
    """
    Analyzes an image file and returns the results in a dictionary.
    """
    try:
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')

        cv_client = ImageAnalysisClient(
            endpoint=ai_endpoint,
            credential=AzureKeyCredential(ai_key)
        )

        with open(image_file, "rb") as f:
            image_data = f.read()

        result = cv_client.analyze(
            image_data=image_data,
            visual_features=[
                VisualFeatures.CAPTION,
                VisualFeatures.DENSE_CAPTIONS,
                VisualFeatures.TAGS,
                VisualFeatures.OBJECTS,
                VisualFeatures.PEOPLE
            ],
        )

        analysis_results = {
            'caption': result.caption if result.caption else None,
            'dense_captions': result.dense_captions if result.dense_captions else None,
            'tags': result.tags if result.tags else None,
            'objects_image': show_objects(image_file, result.objects.list, annotated_folder) if result.objects else None,
            'people_image': show_people(image_file, result.people.list, annotated_folder) if result.people else None
        }
            
        return analysis_results

    except Exception as ex:
        print(ex)
        return {"error": str(ex)}


def show_objects(image_filename, detected_objects, annotated_folder):
    image = Image.open(image_filename)
    fig = plt.figure(figsize=(image.width/100, image.height/100))
    plt.axis('off')
    draw = ImageDraw.Draw(image)
    color = 'cyan'

    for detected_object in detected_objects:
        r = detected_object.bounding_box
        bounding_box = ((r.x, r.y), (r.x + r.width, r.y + r.height))
        draw.rectangle(bounding_box, outline=color, width=3)
        plt.annotate(detected_object.tags[0].name, (r.x, r.y), backgroundcolor=color)

    plt.imshow(image)
    plt.tight_layout(pad=0)
    
    objectfile = f"objects_{uuid.uuid4()}.jpg"
    filepath = os.path.join(annotated_folder, objectfile)
    fig.savefig(filepath)
    plt.close(fig)
    return objectfile


def show_people(image_filename, detected_people, annotated_folder):
    image = Image.open(image_filename)
    fig = plt.figure(figsize=(image.width/100, image.height/100))
    plt.axis('off')
    draw = ImageDraw.Draw(image)
    color = 'cyan'

    for detected_person in detected_people:
        if detected_person.confidence > 0.2:
            r = detected_person.bounding_box
            bounding_box = ((r.x, r.y), (r.x + r.width, r.y + r.height))
            draw.rectangle(bounding_box, outline=color, width=3)

    plt.imshow(image)
    plt.tight_layout(pad=0)

    peoplefile = f"people_{uuid.uuid4()}.jpg"
    filepath = os.path.join(annotated_folder, peoplefile)
    fig.savefig(filepath)
    plt.close(fig)
    return peoplefile