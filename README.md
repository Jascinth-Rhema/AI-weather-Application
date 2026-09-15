# AI Weather Application

An AI-powered weather application that uses function calling to provide real-time weather information and a five-day forecast for any city.

The application combines a Large Language Model with the Open-Meteo weather API. The AI understands the user's city input, calls the weather function, retrieves the required weather data, and generates a natural-language response.

## Features

- AI-powered weather assistant
- Function calling using DeepSeek-V3
- Real-time weather information
- Five-day weather forecast
- Temperature and feels-like temperature
- Humidity information
- Wind speed
- Precipitation details
- Weather condition detection
- City and country identification
- AI-generated weather summary
- Interactive Streamlit interface
- Secure Hugging Face API token handling

## Technologies Used

- Python
- Streamlit
- Hugging Face Inference API
- DeepSeek-V3
- Open-Meteo API
- Requests
- python-dotenv

## How It Works

The application follows a function-calling workflow:

```text
User
  |
  v
Streamlit Interface
  |
  v
DeepSeek-V3
  |
  v
Function Call: get_weather(city)
  |
  v
Open-Meteo Geocoding API
  |
  v
Open-Meteo Weather API
  |
  v
Weather Data
  |
  v
DeepSeek-V3
  |
  v
AI Weather Response
