import os
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter

def create_synthetic_ids():
    samples_dir = os.path.join("DAY4_Goal3", "samples")
    os.makedirs(samples_dir, exist_ok=True)
    
    profiles = [
        {"id": "sample_01", "quality": "clean", "name": "Rahul Sharma", "pan": "ABCDE1234F", "dob": "15/08/1995"},
        {"id": "sample_02", "quality": "clean", "name": "Priya Verma", "pan": "FGHIJ5678K", "dob": "22/11/1990"},
        {"id": "sample_03", "quality": "clean", "name": "Amit Kumar", "pan": "KLMNO9012P", "dob": "05/03/1988"},
        {"id": "sample_04", "quality": "rotated", "name": "Neha Singh", "pan": "PQRST3456W", "dob": "10/12/1992"},
        {"id": "sample_05", "quality": "rotated", "name": "Vikas Gupta", "pan": "UVWXY7890Z", "dob": "18/07/1996"},
        {"id": "sample_06", "quality": "rotated", "name": "Anjali Mehta", "pan": "ZABCD1234E", "dob": "30/01/1994"},
        {"id": "sample_07", "quality": "dark", "name": "Rohan Das", "pan": "EFGHI5678J", "dob": "12/05/1991"},
        {"id": "sample_08", "quality": "dark", "name": "Sneha Roy", "pan": "JKLMN9012O", "dob": "25/09/1989"},
        {"id": "sample_09", "quality": "blurry", "name": "Karan Malhotra", "pan": "PQRST3456V", "dob": "03/06/1993"},
        {"id": "sample_10", "quality": "blurry", "name": "Pooja Nair", "pan": "UVWXY7890A", "dob": "19/10/1995"}
    ]
    
    for p in profiles:
        # Create base image (Card size 500x320)
        img = Image.new('RGB', (500, 320), color=(245, 247, 250))
        d = ImageDraw.Draw(img)
        
        # Draw header banner
        d.rectangle([0, 0, 500, 60], fill=(20, 35, 60))
        d.text((20, 20), "INCOME TAX DEPARTMENT - PAN CARD", fill=(255, 255, 255))
        
        # Draw fields
        d.text((30, 90), f"Name: {p['name']}", fill=(20, 20, 20))
        d.text((30, 140), f"PAN Number: {p['pan']}", fill=(20, 20, 20))
        d.text((30, 190), f"DOB: {p['dob']}", fill=(20, 20, 20))
        d.text((30, 250), f"Quality Condition: {p['quality'].upper()}", fill=(100, 100, 100))
        
        # Apply quality distortions
        if p['quality'] == "rotated":
            img = img.rotate(12, expand=True, fillcolor=(245, 247, 250))
        elif p['quality'] == "dark":
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(0.3) # Very dark
        elif p['quality'] == "blurry":
            img = img.filter(ImageFilter.GaussianBlur(radius=3.5))
            
        file_path = os.path.join(samples_dir, f\"{p['id']}_{p['quality']}.jpg\")
        img.save(file_path, "JPEG")
        
    print("Generated 10 synthetic ID card images successfully with Pillow!")

if __name__ == "__main__":
    create_synthetic_ids()
