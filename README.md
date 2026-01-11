# Comcast RDK Programming Exercises

This repository contains programming exercises completed as part of the Comcast RDK assessment.

## Repository Structure

```
ComcastRDK/
├── E1/                      # Exercise 1: Weather CLI Application
│   ├── weather_app.py       # Main application file
│   ├── requirements.txt     # Python dependencies
│   ├── setup.sh            # Automated setup script
│   └── README.md           # Detailed documentation
│
├── E2/                      # Exercise 2: Median Finder Program
│   ├── median_finder.py    # Main application file
│   └── README.md           # Detailed documentation
│
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## Projects Overview

### E1: Weather CLI Application 🌤️

A command-line weather application that integrates with the OpenWeather API to provide real-time weather information for cities worldwide.

**Key Features:**
- Search weather by city name
- Manage favourite cities (max 3)
- Display comprehensive weather data (temperature, humidity, wind speed, etc.)
- User-friendly CLI interface with emoji indicators
- Error handling for API and network issues

**Technologies:** Python 3.7+, requests library, OpenWeather API

[View E1 Documentation →](E1/README.md)

**Quick Start:**
```bash
cd E1
./setup.sh
source venv/bin/activate
python weather_app.py
```

---

### E2: Median Finder Program 🔢

A Python program that implements a sorting algorithm and calculates the median of an array of numbers, demonstrating the conversion of pseudocode into working code.

**Key Features:**
- Custom Bubble Sort implementation with optimization
- Accurate median calculation for odd/even arrays
- Predefined test cases for demonstration
- Interactive user input mode
- No external dependencies required

**Technologies:** Python 3.x (standard library only)

[View E2 Documentation →](E2/README.md)

**Quick Start:**
```bash
cd E2
python3 median_finder.py
```

---

## Requirements

### General
- **Python**: 3.7 or higher
- **Operating System**: macOS, Linux, or Windows
- **Git**: For cloning the repository

### Project-Specific
- **E1**: Requires `requests` library and OpenWeather API key
- **E2**: No external dependencies

## Installation

### Clone the Repository

```bash
git clone git@github.com:stecadri/ComcastRDK.git
cd ComcastRDK
```

### Setup Individual Projects

Each project has its own setup instructions. Refer to the respective README files:
- [E1 Setup Instructions](E1/README.md#installation)
- [E2 Setup Instructions](E2/README.md#installation)

## Testing

### E1: Weather CLI Application
```bash
cd E1
source venv/bin/activate
python weather_app.py
# Follow the interactive prompts
```

### E2: Median Finder Program
```bash
cd E2
python3 median_finder.py
# The program will run test cases and allow custom input
```

## Project Highlights

### E1 Features
- **API Integration**: Seamless integration with OpenWeather API
- **State Management**: In-memory storage for favourite cities
- **Error Resilience**: Comprehensive error handling for various scenarios

### E2 Features
- **Algorithm Implementation**: Optimized Bubble Sort
- **Mathematical Accuracy**: Correct median calculation for all cases
- **Test Coverage**: Multiple test cases

## Future Enhancements

### E1 Potential Improvements
- Persistent storage for favourite cities (SQLite/JSON)
- Extended weather forecasts (5-day, 7-day)
- Unit conversion (Fahrenheit)
- Weather alerts and notifications
- Data export capabilities

### E2 Potential Improvements
- Additional sorting algorithms (Quick Sort, Merge Sort)
- Performance benchmarking
- File input support
- Sorting visualization
- Extended statistical functions