from anthropic import Anthropic
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("ANTHROPIC_API_KEY")

client = Anthropic(api_key=api_key)

def generate_product_description(product_name, features):
    """Generate product description"""
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=200,
        messages=[
            {
                "role": "user",
                "content": f"""Write a compelling product description for:

Product: {product_name}
Features: {features}

Make it persuasive and professional, under 100 words."""
            }
        ]
    )
    return message.content[0].text.strip()

def generate_social_post(topic, platform):
    """Generate social media post"""
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=150,
        messages=[
            {
                "role": "user",
                "content": f"""Write a {platform} post about: {topic}

Make it engaging and appropriate for {platform}."""
            }
        ]
    )
    return message.content[0].text.strip()

# Test it
print("=== Product Description ===")
desc = generate_product_description(
    "Wireless Headphones",
    "Noise cancellation, 30-hour battery, Bluetooth 5.0"
)
print(desc)

print("\n=== Social Media Post ===")
post = generate_social_post(
    "New AI writing tool launch",
    "LinkedIn"
)
print(post)