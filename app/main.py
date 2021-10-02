from flask import Flask, jsonify, request, render_template
from torch_utils import transform_image, get_prediction, classes


app = Flask(__name__, template_folder='templates')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    return('.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files.get('file')
        print(type(file))
        if file is None or file.filename == "":
            return(jsonify({'ERROR': 'no file'}))
        if not allowed_file(file.filename):
            return(jsonify({'ERROR': 'format not supported'}))

        try:
            img_bytes = file.read()
            tensor = transform_image(img_bytes)
            prediction = get_prediction(tensor)

            class_name =  classes[prediction.item()]

            '''data = {'prediction': prediction.item(),
                    'class_name': str(prediction.item())}'''

            #return(jsonify(class_name))
            return(render_template('results.html', pred=class_name))
        except Exception as e:
            print(e)
            return(jsonify({'error': e}))

if __name__ == '__main__':
    app.run(debug=True)
