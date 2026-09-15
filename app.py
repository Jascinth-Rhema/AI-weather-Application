import streamlit as st
import requests
import os
import json

from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import streamlit.components.v1 as components


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Weather Assistant",
    page_icon="🌤️",
    layout="wide"
)


# =========================================================
# LOAD ENVIRONMENT VARIABLES
# =========================================================

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    st.error(
        "HF_TOKEN not found. Please check your .env file."
    )
    st.stop()


# =========================================================
# HUGGING FACE CLIENT
# =========================================================

client = InferenceClient(
    api_key=HF_TOKEN,
    provider="auto"
)

MODEL = "deepseek-ai/DeepSeek-V3-0324"


# =========================================================
# PAGE STYLE
# =========================================================

st.markdown(
    """
    <style>

    .stApp {
        background: linear-gradient(
            180deg,
            #eaf7ff 0%,
            #f5fbff 45%,
            #ffffff 100%
        );
    }

    .main {
        padding-top: 1rem;
    }

    h1 {
        color: #173f5f;
        text-align: center;
        font-size: 42px !important;
        font-weight: 700 !important;
        margin-bottom: 5px;
    }

    h2, h3 {
        color: #214e6b;
    }

    .stTextInput input {
        border-radius: 12px;
        border: 1px solid #b9d9ed;
        padding: 12px;
        font-size: 16px;
    }

    .stButton button {
        width: 100%;
        border-radius: 12px;
        border: none;
        padding: 12px;
        font-size: 16px;
        font-weight: 600;
        background: #4aa3df;
        color: white;
    }

    .stButton button:hover {
        background: #328ac4;
    }

    [data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.85);
        border: 1px solid #d6e9f5;
        border-radius: 14px;
        padding: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# TITLE
# =========================================================

st.title("🌤️ AI Weather Assistant")

st.markdown(
    "<p style='text-align:center; color:#5d7285; "
    "font-size:18px;'>"
    "Ask about the weather in any city and get an "
    "AI-powered answer."
    "</p>",
    unsafe_allow_html=True
)


# =========================================================
# ANIMATED SKY
# =========================================================

components.html(
    """
    <!DOCTYPE html>

    <html>

    <head>

    <style>

    body {
        margin: 0;
        padding: 0;
        overflow: hidden;
        background: transparent;
    }

    .sky {
        position: relative;
        width: 100%;
        height: 160px;
    }

    .sun {
        position: absolute;
        left: 45%;
        top: 25px;
        font-size: 60px;
        animation: floatSun 3s ease-in-out infinite;
    }

    .cloud {
        position: absolute;
        left: 25%;
        top: 80px;
        font-size: 48px;
        animation: moveCloud 6s ease-in-out infinite;
    }

    .cloud-small {
        position: absolute;
        right: 25%;
        top: 40px;
        font-size: 34px;
        animation: moveSmallCloud 5s ease-in-out infinite;
    }

    .sparkle {
        position: absolute;
        font-size: 24px;
        animation: sparkleAnimation 2s ease-in-out infinite;
    }

    .sparkle-one {
        left: 32%;
        top: 30px;
    }

    .sparkle-two {
        right: 32%;
        top: 90px;
        animation-delay: 0.8s;
    }

    @keyframes floatSun {

        0%, 100% {
            transform: translateY(0) rotate(0deg);
        }

        50% {
            transform: translateY(-10px) rotate(8deg);
        }

    }

    @keyframes moveCloud {

        0%, 100% {
            transform: translateX(0);
        }

        50% {
            transform: translateX(25px);
        }

    }

    @keyframes moveSmallCloud {

        0%, 100% {
            transform: translateX(0);
        }

        50% {
            transform: translateX(-20px);
        }

    }

    @keyframes sparkleAnimation {

        0%, 100% {
            opacity: 0.3;
            transform: scale(0.8);
        }

        50% {
            opacity: 1;
            transform: scale(1.3);
        }

    }

    </style>

    </head>

    <body>

        <div class="sky">

            <div class="sparkle sparkle-one">
                ✦
            </div>

            <div class="sun">
                ☀️
            </div>

            <div class="cloud">
                ☁️
            </div>

            <div class="cloud-small">
                ☁️
            </div>

            <div class="sparkle sparkle-two">
                ✧
            </div>

        </div>

    </body>

    </html>
    """,
    height=160,
    scrolling=False
)


# =========================================================
# WEATHER FUNCTION
# =========================================================

def get_weather(city):

    try:

        # -------------------------------------------------
        # GEOCODING API
        # -------------------------------------------------

        geocoding_url = (
            "https://geocoding-api.open-meteo.com/v1/search"
        )

        geocoding_params = {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }

        geo_response = requests.get(
            geocoding_url,
            params=geocoding_params,
            timeout=10
        )

        geo_response.raise_for_status()

        geo_data = geo_response.json()

        if not geo_data.get("results"):

            return {
                "error": f"City '{city}' was not found."
            }


        # -------------------------------------------------
        # LOCATION INFORMATION
        # -------------------------------------------------

        location = geo_data["results"][0]

        latitude = location["latitude"]
        longitude = location["longitude"]

        city_name = location.get(
            "name",
            city
        )

        country = location.get(
            "country",
            ""
        )


        # -------------------------------------------------
        # OPEN-METEO WEATHER API
        # -------------------------------------------------

        weather_url = (
            "https://api.open-meteo.com/v1/forecast"
        )

        weather_params = {

            "latitude": latitude,

            "longitude": longitude,

            "current": ",".join([
                "temperature_2m",
                "relative_humidity_2m",
                "apparent_temperature",
                "precipitation",
                "weather_code",
                "wind_speed_10m"
            ]),

            "daily": ",".join([
                "weather_code",
                "temperature_2m_max",
                "temperature_2m_min",
                "precipitation_probability_max"
            ]),

            "forecast_days": 6,

            "timezone": "auto"
        }


        weather_response = requests.get(
            weather_url,
            params=weather_params,
            timeout=10
        )

        weather_response.raise_for_status()

        weather_data = weather_response.json()


        # -------------------------------------------------
        # CURRENT WEATHER
        # -------------------------------------------------

        current = weather_data.get(
            "current",
            {}
        )


        # -------------------------------------------------
        # DAILY FORECAST
        # -------------------------------------------------

        daily = weather_data.get(
            "daily",
            {}
        )

        dates = daily.get(
            "time",
            []
        )

        weather_codes = daily.get(
            "weather_code",
            []
        )

        max_temperatures = daily.get(
            "temperature_2m_max",
            []
        )

        min_temperatures = daily.get(
            "temperature_2m_min",
            []
        )

        rain_probability = daily.get(
            "precipitation_probability_max",
            []
        )


        # -------------------------------------------------
        # CREATE FORECAST
        # -------------------------------------------------

        forecast = []

        for i in range(
            1,
            min(6, len(dates))
        ):

            forecast.append({

                "date": dates[i],

                "weather_code":
                    weather_codes[i],

                "max_temperature":
                    max_temperatures[i],

                "min_temperature":
                    min_temperatures[i],

                "rain_probability":
                    rain_probability[i]
            })


        # -------------------------------------------------
        # RETURN WEATHER DATA
        # -------------------------------------------------

        return {

            "city": city_name,

            "country": country,

            "temperature":
                current.get("temperature_2m"),

            "feels_like":
                current.get("apparent_temperature"),

            "humidity":
                current.get("relative_humidity_2m"),

            "precipitation":
                current.get("precipitation"),

            "wind_speed":
                current.get("wind_speed_10m"),

            "weather_code":
                current.get("weather_code"),

            "time":
                current.get("time"),

            "forecast":
                forecast
        }


    except requests.RequestException as e:

        return {
            "error": f"Weather service error: {str(e)}"
        }

    except Exception as e:

        return {
            "error": f"Something went wrong: {str(e)}"
        }


# =========================================================
# WEATHER CODE INFORMATION
# =========================================================

def get_weather_info(weather_code):

    weather_info = {

        0: ("Clear Sky", "☀️"),

        1: ("Mainly Clear", "🌤️"),

        2: ("Partly Cloudy", "⛅"),

        3: ("Overcast", "☁️"),

        45: ("Foggy", "🌫️"),

        48: ("Depositing Rime Fog", "🌫️"),

        51: ("Light Drizzle", "🌦️"),

        53: ("Moderate Drizzle", "🌦️"),

        55: ("Dense Drizzle", "🌧️"),

        61: ("Slight Rain", "🌦️"),

        63: ("Moderate Rain", "🌧️"),

        65: ("Heavy Rain", "🌧️"),

        71: ("Slight Snow", "🌨️"),

        73: ("Moderate Snow", "🌨️"),

        75: ("Heavy Snow", "❄️"),

        80: ("Slight Rain Showers", "🌦️"),

        81: ("Moderate Rain Showers", "🌧️"),

        82: ("Violent Rain Showers", "⛈️"),

        95: ("Thunderstorm", "⛈️"),

        96: (
            "Thunderstorm with Slight Hail",
            "⛈️"
        ),

        99: (
            "Thunderstorm with Heavy Hail",
            "⛈️"
        )
    }

    return weather_info.get(
        weather_code,
        ("Unknown Weather", "🌍")
    )


# =========================================================
# FUNCTION CALLING TOOL
# =========================================================

tools = [

    {
        "type": "function",

        "function": {

            "name": "get_weather",

            "description": (
                "Get current weather and five day "
                "weather forecast for a city."
            ),

            "parameters": {

                "type": "object",

                "properties": {

                    "city": {

                        "type": "string",

                        "description":
                            "Name of the city."
                    }
                },

                "required": [
                    "city"
                ]
            }
        }
    }
]


# =========================================================
# AI WEATHER RESPONSE
# =========================================================

def ask_ai(user_question):

    messages = [

        {
            "role": "system",

            "content": (
                "You are an AI weather assistant. "
                "Help users understand weather information "
                "clearly and naturally. "
                "Use the get_weather tool whenever the "
                "user asks about weather in a city."
            )
        },

        {
            "role": "user",

            "content": user_question
        }
    ]


    # -----------------------------------------------------
    # FIRST AI CALL
    # -----------------------------------------------------

    response = client.chat_completion(

        model=MODEL,

        messages=messages,

        tools=tools,

        tool_choice="auto",

        max_tokens=500
    )


    response_message = response.choices[0].message


    # -----------------------------------------------------
    # CHECK FOR TOOL CALL
    # -----------------------------------------------------

    if not response_message.tool_calls:

        return {
            "answer": response_message.content,
            "weather": None
        }


    # -----------------------------------------------------
    # SAVE AI TOOL REQUEST
    # -----------------------------------------------------

    messages.append(response_message)


    weather_result = None


    # -----------------------------------------------------
    # EXECUTE TOOL
    # -----------------------------------------------------

    for tool_call in response_message.tool_calls:

        function_name = tool_call.function.name

        arguments = json.loads(
            tool_call.function.arguments
        )


        if function_name == "get_weather":

            weather_result = get_weather(
                arguments["city"]
            )


            # ---------------------------------------------
            # SEND TOOL RESULT BACK TO AI
            # ---------------------------------------------

            messages.append({

                "role": "tool",

                "tool_call_id":
                    tool_call.id,

                "name":
                    function_name,

                "content":
                    json.dumps(weather_result)
            })


    # -----------------------------------------------------
    # SECOND AI CALL
    # -----------------------------------------------------

    final_response = client.chat_completion(

        model=MODEL,

        messages=messages,

        max_tokens=700
    )


    final_answer = (
        final_response
        .choices[0]
        .message
        .content
    )


    return {

        "answer": final_answer,

        "weather": weather_result
    }


# =========================================================
# SEARCH SECTION
# =========================================================

st.divider()

st.subheader("Check the Weather")

city = st.text_input(
    "Enter a city name",
    placeholder="Example: Chennai, Coimbatore, Delhi"
)

search = st.button(
    "Get Weather"
)


# =========================================================
# SEARCH ACTION
# =========================================================

if search:

    if not city.strip():

        st.warning(
            "Please enter a city name."
        )

    else:

        user_question = (
            f"What is the current weather and "
            f"five day forecast in {city.strip()}?"
        )


        with st.spinner(
            "Getting weather information..."
        ):

            try:

                result = ask_ai(
                    user_question
                )

            except Exception as e:

                st.error(
                    f"AI Error: {str(e)}"
                )

                st.stop()


        weather = result.get(
            "weather"
        )


        # =================================================
        # WEATHER RESULT
        # =================================================

        if weather:

            if "error" in weather:

                st.error(
                    weather["error"]
                )

            else:

                weather_code = weather[
                    "weather_code"
                ]

                condition, emoji = (
                    get_weather_info(
                        weather_code
                    )
                )


                # -----------------------------------------
                # LOCATION
                # -----------------------------------------

                st.divider()

                st.header(
                    f"{weather['city']}, "
                    f"{weather['country']}"
                )

                st.caption(
                    f"Updated: {weather['time']}"
                )


                # -----------------------------------------
                # MAIN WEATHER
                # -----------------------------------------

                main_col1, main_col2 = st.columns(
                    [1, 2]
                )


                with main_col1:

                    st.markdown(
                        f"# {emoji}"
                    )

                    st.subheader(
                        condition
                    )


                with main_col2:

                    temperature = weather[
                        "temperature"
                    ]

                    feels_like = weather[
                        "feels_like"
                    ]

                    st.metric(
                        "Temperature",
                        f"{temperature} °C"
                    )

                    st.write(
                        f"Feels like **{feels_like} °C**"
                    )


                # -----------------------------------------
                # WEATHER DETAILS
                # -----------------------------------------

                st.subheader(
                    "Weather Details"
                )

                detail1, detail2, detail3 = (
                    st.columns(3)
                )


                with detail1:

                    st.metric(
                        "Humidity",
                        f"{weather['humidity']}%"
                    )


                with detail2:

                    st.metric(
                        "Wind Speed",
                        f"{weather['wind_speed']} km/h"
                    )


                with detail3:

                    st.metric(
                        "Precipitation",
                        f"{weather['precipitation']} mm"
                    )


                # -----------------------------------------
                # AI RESPONSE
                # -----------------------------------------

                st.subheader(
                    "AI Weather Summary"
                )

                st.info(
                    result["answer"]
                )


                # -----------------------------------------
                # FIVE DAY FORECAST
                # -----------------------------------------

                st.subheader(
                    "5-Day Forecast"
                )

                forecast = weather.get(
                    "forecast",
                    []
                )


                if forecast:

                    forecast_columns = st.columns(
                        len(forecast)
                    )


                    for i, day in enumerate(
                        forecast
                    ):

                        day_condition, day_emoji = (
                            get_weather_info(
                                day["weather_code"]
                            )
                        )


                        with forecast_columns[i]:

                            with st.container(
                                border=True
                            ):

                                st.caption(
                                    day["date"]
                                )

                                st.markdown(
                                    f"### {day_emoji}"
                                )

                                st.write(
                                    day_condition
                                )

                                st.metric(
                                    "High",
                                    f"{day['max_temperature']} °C"
                                )

                                st.metric(
                                    "Low",
                                    f"{day['min_temperature']} °C"
                                )

                                st.caption(
                                    "Rain chance: "
                                    f"{day['rain_probability']}%"
                                )

                else:

                    st.info(
                        "Forecast information is not available."
                    )


        else:

            st.info(
                result["answer"]
            )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "AI Weather Assistant • "
    "Powered by Hugging Face and Open-Meteo"
)