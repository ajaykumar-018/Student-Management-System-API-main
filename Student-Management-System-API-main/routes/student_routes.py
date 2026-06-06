from flask import Blueprint, jsonify, request
from models.student import( create_student,get_all_students,get_student_by_id,update_student,delete_student)
student_bp = Blueprint("student_bp", __name__)

@student_bp.route("/students", methods=["POST"])
def create_student_route():
    data = request.get_json()

    # Step 1: JSON check
    if data is None:
        return jsonify({"message": "Request must be JSON"}), 400

    # Step 2: required fields
    required_fields = ["name", "department", "course", "academic_session"]

    for field in required_fields:
        if field not in data:
            return jsonify({"message": f"attribute {field} missing"}), 400

        if not str(data[field]).strip():
            return jsonify({"message": f"attribute {field} cannot be empty"}), 400

    # Step 3: success
    saved = create_student(data)
    if not saved:
        return jsonify({"message": "Failed to save student"}), 500

    return jsonify({
        "message": "Student received successfully",
        "data": data
    }), 201

@student_bp.route("/students", methods=["GET"])
def get_students_route():
    students = get_all_students()

    if students is None:
        return jsonify({"message": "Failed to fetch students"}), 500

    return jsonify({
        "data": students
    }), 200

@student_bp.route("/students/<int:student_id>", methods=["GET"])
def get_student_by_id_route(student_id):
    student = get_student_by_id(student_id)

    if student is None:
        return jsonify({"message": "Student not found"}), 404

    return jsonify({
        "data": student
    }), 200

@student_bp.route("/students/<int:student_id>", methods=["PUT"])
def update_student_route(student_id):
    data = request.get_json()

    if data is None:
        return jsonify({"message": "Request must be JSON"}), 400

    required_fields = ["name", "department", "course", "academic_session"]

    for field in required_fields:
        if field not in data:
            return jsonify({"message": f"attribute {field} missing"}), 400

        if not str(data[field]).strip():
            return jsonify({"message": f"attribute {field} cannot be empty"}), 400

    result = update_student(student_id, data)

    if result == 0:
        return jsonify({"message": "Student not found"}), 404

    if result == -1:
        return jsonify({"message": "Failed to update student"}), 500

    return jsonify({"message": "Student updated successfully"}), 200

@student_bp.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student_route(student_id):
    result = delete_student(student_id)

    if result == 0:
        return jsonify({"message": "Student not found"}), 404

    if result == -1:
        return jsonify({"message": "Failed to delete student"}), 500

    return jsonify({"message": "Student deleted successfully"}), 200
