Yes bro, **full `README.md` code** — direct copy-paste pannunga. Extra ``` inside issue varama, single code block-la kudukuren.

```markdown
# AI Weather Application

An AI-powered weather assistant that provides real-time weather information and a five-day forecast for any city. It uses DeepSeek-V3 function calling with the Open-Meteo API to retrieve weather data and generate clear natural-language responses.

## Live Application

[Open AI Weather Application](https://ai-weather-application-e6evcdxetystsgcpuh7djs.streamlit.app/)

## GitHub Repository

[View Source Code](https://github.com/Jascinth-Rhema/AI-weather-Application)

## Features

- AI-powered weather assistant
- Real-time weather information
- Five-day weather forecast
- Current and feels-like temperature
- Humidity and wind speed
- Precipitation information
- Weather condition detection
- AI-generated weather summary
- Interactive Streamlit interface
- Secure API token handling

## Technologies Used

- Python
- Streamlit
- DeepSeek-V3
- Hugging Face Inference API
- Open-Meteo API
- Requests
- Python Dotenv

## How It Works

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

The user enters a city name through the Streamlit interface. DeepSeek-V3 determines when the `get_weather()` function is required. The function retrieves weather information from Open-Meteo, and the AI model generates a clear response using the retrieved data.

## Weather Information

The application provides:

- Current weather condition
- Temperature
- Feels-like temperature
- Relative humidity
- Wind speed
- Precipitation
- Five-day temperature forecast
- Daily precipitation probability

## Project Structure

    AI-weather-Application/
    │
    ├── app.py
    ├── requirements.txt
    ├── .gitignore
    ├── .env
    └── .venv/

The `app.py` file contains the main application code. The `requirements.txt` file contains the required dependencies. The `.env` file stores the Hugging Face API token and is excluded from GitHub using `.gitignore`.

## Installation

Clone the repository:

    git clone https://github.com/Jascinth-Rhema/AI-weather-Application.git
    cd AI-weather-Application

Create a virtual environment:

    python -m venv .venv

Activate the virtual environment on Windows:

    .venv\Scripts\activate

Install the required dependencies:

    pip install -r requirements.txt

## Environment Setup

Create a `.env` file in the project directory and add your Hugging Face API token:

    HF_TOKEN=your_huggingface_token

The API token should not be uploaded to GitHub or shared publicly.

## Run the Application

Start the Streamlit application using:

    streamlit run app.py

The application will open in the browser. Enter a city name to view the current weather and five-day forecast.

## Deployment

The application can be deployed using Streamlit Community Cloud.

For deployment, the Hugging Face API token is stored securely using Streamlit Secrets instead of exposing it in the source code.

    HF_TOKEN = "your_huggingface_token"

## APIs Used

### Hugging Face Inference API

The Hugging Face Inference API is used to access the DeepSeek-V3 model for natural-language understanding, function calling, and response generation.

### Open-Meteo API

The Open-Meteo API is used to retrieve city coordinates, current weather conditions, and five-day forecast data.

## Function Calling

Function calling allows the AI model to decide when an external function is required.

The weather function used in this application is:

    get_weather(city)

DeepSeek-V3 identifies when weather information is required and calls the function. The function retrieves the required data from Open-Meteo and returns it to the AI model. The model then generates a natural-language weather response.

## Security

The Hugging Face API token is stored using environment variables during local development.

    HF_TOKEN=your_huggingface_token

The `.env` file is added to `.gitignore` to prevent the token from being uploaded to GitHub. For Streamlit deployment, the token is stored securely using Streamlit Secrets.

## Future Enhancements

- Hourly weather forecast
- Weather alerts and notifications
- Location-based weather detection
- Historical weather analysis
- Multi-language support
- Weather maps
- Personalized weather recommendations

## Conclusion

The AI Weather Application demonstrates how artificial intelligence, function calling, and real-time APIs can be combined to build a practical weather assistant. It provides current weather conditions and a five-day forecast through a simple and interactive Streamlit interface.

## Author

**Jascinth Rhema R**

GitHub: https://github.com/Jascinth-Rhema
```
