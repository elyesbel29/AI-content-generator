from anthropic import Anthropic
from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("ANTHROPIC_API_KEY")

client = Anthropic(api_key=api_key)
app = Flask(__name__)

def generate_content(content_type, input_text):
    """Generate content based on type"""
    
    prompts = {
        "product_description": f"Write a compelling product description for: {input_text}\nMake it persuasive and professional, under 100 words.",
        "social_post": f"Write an engaging social media post about: {input_text}\nKeep it concise and catchy.",
        "ad_copy": f"Write advertising copy for: {input_text}\nMake it persuasive and action-oriented.",
        "blog_outline": f"Create a blog outline for: {input_text}\nInclude main sections and key points."
    }
    
    prompt = prompts.get(content_type, input_text)
    
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=300,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return message.content[0].text.strip()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    content_type = data.get('type', '')
    text = data.get('text', '')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    result = generate_content(content_type, text)
    return jsonify({'content': result})

if __name__ == '__main__':
    app.run(debug=True)