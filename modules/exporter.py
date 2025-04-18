from typing import Dict, Any, Optional
from fpdf import FPDF
import os
import textwrap
from datetime import datetime
from pathlib import Path
OUTPUT_DIR = "../output"

#
BASE_DIR = Path(__file__).resolve().parent
print("BASE_DIR " , BASE_DIR)
font_path_B = BASE_DIR / "fonts" / "NotoSans-Bold.ttf"
font_path_I = BASE_DIR / "fonts" / "NotoSans-Italic.ttf"
font_path_R = BASE_DIR / "fonts" / "NotoSans-Regular.ttf"


class MeetingSummaryPDF(FPDF):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.alias_nb_pages()
        self.add_font('NotoSans', 'B', str(font_path_B), uni=True)
        self.add_font('NotoSans', 'I', str(font_path_I), uni=True)
        self.add_font('NotoSans', '', str(font_path_R), uni=True)
        self.set_font('NotoSans', '', 11)

    def header(self):
        """custom header for each page"""

        self.set_font('NotoSans', 'B', 15)
        # title
        self.cell(0, 10, 'Meeting Summary', 0, 1, 'C')
        # date
        self.set_font('NotoSans', 'I', 10)
        self.cell(
            0, 5, f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M')}", 0, 1, 'C')

        self.ln(10)

    def footer(self):
        """custom footer for each page"""
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        self.set_font('NotoSans', 'I', 8)
        # page number
        self.cell(
            0, 10, f'Page {self.page_no()}/{{nb}}', 0, 0, 'C')


def generate_pdf(transcript_id: str, transcript: str, summary: Dict[str, Any],
                 title: Optional[str] = None) -> str:
    """
    Generates a PDF report of the meeting transcript and summary.
    Args:
        transcript_id: Unique identifier for the transcript
        transcript: Full transcript text
        summary: Dictionary containing summary components
        title: Optional custom title for the PDF
    Returns:
        str: Path to the generated PDF file
    """
    pdf = MeetingSummaryPDF()
    pdf.add_page()

    # Set document information
    pdf.set_title(title or f"Meeting Summary - {transcript_id[:8]}")
    pdf.set_author("hivang26")

    # main content
    pdf.set_font('NotoSans', 'B', 14)
    pdf.cell(0, 10, "Meeting Overview", 0, 1)

    # overview
    pdf.set_font('NotoSans', '', 11)
    overview = summary.get("overview", "No overview available.")
    # Word wrap for long paras
    for line in textwrap.wrap(overview, width=75):
        pdf.cell(0, 5, line, 0, 1)
    pdf.ln(5)

    # key points
    pdf.set_font('NotoSans', 'B', 14)
    pdf.cell(0, 10, "Key Points", 0, 1)
    pdf.set_font('NotoSans', '', 11)
    key_points = summary.get("key_points", [])
    if key_points:
        for point in key_points:
            pdf.cell(5, 5, "-", 0, 0)
            # Word wrap for each bullet point
            lines = textwrap.wrap(point, width=70)
            if lines:
                pdf.cell(0, 5, lines[0], 0, 1)
                # Indent
                for line in lines[1:]:
                    pdf.cell(10, 5, "", 0, 0)
                    pdf.cell(0, 5, line, 0, 1)
            else:
                pdf.ln(5)
    else:
        pdf.cell(0, 5, "No key points identified.", 0, 1)
    pdf.ln(5)

    # action items
    pdf.set_font('NotoSans', 'B', 14)
    pdf.cell(0, 10, "Action Items", 0, 1)
    pdf.set_font('NotoSans', '', 11)
    action_items = summary.get("action_items", [])
    if action_items:
        for i, action in enumerate(action_items, 1):
            pdf.cell(10, 5, f"{i}.", 0, 0)
            # Word wrap for each action item
            lines = textwrap.wrap(action, width=65)
            if lines:
                pdf.cell(0, 5, lines[0], 0, 1)
                for line in lines[1:]:
                    pdf.cell(15, 5, "", 0, 0)
                    pdf.cell(0, 5, line, 0, 1)
            else:
                pdf.ln(5)
    else:
        pdf.cell(0, 5, "No action items identified.", 0, 1)
    pdf.ln(10)

    #   full transcript
    pdf.set_font('NotoSans', 'B', 14)
    pdf.cell(0, 10, "Full Transcript", 0, 1)
    pdf.set_font('NotoSans', '', 10)
    for line in textwrap.wrap(transcript, width=80):
        pdf.cell(0, 5, line, 0, 1)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, f"summary_{transcript_id}.pdf")
    pdf.output(output_path)
    return output_path
