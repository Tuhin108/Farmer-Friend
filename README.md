# 🌾 Farm Assistant - AI-Powered Agricultural Recommendations

<div align="center">

![Farm Assistant Banner](https://img.shields.io/badge/Farm-Assistant-green?style=for-the-badge&logo=leaf&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.7+-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0+-red?style=for-the-badge&logo=flask&logoColor=white)
![Mistral AI](https://img.shields.io/badge/Mistral-AI-orange?style=for-the-badge&logo=ai&logoColor=white)

*Empowering farmers with intelligent crop and fertilizer recommendations using cutting-edge AI technology*

</div>

## 🚀 Overview

Farm Assistant is a modern web application that leverages the power of **Mistral AI** to provide intelligent agricultural recommendations. Whether you're a seasoned farmer or just starting your agricultural journey, this tool helps you make data-driven decisions for optimal crop yields and sustainable farming practices.

### ✨ Key Features

- 🌱 **Smart Crop Recommendations** - Get AI-powered suggestions based on soil conditions, climate, and location
- 🧪 **Fertilizer Optimization** - Receive precise fertilizer recommendations for maximum crop health
- 🎨 **Beautiful UI** - Rustic, farm-themed interface with smooth animations
- ⚡ **Real-time Processing** - Instant recommendations powered by Mistral AI
- 📱 **Responsive Design** - Works seamlessly on desktop and mobile devices

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Flask (Python) |
| **AI Engine** | Mistral AI API |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Styling** | Custom CSS with farm-themed design |
| **API Integration** | Mistral AI Large Language Model |

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)
- A Mistral AI API key ([Get one here](https://mistral.ai/))

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/farm-assistant.git
cd farm-assistant
```

### 2. Install Dependencies

```bash
pip install flask mistralai
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
MISTRAL_API_KEY=your_mistral_api_key_here
```

Or export the environment variable:

```bash
export MISTRAL_API_KEY="your_mistral_api_key_here"
```

### 4. Run the Application

```bash
python app.py
```

Visit `http://localhost:5000` in your browser and start getting AI-powered farm recommendations! 🎉

## 🏗️ Project Structure

```
farm-assistant/
├── app.py                 # Main Flask application
├── templates/
│   ├── index.html        # Home page with navigation
│   ├── crop.html         # Crop recommendation form
│   ├── fertilizer.html   # Fertilizer recommendation form
│   └── result.html       # Results display page
├── static/               # Static assets (if any)
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🌾 How It Works

### Crop Recommendations

1. **Input Parameters**: Location, soil nutrients (N-P-K), temperature, humidity, pH, rainfall
2. **AI Processing**: Mistral AI analyzes the conditions using agricultural knowledge
3. **Smart Output**: Receive tailored crop suggestions for maximum profitability

### Fertilizer Recommendations

1. **Input Parameters**: Environmental conditions, soil type, crop type, current nutrient levels
2. **AI Analysis**: Advanced algorithms determine optimal fertilizer composition
3. **Precise Results**: Get specific fertilizer recommendations for crop health

## 📊 API Integration

The application uses the **Mistral AI Large Language Model** to process agricultural data:

```python
def get_mistral_response(prompt):
    try:
        chat_response = client.chat.complete(
            model="mistral-large-latest",
            messages=[{"role": "user", "content": prompt}]
        )
        return chat_response.choices[0].message.content
    except Exception as e:
        return f"Error retrieving recommendation: {e}"
```

## 🎨 Design Philosophy

The application features a **rustic farm aesthetic** with:

- **Warm Color Palette**: Earth tones and golden accents
- **Typography**: "Rye" font for that authentic farm feel
- **Interactive Elements**: Smooth hover effects and transitions
- **Responsive Layout**: Optimized for all screen sizes

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `MISTRAL_API_KEY` | Your Mistral AI API key | Yes |

### Model Configuration

The application uses `mistral-large-latest` model by default. You can modify this in `app.py`:

```python
model = "mistral-large-latest"  # Change as needed
```

## 🚀 Deployment

### Local Development

```bash
python app.py
```

### Production Deployment

For production, consider using:

- **Gunicorn**: `gunicorn -w 4 app:app`
- **Docker**: Create a Dockerfile for containerization
- **Cloud Platforms**: Deploy on Heroku, AWS, or Google Cloud

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/amazing-feature`)
3. 💾 Commit your changes (`git commit -m 'Add amazing feature'`)
4. 📤 Push to the branch (`git push origin feature/amazing-feature`)
5. 🔀 Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Mistral AI** for providing powerful language models
- **Flask** team for the excellent web framework
- The agricultural community for inspiring this project


<div align="center">

**Made with ❤️ for farmers everywhere**

*Cultivating the future of agriculture, one recommendation at a time* 🌱

</div>
