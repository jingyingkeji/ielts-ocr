import os
import uuid

from PIL import Image, ImageDraw, ImageFont
from fastapi import HTTPException

os.makedirs("uploads/new", exist_ok=True)


async def process_annotation(file, annotations):
    try:

        """data schema
        {
            "words": [
                {
                    "old": "view",
                    "new": "views",
                    "location": [[164,16], [816,16], [816,48], [164,48]]
                },
                {
                    "old": "item",
                    "new": "items",
                    "location": [[63, 67],[857, 61],[858, 92],[63, 98]]
                }
            ],
            "sentences": [
                {
                    "old": "shopping of .....",
                    "new": "The growing popularity of shopping...",
                    "location": [[54,186],[847,183],[847,213],[54,216]]
                }
            ]
        }
        """

        # Save uploaded file
        file_location = f"uploads/new/{uuid.uuid4()}.png"
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())

        # Open image
        image = Image.open(file_location)
        draw = ImageDraw.Draw(image)

        # Set font and size
        font_path = "static/fonts/Sriracha.ttf"  # Adjust path as necessary
        font_size = 16
        font = ImageFont.truetype(font_path, font_size)

        # Get image dimensions
        width, height = image.size

        # 在图片上画矩形框并标注文字
        for key, word in enumerate(annotations['words']):
            old_text = word['old']
            new_text = word['new']
            location = word['location']

            draw_text = str((key + 1)) + ". " + new_text

            rectangle_height = (location[3][1] - location[0][1])
            font_diff = (rectangle_height / font_size)
            text_location = (location[0][0], location[2][1] - font_diff)

            # 计算位置
            top_left = (location[0][0], location[0][1])
            bottom_right = (location[2][0], location[2][1])

            draw.rectangle([top_left, bottom_right], outline='blue', width=2)
            draw.text(text_location, draw_text, font=font, fill='blue')

        for key, sentence in enumerate(annotations['sentences']):
            old_text = sentence['old']
            new_text = sentence['new']
            location = sentence['location']

            draw_text = str((key + 1)) + ". " + new_text

            rectangle_height = (location[3][1] - location[0][1])
            font_diff = (rectangle_height / font_size)
            text_location = (location[0][0], location[2][1] - font_diff)

            # 计算位置
            top_left = (location[0][0], location[0][1])
            bottom_right = (location[2][0], location[2][1])

            draw.rectangle([top_left, bottom_right], outline='red', width=2)
            draw.text(text_location, draw_text, font=font, fill='red')

        # Save annotated image
        annotated_image_name = f"{uuid.uuid4()}.jpg"
        annotated_image_path = f"uploads/new/{annotated_image_name}"
        image = image.convert("RGB")
        image.save(annotated_image_path)

        # Remove temporary file
        os.remove(file_location)

        # return FileResponse(annotated_image_path, media_type="image/jpeg")
        # Return the URL to access the image
        return {"url": f"/uploads/new/{annotated_image_name}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
