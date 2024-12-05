"""
zly priklad
class ReportGenerator:
    def __init__(self, data, report_type="text"):
        self.data = data
        self.report_type = report_type

    def generate(self):
        if self.report_type == "text":
            return "Report:\n" + "\n".join([f"{key}: {value}" for key, value in self.data.items()])
        elif self.report_type == "html":
            html_content = "<html><body><h1>Report</h1><ul>"
            for key, value in self.data.items():
                html_content += f"<li>{key}: {value}</li>"
            html_content += "</ul></body></html>"
            return html_content
        elif self.report_type == "pdf":
            # Imagine this is a complex PDF generation logic
            return f"PDF Report -- {self.data}"
        else:
            raise ValueError(f"Unknown report type: {self.report_type}")
"""


class ReportGenerator:
    def __init__(self, data):
        self.data = data

    def generate(self):
        return "Report:\n" + "\n".join(
            [f"{key}: {value}" for key, value in self.data.items()]
        )


class HTMLReportGenerator(ReportGenerator):
    def generate(self):
        html_content = "<html><body><h1>Report</h1><ul>"
        for key, value in self.data.items():
            html_content += f"<li>{key}: {value}</li>"
        html_content += "</ul></body></html>"
        return html_content


class PDFReportGenerator(ReportGenerator):
    def generate(self):
        # Imagine this is a complex PDF generation logic
        return f"PDF Report -- {self.data}"
