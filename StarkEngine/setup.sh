#!/bin/bash
# STARK ENGINE v4.0 - Quick Setup Script

echo "========================================"
echo "STARK ENGINE v4.0 - Setup"
echo "========================================"
echo ""

# Check Python version
echo "Checking Python version..."
python3 --version

# Create virtual environment
echo ""
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "========================================"
echo "Setup complete!"
echo "========================================"
echo ""
echo "To run the application:"
echo "  source venv/bin/activate"
echo "  python stark_engine_v4_optimized.py"
echo ""
echo "To run benchmarks:"
echo "  source venv/bin/activate"
echo "  python benchmark.py"
echo ""
