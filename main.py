from flask import Flask

app = Flask(__name__)


@app.route('/sample_file_upload', methods=['POST', 'GET'])
def sample_file_upload():
    return '''<html lang="en">
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="static/style.css">
</head>
<body>
    <div id="carouselExampleSlidesOnly" class="carousel slide" data-bs-ride="carousel" data-bs-interval="2000">
        <div class="carousel-inner">
            <div class="carousel-item active">
                <img class="d-block w-100" src="static/img1.jpg" alt="First slide">
            </div>
            <div class="carousel-item">
                <img class="d-block w-100" src="static/img2.jpg" alt="Second slide">
            </div>
            <div class="carousel-item">
                <img class="d-block w-100" src="static/img3.jpg" alt="Third slide">
            </div>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
