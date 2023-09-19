from flask import Flask, jsonify
import data_uploader

app = Flask(__name__)

@app.route('/process-file', methods=['POST'])
def processFile():
	list_id = 1 
	csv_file_path = 'list.csv'
	data_uploader.read_and_upload_csv.apply_async(args=(list_id, csv_file_path))
	return jsonify({'message': 'We have received your message and we will process it soon.'})

if __name__ == '__main__':
    app.run(debug=True)