import os
import uuid
from PIL import Image, ImageDraw, ImageFont
from fastapi.responses import FileResponse
from fastapi import HTTPException

async def process_annotation(file, annotations):
    try:
        # Save uploaded file
        file_location = f"temp/{uuid.uuid4()}.png"
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())

        # Open image
        image = Image.open(file_location)
        draw = ImageDraw.Draw(image)

        # Set font and size
        font_path = "static/fonts/Sriracha.ttf"  # Adjust path as necessary
        font = ImageFont.truetype(font_path, 12)

        # Get image dimensions
        width, height = image.size

        # Draw rectangles and annotate text
        for text, (x, y, w, h) in annotations['words']:
            top_left = (x * width, y * height)
            bottom_right = ((x + w) * width, (y + h) * height)
            draw.rectangle([top_left, bottom_right], outline='blue', width=2)
            draw.text((x * width, y * height), text, font=font, fill='red')

        for text, (x, y, w, h) in annotations['sentences']:
            top_left = (x * width, y * height)
            bottom_right = ((x + w) * width, (y + h) * height)
            draw.rectangle([top_left, bottom_right], outline='red', width=2)
            draw.text((x * width, y * height), text, font=font, fill='red')

        # Save annotated image
        annotated_image_path = f"temp/{uuid.uuid4()}.jpg"
        image = image.convert("RGB")
        image.save(annotated_image_path)

        # Remove temporary file
        os.remove(file_location)

        return FileResponse(annotated_image_path, media_type="image/jpeg")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
