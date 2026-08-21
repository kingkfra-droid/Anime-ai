import openai
import flask
import os
from flask import request, jsonify
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = flask.Flask(__name__)

# Configure OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")


# Route to create anime characters
@app.route("/create-character", methods=["POST"])
def create_character():
    """Generate an anime character based on user description."""
    data = request.json
    description = data.get("description", "")
    
    if not description:
        return jsonify({"error": "Description is required"}), 400
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert anime character designer. Create detailed anime character descriptions with personality, appearance, and backstory."
                },
                {
                    "role": "user",
                    "content": f"Create an anime character based on: {description}"
                }
            ],
            temperature=0.7,
            max_tokens=1000
        )
        
        character_data = response.choices[0].message["content"]
        return jsonify({"character": character_data}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route to generate manga panels
@app.route("/generate-panel", methods=["POST"])
def generate_panel():
    """Generate manga panel descriptions and dialogue."""
    data = request.json
    scene_description = data.get("scene", "")
    
    if not scene_description:
        return jsonify({"error": "Scene description is required"}), 400
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "You are a manga panel writer. Create vivid panel descriptions, dialogue, and action sequences."
                },
                {
                    "role": "user",
                    "content": f"Design a manga panel for this scene: {scene_description}"
                }
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        panel_data = response.choices[0].message["content"]
        return jsonify({"panel": panel_data}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route to write stories
@app.route("/write-story", methods=["POST"])
def write_story():
    """Generate anime/manga stories."""
    data = request.json
    prompt = data.get("prompt", "")
    
    if not prompt:
        return jsonify({"error": "Story prompt is required"}), 400
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional anime/manga writer. Create engaging, original stories with rich dialogue and character development."
                },
                {
                    "role": "user",
                    "content": f"Write an anime story based on: {prompt}"
                }
            ],
            temperature=0.8,
            max_tokens=2000
        )
        
        story_data = response.choices[0].message["content"]
        return jsonify({"story": story_data}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route to build worlds
@app.route("/create-world", methods=["POST"])
def create_world():
    """Design anime/manga worlds and settings."""
    data = request.json
    world_concept = data.get("concept", "")
    
    if not world_concept:
        return jsonify({"error": "World concept is required"}), 400
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "You are a world-builder for anime and manga. Create detailed, immersive world settings with geography, culture, magic systems, and lore."
                },
                {
                    "role": "user",
                    "content": f"Build an anime world based on: {world_concept}"
                }
            ],
            temperature=0.75,
            max_tokens=1500
        )
        
        world_data = response.choices[0].message["content"]
        return jsonify({"world": world_data}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Health check endpoint
@app.route("/health", methods=["GET"])
def health():
    """Check API status."""
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
