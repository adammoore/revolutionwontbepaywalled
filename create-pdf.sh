#!/bin/bash

# Script to create PDF from the manifesto HTML file

HTML_FILE="manifesto-print.html"
PDF_FILE="TRWBP-Manifesto.pdf"

echo "Creating PDF from manifesto..."

# Method 1: Try Chrome/Chromium headless (if available)
if command -v google-chrome &> /dev/null; then
    echo "Using Chrome..."
    google-chrome --headless --disable-gpu --print-to-pdf="$PDF_FILE" --no-pdf-header-footer "$HTML_FILE"
    exit 0
elif command -v chromium &> /dev/null; then
    echo "Using Chromium..."
    chromium --headless --disable-gpu --print-to-pdf="$PDF_FILE" --no-pdf-header-footer "$HTML_FILE"
    exit 0
fi

# Method 2: Try wkhtmltopdf (if installed)
if command -v wkhtmltopdf &> /dev/null; then
    echo "Using wkhtmltopdf..."
    wkhtmltopdf --enable-local-file-access "$HTML_FILE" "$PDF_FILE"
    exit 0
fi

# Method 3: Try pandoc (if installed)
if command -v pandoc &> /dev/null; then
    echo "Using pandoc..."
    pandoc manifesto-for-pdf.md -o "$PDF_FILE" --pdf-engine=xelatex
    exit 0
fi

# If none work, provide manual instructions
echo ""
echo "⚠️  No automated PDF tools found."
echo ""
echo "Please create the PDF manually:"
echo ""
echo "Option 1: Using a Web Browser (Recommended)"
echo "  1. Open: manifesto-print.html in Safari, Chrome, or Firefox"
echo "  2. Press Cmd+P to open Print dialog"
echo "  3. Select 'Save as PDF' from the PDF dropdown"
echo "  4. Save as: TRWBP-Manifesto.pdf"
echo ""
echo "Option 2: Install required tools"
echo "  brew install pandoc  # Then run this script again"
echo "  or"
echo "  brew install wkhtmltopdf  # Then run this script again"
echo ""
