from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import cv2
from roboflow import Roboflow
import os
import requests


# Initialize SQLAlchemy without an app
db = SQLAlchemy()

# User Model


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        print("Creating tables...")
        db.create_all()
        print("Tables created.")

    CORS(app, supports_credentials=True)
    # Signup Endpoint

    @app.route('/signup', methods=['POST'])
    def signup():
        try:
            data = request.get_json()
            # Check if user already exists
            if User.query.filter_by(email=data['email']).first():
                return jsonify({'message': 'Email already in use'}), 409

            hashed_password = generate_password_hash(data['password'])
            new_user = User(
                username=data['username'], email=data['email'], password_hash=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({'message': 'Registered successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    # Login Endpoint

    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        user = User.query.filter_by(email=data['email']).first()
        if user and check_password_hash(user.password_hash, data['password']):
            session['user_id'] = user.id
            return jsonify({'message': 'Login successful'}), 200
        return jsonify({'message': 'Invalid credentials'}), 401

    # Logout Endpoint

    @app.route('/logout')
    def logout():
        session.pop('user_id', None)
        return jsonify({'message': 'You have been logged out'}), 200

    # Set the directory for saving uploads
    UPLOAD_FOLDER = 'uploads'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    # Ensure the upload directory exists
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    @app.route('/upload', methods=['POST'])
    def upload_file():
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        if file:
            filename = 'uploaded_video.mp4'
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

        try:
            # Process the video file and make external API call
            results = process_video(file_path)
            # Construct the response data
            response_data = {
                'totalBirds': results.get('Total Birds'),
                'birdTypes': list(results.get('Bird Types').keys()),
            }
            return jsonify(response_data)
        except requests.exceptions.HTTPError as e:
            # Log the error and return an appropriate message to the client
            app.logger.error(f'HTTPError: {e}')
            return jsonify({'error': 'Failed to process the video'}), 403
        except Exception as e:
            # Catch any other exceptions and log them
            app.logger.error(f'Error: {e}')
            return jsonify({'error': 'An unexpected error occurred'}), 500

    def process_video(video_path):
        try:
            # Initialize Roboflow
            rf = Roboflow(api_key="COL2OHRzFe8iNs4Nhb3s")
            project = rf.workspace().project("bird-v2")
            model = project.version(2).model

            cap = cv2.VideoCapture(video_path)

            birds = []
            frame_count = 0
            cooldown = 60

            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                frame_count += 1
                image_path = "temp_frame.jpg"
                cv2.imwrite(image_path, frame)

                try:
                    response = model.predict(
                        image_path, confidence=40, overlap=30).json()
                    predictions = response['predictions']

                    for prediction in predictions:
                        predicted_class = prediction['class']
                        birds.append(predicted_class)

                    if predictions:
                        frame_count += cooldown

                    if frame_count > 1000:
                        break
                except requests.exceptions.RequestException as e:
                    app.logger.error(
                        f'RequestException during model prediction: {e}')
                    break

            cap.release()

            counts = dict()
            for bird in birds:
                counts[bird] = counts.get(bird, 0) + 1

            totalBirds = len(birds)
            return {"Total Birds": totalBirds, "Bird Types": counts}
        except Exception as e:
            app.logger.error(f'Error in process_video: {e}')
            raise

    return app


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
