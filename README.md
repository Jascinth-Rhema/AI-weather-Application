# AI Weather Application

An AI-powered weather assistant that provides real-time weather information and a five-day forecast for any city. The application combines artificial intelligence with real-time weather APIs to understand user requests, retrieve relevant weather data, and generate clear natural-language responses.

## Introduction

The AI Weather Application is designed to make weather information simple, accessible, and interactive. Instead of manually searching through weather websites, users can enter the name of a city and receive its current weather conditions along with a five-day forecast.

The application uses DeepSeek-V3 with function calling to understand the user's request and determine when weather data needs to be retrieved. The `get_weather()` function connects with the Open-Meteo API to obtain real-time weather information such as temperature, feels-like temperature, humidity, wind speed, precipitation, and weather conditions. The retrieved data is then processed by the AI model to generate an easy-to-understand weather summary.

The application is developed using Python and Streamlit, providing a clean and interactive interface for users.

## Live Application

[Open AI Weather Application](PASTE_YOUR_STREAMLIT_APP_LINK_HERE)

## GitHub Repository

[View Source Code](https://github.com/Jascinth-Rhema/AI-weather-Application)

## Features

- AI-powered weather assistant
- Function calling with DeepSeek-V3
- Real-time weather information
- Five-day weather forecast
- Current temperature
- Feels-like temperature
- Humidity information
- Wind speed
- Precipitation details
- Weather condition detection
- AI-generated weather summary
- City and country identification
- Interactive Streamlit interface
- Secure API token handling

## Technologies Used

- Python
- Streamlit
- Hugging Face Inference API
- DeepSeek-V3
- Open-Meteo API
- Requests
- Python Dotenv

## How It Works

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
Function Calling
  |
  v
get_weather(city)
  |
  v
Open-Meteo API
  |
  v
Weather Data
  |
  v
DeepSeek-V3
  |
  v
AI Weather Response


## Conclusion

The AI Weather Application demonstrates how artificial intelligence, function calling, and real-time APIs can be combined to build a practical and user-friendly application. DeepSeek-V3 handles the user's natural-language request and determines when the weather function should be used, while the Open-Meteo API provides the required real-time weather data.

The integration of Python and Streamlit makes the application simple to use and easy to deploy. Overall, the project provides an effective example of how AI can be connected with external APIs to deliver useful real-world information through an interactive application.

By
JASCINTH RHEMA.R
