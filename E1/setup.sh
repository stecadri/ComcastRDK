#!/bin/bash
# Setup script for Weather CLI Application

echo "======================================"
echo "Weather App Setup Script"
echo "======================================"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "======================================"
echo "Setup Complete!"
echo "======================================"
echo ""
echo "To run the application:"
echo "1. Activate the virtual environment:"
echo "   source venv/bin/activate"
echo ""
echo "2. Run the app:"
echo "   python weather_app.py"
echo ""
echo "3. When done, deactivate the virtual environment:"
echo "   deactivate"
echo ""
