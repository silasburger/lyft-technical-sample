from flask import Flask, request, jsonify
from cut_string import cut_string
from error import InvalidUsage

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def test():
    """Handles cutting a string.

    A return strign is sent back containing every third character of the request string.

    If request isn't valid an error is sent as response.
    """
    req_string = request.json.get('string_to_cut', None)

    if req_string is None:
        raise InvalidUsage("\"string_to_cut\" key not provided in body of request", 400)
    res_string = cut_string(req_string)

    return jsonify(return_string=res_string)

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    """Handles errors.
    """
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response