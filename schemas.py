weather_schema = {
  "type": "object",
  "properties": {
    "coord": {
      "type": "object",
      "properties": {
        "lon": {
          "type": "number"
        },
        "lat": {
          "type": "number"
        }
      },
      "required": [
        "lon",
        "lat"
      ]
    },
    "weather": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "number"
          },
          "main": {
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "icon": {
            "type": "string"
          }
        },
        "required": [
          "id",
          "main",
          "description",
          "icon"
        ]
      }
    },
    "base": {
      "type": "string"
    },
    "main": {
      "type": "object",
      "properties": {
        "temp": {
          "type": "number"
        },
        "feels_like": {
          "type": "number"
        },
        "temp_min": {
          "type": "number"
        },
        "temp_max": {
          "type": "number"
        },
        "pressure": {
          "type": "number"
        },
        "humidity": {
          "type": "number"
        },
        "sea_level": {
          "type": "number"
        },
        "grnd_level": {
          "type": "number"
        }
      },
      "required": [
        "temp",
        "feels_like",
        "temp_min",
        "temp_max",
        "pressure",
        "humidity",
        "sea_level",
        "grnd_level"
      ]
    },
    "visibility": {
      "type": "number"
    },
    "wind": {
      "type": "object",
      "properties": {
        "speed": {
          "type": "number"
        },
        "deg": {
          "type": "number"
        },
        "gust": {
          "type": "number"
        }
      },
      "required": [
        "speed",
        "deg",
        "gust"
      ]
    },
    "clouds": {
      "type": "object",
      "properties": {
        "all": {
          "type": "number"
        }
      },
      "required": [
        "all"
      ]
    },
    "dt": {
      "type": "number"
    },
    "sys": {
      "type": "object",
      "properties": {
        "type": {
          "type": "number"
        },
        "id": {
          "type": "number"
        },
        "country": {
          "type": "string"
        },
        "sunrise": {
          "type": "number"
        },
        "sunset": {
          "type": "number"
        }
      },
      "required": [
        "type",
        "id",
        "country",
        "sunrise",
        "sunset"
      ]
    },
    "timezone": {
      "type": "number"
    },
    "id": {
      "type": "number"
    },
    "name": {
      "type": "string"
    },
    "cod": {
      "type": "number"
    }
  },
  "required": [
    "coord",
    "weather",
    "base",
    "main",
    "visibility",
    "wind",
    "clouds",
    "dt",
    "sys",
    "timezone",
    "id",
    "name",
    "cod"
  ]
}