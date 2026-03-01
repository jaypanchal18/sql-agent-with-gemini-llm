import json
from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError

class ResultFormatter:
    def __init__(self, data, format_type='json'):
        self.data = data
        self.format_type = format_type.lower()

    def format_results(self):
        try:
            if self.format_type == 'json':
                return self.format_as_json()
            elif self.format_type == 'html':
                return self.format_as_html()
            else:
                raise ValueError("Unsupported format type. Use 'json' or 'html'.")
        except Exception as e:
            return self.handle_error(e)

    def format_as_json(self):
        return jsonify(self.data)

    def format_as_html(self):
        html_content = '<table>'
        if isinstance(self.data, list) and len(self.data) > 0:
            headers = self.data[0].keys()
            html_content += '<tr>' + ''.join(f'<th>{header}</th>' for header in headers) + '</tr>'
            for row in self.data:
                html_content += '<tr>' + ''.join(f'<td>{row[header]}</td>' for header in headers) + '</tr>'
        html_content += '</table>'
        return html_content

    def handle_error(self, error):
        error_message = {
            'error': str(error)
        }
        return jsonify(error_message), 500

def format_query_results(data, format_type='json'):
    formatter = ResultFormatter(data, format_type)
    return formatter.format_results()